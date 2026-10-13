# SortOut — Free vs Pro

SortOut is free to use. **SortOut Pro** unlocks two advanced algorithms.
Every algorithm can be **previewed for free** — Pro is only needed to *apply*
a Pro plan, so you see exactly what you are paying for (try before you buy).

## Tiers

| Feature | Free | Pro |
|---|:---:|:---:|
| By File Type · Smart Name Grouping · Custom Pattern · Move All Together | ✅ | ✅ |
| Smart Rules · Date Organizer · By File Size · Keyword Tagger | ✅ | ✅ |
| Preview (scan + proposed tree) of **every** algorithm | ✅ | ✅ |
| Duplicate Finder — byte-identical sets, review, copies to the Recycle Bin (undoable) | 👀 preview | ✅ |
| AI Grouping — OpenAI / Gemini / Claude / custom compatible services / local Ollama | 👀 preview | ✅ |
| Profiles (2 built-in + your own) | ✅ | ✅ |
| One-click Undo + History with per-run revert | ✅ | ✅ |
| Inline folder rename, filter, stats bar, Edit as JSON | ✅ | ✅ |
| Dark mode, remembered windows and settings | ✅ | ✅ |
| `.sortout-ignore` rules | ✅ | ✅ |
| Command line incl. `--dry-run` JSON | ✅ | ✅ |

Project / Code Detector and Developer Workspace are **parked for a future release**
and are not available in this release. Existing custom profiles for the parked
algorithm are preserved on disk but hidden from the selectable profile list.

Pro algorithms are marked 🔒 in the algorithm list while you're on Free.

## Try before you buy
Duplicate Finder opens a review of the matching files for free; choosing and
inspecting copies does not require Pro. Sending the extra copies to the Recycle
Bin requires Pro and confirmation. AI Grouping can also be previewed for free;
applying its proposed grouping requires Pro. The ordinary organizing algorithms
remain free to scan, preview and apply.

On the command line, `--dry-run` works for every available algorithm. Applying a
Pro algorithm without a licence exits with code `3`. Project / Code Detector is
parked, not a Pro option in this release.

## New: your rules, without a subscription
**Smart Rules is Free** to scan, edit, preview and apply. Build ordered conditions
using file type, name, relative path, size or days since modified. Starter presets
cover downloads, office files and large/old files. First match wins; unmatched
files stay put. Save rules in a profile or import/export them as JSON. Rules run
offline and never read file contents; no background watcher silently moves files.

Repeat Duplicate Finder scans can reuse full hashes from a bounded local cache.
Fresh file identity/change stamps and head/tail samples are required for a hit;
unsupported storage or cache problems fall back to fresh hashing. Cleanup always
rechecks full contents before binning. Disable or clear the cache in Settings →
Organizing, or with `--no-scan-cache` / `--clear-scan-cache`. Scanning every folder
and checking current metadata still takes time; the cache is not an instant scan.

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

- The optional duplicate-hash cache is local and bounded (20,000 entries / 7-day
  validity). It stores hashed path keys, signatures and digests, not plaintext
  paths or file contents. Clearing it does not remove source files or Undo data.
