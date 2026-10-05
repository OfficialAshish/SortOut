👉 **[Download SortOut 2.0 (Windows, SortOut.exe)](https://github.com/OfficialAshish/SortOut/raw/main/executable/dist/SortOut.exe)**

# SortOut 2.0 — Smart File Organizer for Windows

Turn a messy folder into a tidy one: **pick an algorithm → preview → apply**,
and undo with one click if you change your mind.

## What's new in 2.0
- **10 ways to organise**
  - Free: By File Type · Smart Name Grouping · Date Organizer · By File Size ·
    Keyword Tagger · Custom Pattern · Move All Together
  - Pro: Duplicate Finder · Project / Code Detector · AI Grouping (OpenAI,
    Gemini or fully-offline Ollama)
- **Preview everything first**: a folder tree with sizes, search filter, inline
  rename and a stats bar. Pro results can be previewed for free.
- **Safe by default**: copies (not moves) unless you choose otherwise; exact
  one-click **Revert**; **View History** with per-run undo.
- **Profiles**: 📸 Photos & Media, 💻 Developer Workspace, 📥 Downloads Cleanup —
  or save your own.
- **`.sortout-ignore`** rules to skip files/folders, **dark mode**, and a full
  **command line** (`SortOut.exe --help`).

Free vs Pro, how to buy and privacy: **[docs/FREEMIUM.md](docs/FREEMIUM.md)**.

## Install
1. Download `SortOut.exe` (no installer needed) and double-click it.
2. Windows SmartScreen may warn about an unrecognised app: click
   **More info → Run anyway**.

SHA256 of `SortOut.exe` 2.0.0: `BEA01A31815CFE2FCBB02B5F71F48207E83A0A9FB83D9BEECD547CCB349596DE`
(check with `Get-FileHash SortOut.exe`).

Settings, history and logs are stored in `%USERPROFILE%\.sortout\`.

## Command line (optional)
```powershell
SortOut.exe "C:\Users\me\Downloads" --dry-run | Out-Host          # preview as JSON
SortOut.exe D:\Photos -a date_organizer --granularity year -y | Out-Host
SortOut.exe --revert "D:\Photos\SortedOut" -y | Out-Host           # undo
```
(SortOut.exe is a windowed app — pipe to `Out-Host` in PowerShell, or use
`start /wait` in cmd, so the shell waits for it.) Exit codes: 0 ok, 1 error,
3 Pro required.

## Support
Feedback and licence questions: aashish06327@gmail.com

© 2026 OfficialAshish. All rights reserved. SortOut is proprietary software.
