# SortOut static website

No backend, build step, npm dependencies, checkout secrets, cookies or analytics scripts.
Serve this directory directly. Application source code is not included or licensed by this site.

## Free hosting: Cloudflare Pages (recommended)
1. Sign in to the existing Cloudflare account. Workers & Pages → Create application
   → Pages → Connect to Git / Import an existing Git repository. Choose **Pages**,
   not a Worker template.
2. Authorize only `OfficialAshish/SortOut`; select `main`.
3. Root directory: `website`. Framework: None. Build command: leave empty.
   Build output directory: `.`. No environment variables or secrets required.
4. Deploy to the supplied `*.pages.dev` address; no paid domain required.
5. Check mobile layout, project links, contact address and download status.
6. Send the resulting public `https://<project>.pages.dev` URL so app/site references
   can be updated without inventing an address. Subsequent pushes to main deploy
   the website automatically. No Cloudflare token is needed in the repository.

The installer and portable ZIP stay on GitHub Releases. Do not upload them into
the Pages directory; the website links to the versioned GitHub downloads. Updating
a site link does not modify an installed app: install each new reviewed release
over the existing app after closing it. App settings and Undo records are retained.

Official setup reference: https://developers.cloudflare.com/pages/get-started/git-integration/

If using direct upload, upload the contents of this directory as the site root.
A free plan is subject to provider limits/policies; no perpetual availability guarantee.
GitHub stores the source; do **not** use GitHub Pages for this commercial-primary site:
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

## Release enablement
Download actions link to the immutable [v2.3.2-qt6-preview](https://github.com/OfficialAshish/SortOut/releases/tag/v2.3.2-qt6-preview) Free preview.
Windows tests and package checks passed; hashes, notices and corresponding Qt
source archive are on the same release. New releases must pass the same gates
before links change. Do not point to an unverified latest-build URL or old PyQt binaries.

## Paid sales gate
Checkout is not connected. Start with one approved Lemon Squeezy merchant account,
verified payout route and actual seller/contact details. Do not publish invented
checkout URLs. Provider licence keys do not currently work with the app's legacy
machine-bound validator. A tested activation adapter is still required before sales.
Never put merchant API credentials, signing secrets or mail credentials in HTML/JS.
Use hosted checkout and signed/verified server-side webhooks if adding fulfilment.
No tracking or payment form is included here. Hosting request logs remain the
hosting provider's responsibility and must be reflected in final privacy disclosures.
