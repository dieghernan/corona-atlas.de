# Social cards

`social-card.html` composes the existing historical map in
`assets/img/og_corona_atlas.png` with Academia's Montserrat and Roboto fonts
and its white and blue palette. It identifies the project as a historical
archive and preserves the Diego & Rodrigo credit. The map colors represent
historical risk designations, not current travel guidance.
`social-card-en.html` provides the English composition for the GitHub banner;
the Open Graph image uses the German composition in `social-card.html`.

The saved map contains CARTO basemap imagery. Its attribution remains on the
cards, even though the interactive map now uses OpenStreetMap. The old map is
reused without making tile requests. Fonts are bundled with their OFL licenses.

To regenerate the JPEG files with Python and Playwright:

```sh
py -m pip install playwright
py -m playwright install chromium
py scripts/render_social.py
```

An existing Chromium browser can also be used without downloading another:

```powershell
py scripts/render_social.py --executable "C:/Program Files/Google/Chrome/Application/chrome.exe"
```

The outputs are `assets/img/social-preview.jpg` at 1200 × 630 and
`assets/img/github-preview.jpg` at 1280 × 640. The renderer waits for the local
fonts and map to load and uses a device scale factor of 1. Inspect both images
after changing the composition. The GitHub image is ready to upload under
Settings → General → Social preview; committing the file alone does not set it.

# Site maintenance

Use Ruby 3.4 and Bundler to install dependencies and build the site:

```sh
bundle install
bundle exec jekyll build
```

The Pages workflow builds once, deploys the Pages artifact and copies the same
artifact to `gh-pages`. Configure GitHub Pages to use GitHub Actions before
deploying this workflow. The four data and GIF workflows remain disabled in
GitHub; publishing the historical site does not require running them.

Keep translated page metadata in `_pages/index*.md` synchronized with its
source in `_R/index*.Rmd`. The disabled R pipeline still generates the old
`og_corona_atlas.png`; it does not overwrite the new sharing images.

## Contributor identity sources

Contributor names and profile links in `_data/structured_data.json` follow
About and the public profiles linked from it. Checked November 3, 2026.

- Emmanuel de Bourmont: the [LinkedIn profile](https://www.linkedin.com/in/emmanuel-de-bourmont/)
  linked from About. Other people with the same name were excluded.
- Natalia Jedlikowska: [commit b507c0b](https://github.com/dieghernan/corona-atlas.de/commit/b507c0ba42ead1e234c82728ac3f3e086d962799)
  replaces her original `natalia.jedlikowska` Instagram link with
  `hiszpanski.cafecito`, establishing continuity between those profiles.
  Her [Cafecito homepage](https://cafecito.pl/) independently states her full
  name and describes her work teaching Spanish and translating.
- Ege Korkan: his [GitHub profile](https://github.com/egekorkan) links his
  personal website, LinkedIn and ORCID 0000-0003-4910-4962. His repository
  commits also document the Turkish translation.

No verified ORCID was found for Emmanuel or Natalia. Current employers,
private contact details and unverified profile matches are not imported.
