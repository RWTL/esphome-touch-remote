# 3D-printed case

> **Prototype — not a validated production enclosure.** The editable solid models are published, but this revision has not yet completed the release test-print checklist below.

The case is a two-part shell (front and back) that holds the **Freenove ESP32-S3 2.8" display**, the LiPo battery and the Qi wireless charging receiver.

<!-- Add a photo here: ![Case](../images/case.jpg) -->

## Files

The authoritative **STEP** files of the front and back shell are in this folder. You can open and modify them in any CAD program (Fusion, FreeCAD, Onshape…) or import them directly into many slicers.

Automated STL exports are available under [`preview/`](preview/) for inspection and prototype prints. They are clearly separated from release artifacts because they have not passed a physical fit check. Validated STL and 3MF files will be placed in `case/print/` and attached to a versioned GitHub release.

A separate [`rounded-preview/`](rounded-preview/) variant rounds the exposed enclosure edges while leaving the original models unchanged. It includes printable STL files, editable STEP files and the exact fillet dimensions used.

## What's inside

- Freenove ESP32-S3 Display 2.8" (PCB 50 × 86 mm), fixed with self-tapping screws
- LiPo battery 102050 (1000 mAh), in an extension next to the screen
- Qi wireless charging receiver with USB-C output, behind the board

## Validation checklist

- [ ] Confirm PCB mounting-hole locations and screw engagement.
- [ ] Confirm display and touch-active-area alignment.
- [ ] Confirm battery clearance without pinching or bending the cell.
- [ ] Confirm Qi receiver clearance, alignment and charging temperature.
- [ ] Confirm USB connector access and cable strain relief.
- [ ] Confirm snap/screw fit after material shrinkage.
- [ ] Check wake-on-touch operation in the closed case.
- [ ] Record slicer, layer height, walls, supports, material and tolerances.
- [ ] Export and inspect binary STL files in millimetres.
- [ ] Save a ready-to-print 3MF with both parts correctly oriented.

## Planned mechanical revision

- Round the shell into a more ergonomic handheld shape.
- Add explicit battery and Qi-receiver retention instead of relying on compression.
- Verify ventilation and charging temperature before considering TPU edge features.
- Print the final rigid shell in PETG after fit validation.

Ideas and suggestions are welcome!
