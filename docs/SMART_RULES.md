# Smart Rules — your rules, your folders, no guesswork

**Free. Offline. Review first.** Turn repeated tidy-ups into a setup you control.

## A first tidy-up
1. Choose your Downloads folder; select **Smart Rules → Edit rules…**.
2. Keep **Downloads starter** or load **Office tidy** / **Large & old files**.
3. Edit a rule: name, All/Any conditions, Organize or Keep in place, relative folder.
4. Move specific rules above general ones: **first matching enabled rule wins**.
5. Save and **Scan & Preview**. Hover files for their original matched rule.
6. Review/edit the plan, choose Copy (default) or Move, then Apply. Undo/History
   works as with other organizing algorithms. Save a profile to reuse your rules.

Unmatched files stay where they are. Keep rules are sorting decisions, not access
controls: manual preview edits can still move those files. Rule reasons refer to
**the original scan**, not a rule re-evaluation after a manual edit. The app is not
a background watcher; age-based sorting does not mean automatic deletion.

## Conditions
- **File type:** comma-separated extensions, e.g. `pdf, .docx, jpg`.
- **File name / Relative path:** Contains or Matches wildcard (`*`, `?`, `[abc]`).
  Matching ignores letter case. A wildcard applies to the whole name/path;
  use `*invoice*` for a substring. Paths use `/`, relative to the scanned folder;
  wildcard `*` may cross folder separators.
- **Size (MB):** At least / At most, inclusive; 1 MB = 1,048,576 bytes.
- **Days since modified:** At least / At most, inclusive, at scan time.
  Future timestamps count as age 0. Unknown size/time does not match that condition.

All conditions means AND; Any means OR. Disabled rules remain saved but are not
run. Destinations are 1–4 safe relative folder segments, e.g. `Finance/Invoices`;
absolute paths, traversal and Windows-reserved names are rejected. Files retain
source subfolders within their group unless **Discard file paths** is enabled.

## Starters
- **Downloads starter:** invoice/receipt names plus file types first, then photos,
  documents and videos. Apps/archives and anything else remain in place.
- **Office tidy:** keep names containing `private`, then invoices, spreadsheets,
  presentations and documents. Customize protection before using it.
- **Large & old files:** videos ≥500 MB and documents modified ≥365 days ago.
  Age rules classify files for your review; they never delete them.

## Import, export and CLI
Export rules from the editor, edit the JSON if needed, then import it back.
Invalid imports do not replace the current editor setup. Cancel discards edits.
Imports accept UTF-8 JSON (optional BOM), up to 128 KB, 64 rules, 8 conditions each.
A rules file is not an exported preview-plan file; use the editor's Export action.

```json
{
  "version": 1,
  "rules": [
    {
      "name": "Invoices",
      "enabled": true,
      "action": "organize",
      "folder": "Finance/Invoices",
      "match": "all",
      "conditions": [
        {"field": "extension", "op": "in", "value": "pdf,docx"},
        {"field": "name", "op": "contains", "value": "invoice"}
      ]
    }
  ]
}
```

Supported fields/operators: `extension/in`; `name` or `path` with `contains/glob`;
`size_mb` or `age_days` with `ge/le`. Numeric values must be finite and ≥0.
Unknown fields/options, duplicate rule names and unsafe folders are rejected.

```bat
SortOut-cli.exe D:\Inbox -a smart_rules --dry-run
SortOut-cli.exe D:\Inbox -a smart_rules --rules-file my-rules.json --dry-run
SortOut-cli.exe D:\Inbox -a smart_rules --rules-file my-rules.json --move -y
SortOut-cli.exe --revert "D:\Inbox\SortedOut" -y
```

Without `--rules-file`, CLI uses Downloads starter. `--dry-run` is read-only;
`--move -y` applies without an interactive review, so inspect the dry-run first.
Rules look only at scanned metadata. They do not read document contents or send
anything to an AI provider. Duplicate Finder is a separate algorithm; Smart Rules
never deletes duplicates or silently chains another algorithm.
