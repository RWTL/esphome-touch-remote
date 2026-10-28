# Preview mesh exports

These binary STL files are automated tessellations of the STEP solids, provided for inspection and prototype prints. They are **not physically validated release artifacts**.

| File | STEP bounding dimensions | Triangles |
|---|---:|---:|
| `front.stl` | 62.99 × 130.39 × 15.70 mm | 2,808 |
| `rear.stl` | 54.80 × 123.60 × 2.20 mm | 748 |

The meshes use millimetres, a 0.08 mm linear deflection and a 0.35 radian angular deflection. Complete the checklist in the parent README before promoting them to `case/print/` or including them in a release. A 3MF should be made from the physically validated meshes so it can also preserve print orientation and slicer settings.
