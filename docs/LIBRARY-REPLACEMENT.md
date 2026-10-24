# Qt / PySide library rights and replacement

SortOut uses unmodified PySide6 Essentials, Shiboken6 and the Qt6 components listed
in `SBOM.json`. Covered library rights are not restricted by SortOut's proprietary
licence. You may modify/replace/relink these libraries and reverse engineer SortOut
to debug modifications to those LGPL libraries, as permitted by their licences.
No private signing key, application-source access or publisher permission is needed
to run ABI-compatible replacement libraries in this portable/ordinary install build.

1. Close SortOut. Back up the entire portable or installed folder. Do not experiment
   on your only copy of files or Undo history. You can copy the installed app folder
   to a user-writable test location; it does not need to run from its install path.
2. Locate the library paths using `SBOM.json`: PySide6, shiboken6 and Qt DLLs/plugins
   are external files under `_internal`, not embedded in the executable. Their
   checksums in the inventory are documentation, not an enforced runtime allowlist.
3. Download the accompanying `SortOut-Qt-Sources.zip` from the same release. It
   contains exact unmodified upstream archives, hashes and download URLs. Qt base,
   SVG/image-format plugins and PySide/Shiboken sources are included. Source archives
   include their build scripts, licence texts and upstream build documentation.
4. Build the components you want to modify for Windows x64, the recorded Qt/PySide
   ABI and CPython minor version in `SBOM.json` (the shipped build uses CPython 3.12).
   Use a compatible MSVC release toolchain. See the source-tree README and official
   Qt for Python build instructions: https://doc.qt.io/qtforpython-6/building_from_source/index.html
   and Qt Windows build instructions: https://doc.qt.io/qt-6/windows-building.html .
   Build the corresponding dependent components together if you change their ABI.
5. Replace the matching external DLL/PYD/plugin files in your test copy, preserving
   their relative paths. Do not mix x86/ARM64 and x64 binaries. Retain licence notices.
6. Run `SortOut-cli.exe --version`, then launch `SortOut.exe` from your test copy.
   Test on disposable folders first. Restore your backup to return to the official
   libraries. Modified library distributions are your responsibility, not endorsed
   by Qt or OfficialAshish. The application contains no library-signature/hash lock.

The installer merely copies this same folder; it does not create a locked Store
package. This release does not claim MSIX/Store licensing approval. Never replace
system-wide DLLs or disable operating-system security to perform these steps.

Exact source manifests, library licence texts and third-party copyright notices
are in `source-manifest.json`, `THIRD-PARTY-NOTICES.txt` and `third-party-licenses/`.
