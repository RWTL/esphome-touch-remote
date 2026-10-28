# Release process

Versions use Semantic Versioning and a `v`-prefixed Git tag, such as `v0.1.0`.

1. Validate the example configuration with every ESPHome version listed as supported in the README.
2. Test the firmware on the target board, including touch wake, Home Assistant reconnection, deep sleep and OTA mode.
3. Test-print both enclosure parts and record the slicer, material and important tolerances in `case/README.md`.
4. Export `front.stl`, `rear.stl` and, preferably, a ready-to-print `ha-remote.3mf` from the authoritative STEP files.
5. Update `VERSION`, the version in `remote/core.yaml`, the compatibility table, and `CHANGELOG.md`.
6. Commit the changes, create an annotated `vX.Y.Z` tag and publish a GitHub release.
7. Attach the STL/3MF files to the release and keep the latest validated exports under `case/print/`.

Do not call an enclosure release validated until both halves have been printed and checked against the actual display board, battery, charging receiver, fasteners and USB connection.
