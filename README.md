# Vladimir Latypov / Владимир Латыпов

Personal research, engineering and teaching website.

- English: https://donrumata03.github.io/
- Russian: https://donrumata03.github.io/ru/

## Edit and preview

This first version deliberately has no JavaScript framework, package dependencies, analytics or tracking. The published site is ordinary static HTML/CSS with a small optional theme switcher. All content and links are usable without JavaScript.

1. Edit `content.json` for publications, experience, teaching, interests and profile links. Bilingual text arrays are ordered `[English, Russian]`.
2. Introductory/UI text and layout live in `scripts/build.py`; design tokens and responsive rules in `assets/style.css`.
3. Run `python3 scripts/build.py` and `python3 scripts/check.py`.
4. Preview with `python3 -m http.server 8000` and open http://localhost:8000/.
5. Commit both sources and generated `index.html`, `ru/index.html`, `sitemap.xml`.

Python 3.10+ is needed only for editing/building, not for hosting. GitHub Pages can publish `master` from the repository root; `.nojekyll` disables unnecessary Jekyll processing.

## Content and design

The original two-page CV is in `assets/vladimir-latypov-cv.pdf`. Its SHA256 is `5b262974b89a5f2b39d031314cd2c8242c3123e8cc52d3e03690e7673ffd3205`. It is intentionally published unchanged, including the owner's email and phone number. Update the expected hash in the checker when deliberately replacing the CV.

Research and career content are based on the supplied CV and verified sources for the two SMILES projects. SMILES 2025 links to a public proceedings PDF; SMILES 2026 FlowDraft links to Skoltech's award announcement, not to a public paper. Personal interests, the book and teaching links were provided or explicitly approved by the owner. Unpublished research details, private notes and other people's contact information are not included. The VPN Lab entry points to a currently private GitHub repository; a public release must remove credentials and sensitive configuration from the working tree AND commit history.

Palette and system-font choices are inspired by Kirill Neklyudov's site, https://necludov.github.io/. The layout and implementation are original. No font files are distributed. The portrait is the owner's GitHub profile image; if the external service is temporarily unavailable a monogram is displayed.

## Search readiness

The site includes visible English/Russian names, unique titles/descriptions, canonical URLs, reciprocal `hreflang`, Person/ProfilePage JSON-LD, `robots.txt`, `sitemap.xml` and social-sharing metadata. These are technical preparations, not a guarantee of indexing or ranking.

Still requiring owner-specific information/actions:
- Verify ownership in Google Search Console and Yandex Webmaster and submit the sitemap.
- Add the site URL to existing professional profiles.
- The supplied LinkedIn and AmDm URLs are now included. Telegram is the primary contact, while email and phone remain published by the owner's choice.
- If moving to a custom domain, change `BASE` in the generator and the sitemap location in `robots.txt`, then rebuild and set up the domain in GitHub Pages.

## Checks

`scripts/check.py` validates generated languages, anchors, local links, structured data, contact links, sitemap parsing and original PDF integrity. Responsive rendering was checked in Chromium at widths 320, 390, 768 and 1440 pixels for both languages, with no horizontal overflow or JavaScript errors. Offline rendering used the portrait fallback; it does not verify external link availability.
