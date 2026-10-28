"""Create conservative rounded enclosure variants from the original STEP solids.

Requires cadquery-ocp. The generated models are prototypes and still require a
physical fit test before promotion to case/print/.
"""

from pathlib import Path

from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.BRepCheck import BRepCheck_Analyzer
from OCP.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.IFSelect import IFSelect_RetDone
from OCP.STEPControl import (
    STEPControl_AsIs,
    STEPControl_Reader,
    STEPControl_Writer,
)
from OCP.StlAPI import StlAPI_Writer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopExp import TopExp_Explorer
from OCP.TopoDS import TopoDS


CASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = CASE_DIR / "rounded-preview"


def unique_edges(shape):
    explorer = TopExp_Explorer(shape, TopAbs_EDGE)
    edges = []
    while explorer.More():
        edge = TopoDS.Edge(explorer.Current())
        if not any(edge.IsSame(existing) for existing in edges):
            edges.append(edge)
        explorer.Next()
    return edges


def bounds(edge):
    box = Bnd_Box()
    BRepBndLib.Add_s(edge, box)
    return (
        box.GetXMin(), box.GetYMin(), box.GetZMin(),
        box.GetXMax(), box.GetYMax(), box.GetZMax(),
    )


def is_front_outer_edge(edge):
    x0, y0, z0, x1, y1, z1 = bounds(edge)
    on_back_face = abs(z0 - 15.7) < 0.01 and abs(z1 - 15.7) < 0.01
    on_outline = x0 < -0.9 or x1 > 60.9 or y0 < -0.9 or y1 > 128.3
    return on_back_face and on_outline


def is_rear_outer_edge(edge):
    x0, y0, z0, x1, y1, z1 = bounds(edge)
    on_outer_face = abs(z0) < 0.01 and abs(z1) < 0.01
    in_central_recess = x0 >= 21.9 and x1 <= 38.1 and y0 >= 80.6 and y1 <= 100.1
    return on_outer_face and not in_central_recess


def rounded_shape(name, radius, selector):
    reader = STEPControl_Reader()
    if reader.ReadFile(str(CASE_DIR / f"{name}.step")) != IFSelect_RetDone:
        raise RuntimeError(f"Could not read {name}.step")
    reader.TransferRoots()
    source = reader.OneShape()

    fillet = BRepFilletAPI_MakeFillet(source)
    selected = [edge for edge in unique_edges(source) if selector(edge)]
    for edge in selected:
        fillet.Add(radius, edge)
    fillet.Build()
    if not fillet.IsDone():
        raise RuntimeError(f"{name}: {radius} mm fillet failed")

    result = fillet.Shape()
    if not BRepCheck_Analyzer(result).IsValid():
        raise RuntimeError(f"{name}: rounded solid is invalid")
    print(f"{name}: rounded {len(selected)} edges at {radius} mm")
    return result


def export(name, shape):
    step_writer = STEPControl_Writer()
    step_writer.Transfer(shape, STEPControl_AsIs)
    step_path = OUTPUT_DIR / f"{name}-rounded.step"
    if step_writer.Write(str(step_path)) != IFSelect_RetDone:
        raise RuntimeError(f"Could not write {step_path}")

    mesh = BRepMesh_IncrementalMesh(shape, 0.08, False, 0.35, True)
    mesh.Perform()
    if not mesh.IsDone():
        raise RuntimeError(f"Could not mesh rounded {name}")
    stl_writer = StlAPI_Writer()
    stl_writer.ASCIIMode = False
    stl_path = OUTPUT_DIR / f"{name}-rounded.stl"
    if not stl_writer.Write(shape, str(stl_path)):
        raise RuntimeError(f"Could not write {stl_path}")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    export("front", rounded_shape("front", 1.5, is_front_outer_edge))
    export("rear", rounded_shape("rear", 0.8, is_rear_outer_edge))


if __name__ == "__main__":
    main()
