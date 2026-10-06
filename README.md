👉 **[Download SortOut 2.0 for Windows — SortOut.exe](https://github.com/OfficialAshish/SortOut/raw/main/executable/dist/SortOut.exe)**
· [SortOut-cli.exe](https://github.com/OfficialAshish/SortOut/raw/main/executable/dist/SortOut-cli.exe) (command line)
· [SHA256SUMS.txt](https://github.com/OfficialAshish/SortOut/raw/main/executable/dist/SHA256SUMS.txt)

# SortOut 2.0 — Smart File Organizer for Windows

Turn a messy folder into a tidy one in three steps: **choose a folder → pick
how to group it → preview and apply.** Nothing moves until you've seen the
plan, copying is the default, and every run can be undone with one click.

## Free vs Pro
| | Free | Pro |
|---|:---:|:---:|
| By File Type · Smart Name Grouping · Date Organizer · By File Size · Keyword Tagger · Custom Pattern · Move All Together | ✅ | ✅ |
| Preview **every** algorithm, including Pro ones | ✅ | ✅ |
| Duplicate Finder — byte-identical files, recoverable space, never deletes | 👀 preview | ✅ |
| Project / Code Detector — moves whole projects intact, grouped by language | 👀 preview | ✅ |
| AI Grouping — OpenAI, Gemini or fully-offline Ollama, file names only | 👀 preview | ✅ |
| Profiles · History with per-run undo · inline rename · filter · stats · dark mode · `.sortout-ignore` · command line | ✅ | ✅ |

How to buy, activate and what stays offline: **[docs/FREEMIUM.md](docs/FREEMIUM.md)**.

## Get started
1. Download `SortOut.exe` (no installer) and double-click it. Windows
   SmartScreen may warn about an unrecognised app: **More info → Run anyway**.
2. Drag a folder onto **Choose a folder** (or click **Browse…**) and pick an
   algorithm — each one explains when to use it.
3. Optional, under **Options**: skip hidden & system files, put files straight
   into their group folder (**Discard file paths**), move instead of copy,
   remove folders left empty after moving.
4. Click **Scan & Preview**, rename any proposed folder (F2), switch
   **Discard / Preserve File Path** (hover the **?** for help), choose Copy or
   Move, then **Apply Changes**. Changed your mind? **Undo** — or later via
   **File → History…**.

Check the download: `Get-FileHash SortOut.exe` must match the value in
`SHA256SUMS.txt`.

## Command line (optional)
`SortOut-cli.exe` is the console version of the same app:
```bat
SortOut-cli.exe "C:\Users\me\Downloads" --dry-run                  :: preview as JSON
SortOut-cli.exe D:\Photos -a date_organizer --granularity year -y  :: copy into D:\Photos\SortedOut
SortOut-cli.exe D:\Inbox --discard-paths --skip-hidden --move --prune-empty-dirs -y
SortOut-cli.exe --revert "D:\Photos\SortedOut" -y                  :: undo
SortOut-cli.exe --help
```
Exit codes: `0` ok · `1` error · `2` usage / bad folder · `3` Pro required ·
`4` AI failed · `130` cancelled.

## Privacy
No telemetry. Settings, history and logs stay in `%USERPROFILE%\.sortout\`;
AI keys are encrypted with Windows DPAPI. AI Grouping sends **file names
only** — never contents — and only after you agree; Ollama keeps everything on
your PC.

## Support
Feedback and licence questions: aashish06327@gmail.com

© 2026 OfficialAshish. All rights reserved. SortOut is proprietary software.
