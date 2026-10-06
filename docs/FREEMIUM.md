# SortOut — Free vs Pro

SortOut is free to use. **SortOut Pro** unlocks three advanced algorithms.
Every algorithm can be **previewed for free** — Pro is only needed to *apply*
a Pro plan, so you see exactly what you are paying for (try before you buy).

## Tiers

| Feature | Free | Pro |
|---|:---:|:---:|
| By File Type · Smart Name Grouping · Custom Pattern · Move All Together | ✅ | ✅ |
| Date Organizer · By File Size · Keyword Tagger | ✅ | ✅ |
| Preview (scan + proposed tree) of **every** algorithm | ✅ | ✅ |
| Duplicate Finder — byte-identical sets, recoverable space, never deletes | 👀 preview | ✅ |
| Project / Code Detector — whole projects moved intact, grouped by language | 👀 preview | ✅ |
| AI Grouping — OpenAI / Gemini / local Ollama | 👀 preview | ✅ |
| Profiles (3 built-in + your own) | ✅ | ✅ |
| One-click Undo + History with per-run revert | ✅ | ✅ |
| Inline folder rename, filter, stats bar, Edit as JSON | ✅ | ✅ |
| Dark mode, remembered windows and settings | ✅ | ✅ |
| `.sortout-ignore` rules | ✅ | ✅ |
| Command line incl. `--dry-run` JSON | ✅ | ✅ |

Pro algorithms are marked 🔒 in the algorithm list while you're on Free.

## Try before you buy
Pick a 🔒 algorithm and click **Scan & Preview**. The proposal window shows the
real plan behind a blur with a summary of what was found — e.g. *"You found 12
duplicates — 1.4 GB recoverable"*, *"Found 5 projects"* or *"AI created 8
groups for 240 files"*. **Apply Changes** needs Pro. On the command line, `--dry-run` works for every
algorithm; applying a Pro algorithm without a licence exits with code `3`.

## How to buy and activate
1. Open **Help → Enter License Key…** and click **Copy** next to your
   **Machine ID** (or run `SortOut-cli.exe --machine-id`).
2. Click **Get SortOut Pro** (header button or Help menu). It opens the store
   page — include your Machine ID with the order.
3. You receive a key like `SORTOUT-PRO-ABCD2345`. Paste it into
   **Help → Enter License Key… → Activate** (or run
   `SortOut-cli.exe --license-key SORTOUT-PRO-ABCD2345`).
   Pro unlocks immediately — no restart; the header badge changes to **PRO**.

Keys are case- and space-insensitive and are bound to one computer. Moving to
a new PC? Contact support with your old and new Machine IDs.

## Offline behaviour
- Activation first asks the licence server (3-second timeout). If it can't be
  reached, the key is checked offline, so activation works without internet.
- The result is cached for 24 hours. After that SortOut re-checks **in the
  background** — startup never waits for the network. If you're offline and
  the key is still valid for this machine, Pro stays active.
- Typing a wrong key never removes a licence that is already active.

## Privacy
- No telemetry. Activation sends only the key, the Machine ID (an anonymous
  hash), the product name and the version.
- AI Grouping sends **file names only** (never contents) to the cloud provider
  you choose, after asking for your consent — or nothing leaves your PC when
  you use local Ollama.
