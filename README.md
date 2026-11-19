# bionut.az — static corporate website

A custom-built static site with no WordPress and no theme. EN is the default at the site root, AZ is under `/az/` and RU is under `/ru/`.

## Structure
- `tools/content.py`: **all copy** (EN master + AZ/RU), product specs, certificates, articles, contacts
- `tools/build.py`: generator that writes the full site into `public/` (HTML, spec PDFs, sitemap, robots, 404)
- `tools/process_images.sh`: converts `images/raw/*.jpg` into graded WebP/AVIF assets in `assets/img/`
- `tools/gen_map.py`: builds the world-map path data (`tools/data/map.json`) from world-atlas
- `assets/`: CSS, JS, brand logo (original, unmodified), optimised images

## Build & preview
```bash
python3 tools/build.py                 # regenerate public/
cd public && python3 -m http.server 8080   # open http://localhost:8080
```
To deploy, upload the contents of `public/` to the web root. Any static host works: nginx, Apache, Netlify or Cloudflare Pages.

## Still to supply
- Certificate numbers, issuing bodies, validity dates and PDF scans go in `CERTS` in `content.py`. Put the PDFs in `assets/certificates/` and set `"pdf": "file.pdf"`. Until then the pages show "Available on request" with a request button.
  Expected files (one per card): `fssc-22000.pdf`, `iso-22000-2018.pdf`, `organic.pdf`, `sedex-membership.pdf`. Once `"pdf"` is set, the home-page card and the certificate page open that PDF in a new tab. Until then each card links to its own entry on the certifications page.
- Certificate logos live in `assets/brand/certs/*.webp`. They were taken from the client's WhatsApp images, so they should be replaced with official vector or high-resolution files under the same names.
- In-shell hazelnut product photo: `p-inshell` is still cropped from a branch photo (`img03`). Add a real in-shell product shot to `images/raw/` and point the `sq ... p-inshell` line in `tools/process_images.sh` at it.
- Team job titles: `ABOUT["team"]` (currently "Management").
- The logo is the 106 px PNG from the old site. An SVG or high-resolution master should replace `assets/brand/bionut-logo.png`.
- Photographer images: replace the files in `images/raw/` (same names), then run `tools/process_images.sh` and `tools/build.py`.
- The contact form currently opens the visitor's email client (mailto). To receive submissions server-side, point the form at a backend or a form service.
