# Rounded enclosure test print

This directory contains a separate, unvalidated rounded variant; the original STEP and STL files remain unchanged.

| Part | Exterior fillet | Bounding dimensions | STL triangles |
|---|---:|---:|---:|
| `front-rounded` | 1.5 mm | 62.99 × 130.39 × 15.70 mm | 3,528 |
| `rear-rounded` | 0.8 mm | 56.65 × 123.90 × 2.20 mm | 2,658 |

The front fillet follows the eight outer edges of its rear-facing perimeter. The rear fillet follows twenty edges around its exposed outer face. The mating face and central rear recess were excluded from the rear operation.

Use the STL files for the test print. The STEP files are included so the radii or other geometry can be adjusted without modifying the originals. Inspect the sliced preview carefully and complete the validation checklist in the parent README before fitting a LiPo cell or powering the charger.

To regenerate the files, install `cadquery-ocp` and run:

```sh
python case/tools/make_rounded_preview.py
```
