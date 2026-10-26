# Observatory / maintenance

## Design system

Obsidian #090D16, graphite #151D2B, cyan #33E6F5, violet #9575FF,
gold #D9B36C, white #F2F6FC. Native README text follows GitHub's theme.
Artwork uses Segoe UI/Arial and Consolas/monospace system fallbacks.
The geometry is an original orthographic instrument, not a product screenshot.
Its cube, inner diamond, orbital planes and reference nodes connect computation
and incentive systems. Project diagrams illustrate branching, finite checking
and counterexample search. They do not represent measured outcomes.

## Asset sources and regeneration

All six SVGs are original code-authored artwork in scripts/generate_assets.py.
No stock artwork, AI raster image, remote font, JavaScript, foreignObject,
iframe or external SVG resource is required. Python 3.11+ standard library:

```text
python scripts/generate_assets.py
python scripts/validate_profile.py
```

The deterministic seed controls decorative stars only. Edit text, palette or
projection in the generator; never hand-edit output and expect regeneration to
preserve it. Desktop and <=600px hero variants use picture/source with an img
fallback. Every graphic has a title, description and README alt text.
The visuals are deliberately static: no essential animation, flashes, video,
motion preference dependency or GIF payload. The static image is the full design.
The vector paths stay crisp at high density. The body preserves identity,
project scope and links if graphics fail. At narrow widths, the body remains the
authoritative readable content; diagram annotations are decorative.

To replace an image, retain a relative repository path, descriptive alt text,
intrinsic viewBox and the 1200px maximum display width. Keep all first-party
artwork under 2 MB total. A self-contained dark panel works in both GitHub themes.

## Update project descriptions

Check each public default-branch README and linked trust/limitations document.
Keep maturity and finite/synthetic boundaries next to claims. Never infer peer
review, deployment, external validation or open-source rights from visibility.
Current focus describes public work, not undisclosed release plans.
The economics-of-forgetting working paper replaces an extra policy-simulator
slot to keep this atlas focused on four complementary questions. Economic War
Room was inspected but its owner-private deployment is not used as a public CTA.
The README contains only the GitHub and LinkedIn contact destinations supplied
by the owner. No private email is added.

## Live signals

1. Hits.sh's free service uses the profile key github.com/Aayush-Kadam,
   with no extraCount offset, token or paid account. It counts image requests, not
   unique visitors. GitHub's Camo cache can coalesce, delay or fail requests.
   Previews, validation and direct requests also affect the count. Existing
   provider history is unknown; this installation cannot establish lifetime
   coverage. Validation began on 26 October 2026; test requests affect the count.
   Komarev returned SVG directly but failed in GitHub Camo during visual QA,
   so it was replaced rather than reporting a direct response as render success.
2. Shields' GitHub stars endpoint reports the GhostFrame public repository's
   star count, subject to provider caching. Clicking opens the source repository.
3. GitHub's native workflow badge reports ci.yml on main, not a reviewer branch
   or this profile PR. It is a cached latest-status signal, not a test total or
   reliability guarantee. Clicking opens that workflow filtered to main.

These are external services. If an image fails, its meaningful alt text and
source link survive; no stale number or invented success is substituted.
No workflow, access token, analytics script, tracking pixel beyond the disclosed
view badge, paid service or external website was introduced. GitHub proxies
README image requests; direct provider visits have ordinary provider privacy
implications. Provider source and cache explanation:
https://github.com/silentsoft/hits
https://shields.io/badges/git-hub-repo-stars
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls

## Evidence and review

See docs/SOURCES.md for public repository sources and the audit date.
The feature branch is reviewable; merging changes the live profile and remains
an owner decision. No account settings or pinned repositories are changed.
