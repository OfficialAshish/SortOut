# SortOut — review first, organize with confidence

Windows file organizer by Ashish Prajapati, trading as SortOut. Smart Rules, file type/name/date/size/
keyword organization, preview, profiles, History and Undo are Free. Duplicate
Finder and optional AI Grouping can be previewed for Free; applying those plans
requires Pro. Project / Code Detector is parked for a future release.

## Qt6 download status

[Download SortOut 2.3.2 — Qt6 Free preview](https://github.com/OfficialAshish/SortOut/releases/tag/v2.3.2-qt6-preview).
Windows x64: choose **SortOut-2.3.2-Setup.exe** or **SortOut-Portable-Windows.zip**.
This is a tested direct-download preview, **not a paid commercial launch or
Microsoft Store approval**. Historical PyQt-based packages are not the current
recommended downloads; migration does not retroactively clear their licensing.

The Windows installer now offers **Launch SortOut** on Finish and includes
Installed apps icon, size and SortOut publisher details. Close the app, then
install the new version over the old one; settings and Undo history are retained.

The new distribution offers:
- **Offline per-user installer:** no administrator permission intended; includes
  its runtime rather than downloading components during installation.
- **Portable ZIP:** extract the entire folder, then run `SortOut.exe`. CLI users
  run `SortOut-cli.exe`. Keep `_internal` and the companion files together.
- **SHA256SUMS.txt**, offline component notices, library replacement instructions
  and an accompanying exact upstream Qt/PySide source archive.

Initial direct-download packages are unsigned. Windows may warn about the
publisher. Verify the release origin and hashes and make your own trust decision;
SortOut does not require disabling security settings. Back up important files and
try a small disposable folder first. Undo depends on records/files still being
available and is not a backup.

## Pro checkout status

**New purchases are not open.** No merchant checkout or automatic licence-key
email delivery is connected. Do not send payment or a Machine ID to an unverified
store. Existing privately issued SortOut keys remain supported. New checkout is
planned without a pre-purchase Machine ID field, but its activation integration
still needs implementation and merchant verification before sales.

See [Free vs Pro](docs/FREEMIUM.md) and [Smart Rules](docs/SMART_RULES.md).
File operations run locally. Optional cloud AI sends disclosed metadata after
consent; local records are not all encrypted. The app's legal policies remain
clearly marked review drafts, not effective purchase terms.

## Website and updates

Website source is in [website/](website/). It is ready to connect to a static
Cloudflare Pages host with a free provider subdomain. No backend or custom domain
is required. It has no active checkout or tracking scripts. It is not yet a live
hosted website. GitHub Pages is not the commercial-site host.

Updates are manual for now. There is no silent self-updater. Store-managed updates
remain a separate future distribution path requiring publisher onboarding,
package identity, certification and licensing review.

Support: ashish06327@gmail.com · Project location: Pune, Maharashtra, India.
SortOut is a product/trading label, not a claim of an incorporated company.
Third-party component rights remain governed by their own licences.

## Product tour
Explore all ten active algorithms, actual application screenshots and the Free/Pro comparison at https://sortout-8sb.pages.dev/ . Site source lives in `website/`; Cloudflare Pages deploys public `main` automatically. Paid checkout remains disabled pending activation and seller/legal readiness.
