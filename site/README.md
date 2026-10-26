# The Observatory — interactive build

This is the real WebGL experience shown in the profile README preview. The rendered instrument is made of three-dimensional polyhedral meshes, orbit geometry, project nodes, lighting, and trajectories. Pointer movement changes its orientation and lighting; dragging adds a bounded manual rotation; chapter position changes the camera, ring separation, scale, and scene state. These changes run in a frame-rate-independent animation loop. The page content and verified links remain usable without WebGL.

## Run and review

Use Node.js 22 or newer, then from this directory:

```sh
npm install
npm run build
npm run preview
```

Open the URL printed by Vite, normally `http://localhost:4173/Aayush-Kadam/`. The repository-subpath base is configured in `vite.config.ts`, and the production build goes to `dist/`. `?forceFallback=1` shows the no-WebGL fallback; `?forceInitFailure=1` tests the initialization-error fallback; `?lowQuality=1` forces a 1x rendering pixel ratio; `?reducedMotion=1` exercises the reduced-motion code path; `?qa=1` exposes projected node coordinates for interaction tests. These query parameters are for review, not advertised product features.

Three.js r150 is pinned as a self-contained vendor build in `public/vendor/three.min.js` because the build environment used for review could not reach the package registry. Its MIT license is included in `public/vendor/THREE-LICENSE.txt`. The site adds no analytics or backend. Fonts have system fallbacks if Google Fonts is unavailable. Future maintainers may migrate the vendor build to a current ES module after a full visual and interaction regression pass.

## Deployment gate

**No public Pages site has been deployed by this branch.** The intended repository project URL is `https://aayush-kadam.github.io/Aayush-Kadam/`, but it must not be treated as live until verified. The profile README currently links here for an honest source and local preview.

After owner approval, merge the reviewed PR, set **Settings → Pages → Build and deployment → Source → GitHub Actions**, and manually run the `Publish Observatory to GitHub Pages` workflow on `main`. The workflow is `workflow_dispatch` only, checks out read-only source, builds `site/dist`, and grants `pages: write` plus `id-token: write` only to the deployment job. It has no secret or paid-service dependency. Verify the returned Pages URL, all assets under `/Aayush-Kadam/`, chapter links, and the WebGL fallback. Only then replace the README preview link with the verified live URL in a follow-up reviewed change.

Deployment configuration follows [Vite's nested-base guidance](https://vite.dev/guide/static-deploy#github-pages) and [GitHub's custom Pages workflow requirements](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
