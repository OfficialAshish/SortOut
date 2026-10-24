# SortOut static website

No backend, build step, npm dependencies, checkout secrets, cookies or analytics scripts.
Serve this directory directly. Application source code is not included or licensed by this site.

## Free hosting: Cloudflare Pages (recommended)
1. Create a Cloudflare account. Workers & Pages → Create → Pages → Connect to Git.
2. Authorize only `OfficialAshish/SortOut`; select `main`.
3. Root directory: `website`. Framework: None. Build command: leave empty.
   Build output directory: `.`. No environment variables or secrets required.
4. Deploy to the supplied `*.pages.dev` address; no paid domain required.
5. Check mobile layout, project links, contact address and download status.

If using direct upload, upload the contents of this directory as the site root.
A free plan is subject to provider limits/policies; no perpetual availability guarantee.
GitHub stores the source; do **not** use GitHub Pages for this commercial-primary site:
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

## Release enablement
Download actions intentionally stay disabled until a Windows candidate has passed
package checks and a matching public release with hashes and Qt source archive exists.
Then replace disabled buttons with links to that specific, immutable release's
installer and portable ZIP and update the validation copy. Do not link old PyQt builds.

## Paid sales gate
Checkout is not connected. Start with one approved Lemon Squeezy merchant account,
verified payout route and actual seller/contact details. Do not publish invented
checkout URLs. Provider licence keys do not currently work with the app's legacy
machine-bound validator. A tested activation adapter is still required before sales.
Never put merchant API credentials, signing secrets or mail credentials in HTML/JS.
Use hosted checkout and signed/verified server-side webhooks if adding fulfilment.
No tracking or payment form is included here. Hosting request logs remain the
hosting provider's responsibility and must be reflected in final privacy disclosures.
