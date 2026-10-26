// The pinned Three.js r150 browser build is loaded before this module.
declare const THREE: any;
import './style.css';

type Project = { id: string; index: string; title: string; description: string; url: string; color: number; angle: number };
const projects: Project[] = [
  { id: 'ghostframe', index: '01 / AGENT SYSTEMS', title: 'GhostFrame', description: 'Branch a supported deterministic agent execution at one observation and compare the continuation.', url: 'https://github.com/Aayush-Kadam/ghostframe', color: 0x93e4f0, angle: -1.55 },
  { id: 'epv', index: '02 / FORMAL ASSURANCE', title: 'Economic Protocol Verifier', description: 'Bounded economic protocol checks with explicit assurance levels and replayable witnesses.', url: 'https://github.com/Aayush-Kadam/economic-protocol-verifier', color: 0xc4b7f2, angle: -.20 },
  { id: 'fuzzer', index: '03 / ADVERSARIAL TESTING', title: 'Incentive Fuzzer', description: 'Search finite economic rules for feasible counterexamples and regression-test a proposed repair.', url: 'https://github.com/Aayush-Kadam/incentive-fuzzer', color: 0xd9b879, angle: 1.2 },
];

const canvas = document.querySelector<HTMLCanvasElement>('#observatory')!;
const sceneShell = document.querySelector<HTMLElement>('.scene-shell')!;
const fallback = document.querySelector<HTMLElement>('#scene-fallback')!;
const stateLabel = document.querySelector<HTMLElement>('#scene-state')!;
const progressFill = document.querySelector<HTMLElement>('#progress-fill')!;
const nodeCard = document.querySelector<HTMLElement>('#node-card')!;
const nodeIndex = document.querySelector<HTMLElement>('#node-index')!;
const nodeTitle = document.querySelector<HTMLElement>('#node-title')!;
const nodeDescription = document.querySelector<HTMLElement>('#node-description')!;
const nodeLink = document.querySelector<HTMLAnchorElement>('#node-link')!;
const chapters = ['IDENTITY', 'ENGINEERING', 'RESEARCH', 'CAPABILITIES', 'CONTACT'];
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const qaReducedMotion = new URLSearchParams(location.search).has('reducedMotion');
const shouldReduceMotion = () => reducedMotion.matches || qaReducedMotion;
let activeChapter = 0;
let scrollFraction = 0;

function setChapterUI() {
  const maxScroll = Math.max(1, document.documentElement.scrollHeight - innerHeight);
  scrollFraction = Math.min(1, Math.max(0, scrollY / maxScroll));
  progressFill.style.width = `${(scrollFraction * 100).toFixed(2)}%`;
  const center = innerHeight * .5;
  let closest = Number.POSITIVE_INFINITY;
  document.querySelectorAll<HTMLElement>('.chapter').forEach((section, index) => {
    const rect = section.getBoundingClientRect();
    const distance = Math.abs((rect.top + rect.bottom) * .5 - center);
    if (distance < closest) { closest = distance; activeChapter = index; }
  });
  document.querySelectorAll<HTMLElement>('[data-nav]').forEach((link, index) => {
    link.classList.toggle('active', index === activeChapter);
    if (index === activeChapter) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  stateLabel.textContent = `${String(activeChapter + 1).padStart(2, '0')} / ${chapters[activeChapter]} · SCROLL ${Math.round(scrollFraction * 100)}%`;
  canvas.dataset.chapter = chapters[activeChapter].toLowerCase();
  canvas.dataset.progress = scrollFraction.toFixed(3);
}
addEventListener('scroll', setChapterUI, { passive: true });
addEventListener('resize', setChapterUI, { passive: true });
setChapterUI();

function showProject(project: Project) {
  nodeIndex.textContent = project.index;
  nodeTitle.textContent = project.title;
  nodeDescription.textContent = project.description;
  nodeLink.href = project.url;
  nodeCard.hidden = false;
  document.querySelectorAll<HTMLElement>('[data-project]').forEach(card => card.classList.toggle('is-highlighted', card.dataset.project === project.id));
}
function closeProject() {
  nodeCard.hidden = true;
  document.querySelectorAll<HTMLElement>('[data-project]').forEach(card => card.classList.remove('is-highlighted'));
}
document.querySelector<HTMLButtonElement>('#node-close')!.addEventListener('click', closeProject);
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeProject(); });

function showFallback(reason: string) {
  canvas.hidden = true;
  fallback.hidden = false;
  sceneShell.dataset.mode = 'fallback';
  stateLabel.textContent = `STATIC VIEW · ${reason}`;
}

const forcedFallback = new URLSearchParams(location.search).has('forceFallback');
const gl = !forcedFallback && (canvas.getContext('webgl2', { antialias: true, alpha: true }) || canvas.getContext('webgl', { antialias: true, alpha: true }));
if (!gl) showFallback(forcedFallback ? 'PREVIEW MODE' : 'WEBGL UNAVAILABLE');
else {
  try { startScene(); }
  catch (error) { console.error('Observatory 3D initialization failed:', error); showFallback('3D UNAVAILABLE'); }
}

function startScene() {
  if (new URLSearchParams(location.search).has('forceInitFailure')) throw new Error('QA: forced 3D initialization failure');
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(34, 1, .1, 100);
  camera.position.set(0, .12, 11.3);
  const renderer = new THREE.WebGLRenderer({ canvas, context: gl as WebGLRenderingContext, antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setClearColor(0x080b12, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.55;

  const rig = new THREE.Group();
  scene.add(rig);
  const chassis = new THREE.Group();
  rig.add(chassis);
  const gold = new THREE.MeshStandardMaterial({ color: 0xb89a67, metalness: .9, roughness: .24 });
  const silver = new THREE.MeshStandardMaterial({ color: 0x9cc2ce, metalness: .83, roughness: .22, emissive: 0x143c4d, emissiveIntensity: .65 });
  const deep = new THREE.MeshStandardMaterial({ color: 0x102335, metalness: .72, roughness: .2, transparent: true, opacity: .78, side: THREE.DoubleSide, flatShading: true });
  const coreMat = new THREE.MeshStandardMaterial({ color: 0xa9e5ef, metalness: .35, roughness: .18, emissive: 0x276f88, emissiveIntensity: 1.15, flatShading: true });
  const frameMesh = new THREE.Mesh(new THREE.IcosahedronGeometry(2.03, 0), deep);
  chassis.add(frameMesh);
  const frameEdges = new THREE.LineSegments(new THREE.EdgesGeometry(frameMesh.geometry), new THREE.LineBasicMaterial({ color: 0x77bdce, transparent: true, opacity: .66 }));
  chassis.add(frameEdges);
  const innerShell = new THREE.Mesh(new THREE.IcosahedronGeometry(1.46, 1), new THREE.MeshStandardMaterial({ color: 0x1d3f52, metalness: .7, roughness: .24, transparent: true, opacity: .32, side: THREE.DoubleSide, flatShading: true }));
  chassis.add(innerShell);
  const innerEdges = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.OctahedronGeometry(1.35, 0)), new THREE.LineBasicMaterial({ color: 0x629cab, transparent: true, opacity: .7 }));
  chassis.add(innerEdges);
  const core = new THREE.Mesh(new THREE.IcosahedronGeometry(.65, 0), coreMat);
  chassis.add(core);
  const coreWire = new THREE.LineSegments(new THREE.EdgesGeometry(core.geometry), new THREE.LineBasicMaterial({ color: 0xe5fbfb, transparent: true, opacity: .86 }));
  chassis.add(coreWire);
  const coreHalo = new THREE.Mesh(new THREE.SphereGeometry(.95, 20, 16), new THREE.MeshBasicMaterial({ color: 0x44879a, transparent: true, opacity: .055, depthWrite: false }));
  chassis.add(coreHalo);

  const ringGroup = new THREE.Group();
  rig.add(ringGroup);
  const rings: any[] = [];
  const tickSilver = new THREE.MeshBasicMaterial({ color: 0xa5c9d1 });
  const tickGold = new THREE.MeshBasicMaterial({ color: 0xcab17b });
  const ringSpecs = [
    { radius: 2.56, tube: .018, x: .34, y: .28, z: -.37, material: silver },
    { radius: 2.85, tube: .025, x: 1.18, y: -.16, z: .4, material: gold },
    { radius: 3.12, tube: .013, x: -.48, y: 1.06, z: .27, material: silver },
  ];
  ringSpecs.forEach((spec, i) => {
    const ring = new THREE.Group();
    ring.rotation.set(spec.x, spec.y, spec.z);
    ring.add(new THREE.Mesh(new THREE.TorusGeometry(spec.radius, spec.tube, 8, 160), spec.material));
    const silverMarks = new THREE.InstancedMesh(new THREE.BoxGeometry(.028, .048, .018), tickSilver, 36);
    const goldMarks = new THREE.InstancedMesh(new THREE.BoxGeometry(.055, .11, .018), tickGold, 12);
    const marker = new THREE.Object3D();
    let si = 0, gi = 0;
    for (let k = 0; k < 48; k++) {
      const a = k / 48 * Math.PI * 2;
      marker.position.set(Math.cos(a) * spec.radius, Math.sin(a) * spec.radius, 0);
      marker.rotation.z = a - Math.PI / 2;
      marker.updateMatrix();
      if (k % 4 === 0) goldMarks.setMatrixAt(gi++, marker.matrix);
      else silverMarks.setMatrixAt(si++, marker.matrix);
    }
    silverMarks.instanceMatrix.needsUpdate = true;
    goldMarks.instanceMatrix.needsUpdate = true;
    ring.add(silverMarks, goldMarks);
    ringGroup.add(ring);
    rings.push(ring);
    if (i === 1) ring.rotation.z += .16;
  });

  const trajectories = new THREE.Group();
  rig.add(trajectories);
  for (let i = 0; i < 5; i++) {
    const points: any[] = [];
    for (let k = 0; k <= 110; k++) {
      const t = k / 110 * Math.PI * 2;
      const r = 3.32 + .12 * Math.sin(t * 3 + i);
      points.push(new THREE.Vector3(r * Math.cos(t), 1.15 * Math.sin(t * 2 + i * .8), r * .36 * Math.sin(t + i * 1.25)));
    }
    const curve = new THREE.CatmullRomCurve3(points);
    const geometry = new THREE.BufferGeometry().setFromPoints(curve.getPoints(190));
    const line = new THREE.Line(geometry, new THREE.LineBasicMaterial({ color: i % 2 ? 0xa17fc8 : 0x5da5b9, transparent: true, opacity: .17 }));
    line.rotation.y = i * 1.15;
    trajectories.add(line);
  }

  const nodeMeshes: any[] = [];
  const nodeOrbits = new THREE.Group();
  rig.add(nodeOrbits);
  projects.forEach((project, index) => {
    const a = project.angle;
    const radius = 2.66 + index * .15;
    const node = new THREE.Mesh(new THREE.IcosahedronGeometry(.20, 1), new THREE.MeshBasicMaterial({ color: project.color }));
    node.position.set(Math.cos(a) * radius, Math.sin(a) * radius * .62, .95 + index * .14);
    node.userData.project = project;
    nodeOrbits.add(node);
    nodeMeshes.push(node);
    const halo = new THREE.Mesh(new THREE.SphereGeometry(.23, 12, 10), new THREE.MeshBasicMaterial({ color: project.color, transparent: true, opacity: .12, depthWrite: false }));
    halo.position.copy(node.position);
    nodeOrbits.add(halo);
    const line = new THREE.Line(new THREE.BufferGeometry().setFromPoints([node.position, new THREE.Vector3(0, 0, 0)]), new THREE.LineBasicMaterial({ color: project.color, transparent: true, opacity: .25 }));
    nodeOrbits.add(line);
  });

  const dustGeometry = new THREE.BufferGeometry();
  const dustPositions = new Float32Array(240 * 3);
  for (let i = 0; i < 240; i++) {
    const a = i * 2.399963229728653;
    const r = 3.6 + Math.sqrt(i / 240) * 3.3;
    dustPositions[i * 3] = Math.cos(a) * r;
    dustPositions[i * 3 + 1] = Math.sin(a) * r * .72;
    dustPositions[i * 3 + 2] = -3.2 + ((i * 67) % 41) / 41 * 4;
  }
  dustGeometry.setAttribute('position', new THREE.BufferAttribute(dustPositions, 3));
  const dust = new THREE.Points(dustGeometry, new THREE.PointsMaterial({ color: 0x93b5c7, size: .018, transparent: true, opacity: .4, sizeAttenuation: true }));
  scene.add(dust);
  scene.add(new THREE.AmbientLight(0x8dbed3, 1.15));
  const cyanLight = new THREE.PointLight(0x7ecddd, 25, 18, 2);
  cyanLight.position.set(-3, 2.8, 4);
  scene.add(cyanLight);
  const goldLight = new THREE.PointLight(0xe9b976, 21, 17, 2);
  goldLight.position.set(3, -2, 2);
  scene.add(goldLight);
  const violetLight = new THREE.PointLight(0x8270bb, 17, 15, 2);
  violetLight.position.set(2.6, 1, -3);
  scene.add(violetLight);

  let targetPointerX = 0, targetPointerY = 0, pointerX = 0, pointerY = 0;
  let dragX = 0, dragY = 0, dragging = false, dragMoved = false, startX = 0, startY = 0;
  document.querySelector<HTMLButtonElement>('#rotate-left')!.addEventListener('click', () => { dragX = THREE.MathUtils.clamp(dragX - .34, -1.1, 1.1); canvas.dataset.control = 'left'; });
  document.querySelector<HTMLButtonElement>('#rotate-right')!.addEventListener('click', () => { dragX = THREE.MathUtils.clamp(dragX + .34, -1.1, 1.1); canvas.dataset.control = 'right'; });
  let hovered: any = null;
  let frame = 0, sampleDuration = 0, slowFrames = 0, lastTime = performance.now(), raf = 0, disposed = false;
  let quality = matchMedia('(max-width: 800px)').matches ? Math.min(devicePixelRatio, 1.35) : Math.min(devicePixelRatio, 1.8);
  if (new URLSearchParams(location.search).has('lowQuality')) quality = 1;
  const raycaster = new THREE.Raycaster();
  const qaGeometry = new URLSearchParams(location.search).has('qa');
  const pointer = new THREE.Vector2();
  const clock = new THREE.Clock();
  const keyframes = [
    { z: 11.3, x: 0, y: .1, scale: 1, spread: 0, twist: 0, color: 0x7ecddd },
    { z: 9.8, x: -.25, y: .25, scale: 1.12, spread: .55, twist: .42, color: 0x7ecddd },
    { z: 10.8, x: .35, y: -.18, scale: 1.02, spread: 1.12, twist: 1.12, color: 0xb69adf },
    { z: 10.2, x: -.25, y: .08, scale: .92, spread: 1.64, twist: 1.75, color: 0xd6b77b },
    { z: 12.4, x: 0, y: .12, scale: .8, spread: .25, twist: 2.2, color: 0x9dcad6 },
  ];
  function timeline() {
    // Section centers, rather than document percentages, anchor the reversible scene state.
    const centers = Array.from(document.querySelectorAll<HTMLElement>('.chapter'), element => element.offsetTop + element.offsetHeight * .5);
    const position = scrollY + innerHeight * .5;
    let segment = 0;
    while (segment < centers.length - 2 && position > centers[segment + 1]) segment++;
    const t = THREE.MathUtils.clamp((position - centers[segment]) / Math.max(1, centers[segment + 1] - centers[segment]), 0, 1);
    return { a: keyframes[segment], b: keyframes[segment + 1], t: t * t * (3 - 2 * t) };
  }
  function resize() {
    const rect = sceneShell.getBoundingClientRect();
    const width = Math.max(1, rect.width), height = Math.max(1, rect.height);
    renderer.setPixelRatio(quality);
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.fov = width < height ? 39 : 34;
    camera.updateProjectionMatrix();
    canvas.dataset.dpr = quality.toFixed(2);
  }
  resize();
  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(sceneShell);
  function updatePointer(event: PointerEvent) {
    const rect = canvas.getBoundingClientRect();
    targetPointerX = THREE.MathUtils.clamp(((event.clientX - rect.left) / rect.width - .5) * 2, -1, 1);
    targetPointerY = THREE.MathUtils.clamp(((event.clientY - rect.top) / rect.height - .5) * 2, -1, 1);
    pointer.set(targetPointerX, -targetPointerY);
    raycaster.setFromCamera(pointer, camera);
    const hit = raycaster.intersectObjects(nodeMeshes, false)[0];
    hovered = hit?.object || null;
    canvas.dataset.hovered = hovered ? (hovered.userData.project as Project).id : '';
    canvas.style.cursor = hovered ? 'pointer' : dragging ? 'grabbing' : 'grab';
    if (hovered) {
      const project = hovered.userData.project as Project;
      document.querySelectorAll<HTMLElement>('[data-project]').forEach(card => card.classList.toggle('is-highlighted', card.dataset.project === project.id));
    } else if (nodeCard.hidden) {
      document.querySelectorAll<HTMLElement>('[data-project]').forEach(card => card.classList.remove('is-highlighted'));
    }
    if (dragging) {
      const dx = event.clientX - startX, dy = event.clientY - startY;
      if (Math.abs(dx) + Math.abs(dy) > 6) dragMoved = true;
      dragX = THREE.MathUtils.clamp(dragX + dx * .003, -1.1, 1.1);
      dragY += dy * .003;
      dragY = THREE.MathUtils.clamp(dragY, -.55, .55);
      startX = event.clientX; startY = event.clientY;
    }
  }
  canvas.addEventListener('pointermove', updatePointer);
  canvas.addEventListener('pointerdown', event => { dragging = true; dragMoved = false; startX = event.clientX; startY = event.clientY; canvas.setPointerCapture(event.pointerId); updatePointer(event); });
  canvas.addEventListener('pointerup', event => { dragging = false; if (!dragMoved && hovered) showProject(hovered.userData.project as Project); if (canvas.hasPointerCapture(event.pointerId)) canvas.releasePointerCapture(event.pointerId); });
  canvas.addEventListener('pointercancel', () => { dragging = false; });
  canvas.addEventListener('pointerleave', () => { targetPointerX = 0; targetPointerY = 0; if (!dragging) hovered = null; });
  canvas.addEventListener('webglcontextlost', event => { event.preventDefault(); stop(); showFallback('WEBGL CONTEXT LOST'); });

  function render(now: number) {
    if (disposed) return;
    raf = requestAnimationFrame(render);
    const rawDt = Math.max(.001, (now - lastTime) / 1000);
    const dt = Math.min(.05, rawDt);
    lastTime = now;
    const damp = (rate: number) => shouldReduceMotion() ? 1 : 1 - Math.exp(-rate * dt);
    pointerX = THREE.MathUtils.lerp(pointerX, targetPointerX, damp(5));
    pointerY = THREE.MathUtils.lerp(pointerY, targetPointerY, damp(5));
    const { a, b, t } = timeline();
    const mix = (key: 'z' | 'x' | 'y' | 'scale' | 'spread' | 'twist') => THREE.MathUtils.lerp(a[key], b[key], t);
    camera.position.z = THREE.MathUtils.lerp(camera.position.z, mix('z'), damp(2.8));
    camera.position.x = THREE.MathUtils.lerp(camera.position.x, mix('x') + pointerX * .22, damp(3.8));
    camera.position.y = THREE.MathUtils.lerp(camera.position.y, mix('y') - pointerY * .15, damp(3.8));
    camera.lookAt(0, 0, 0);
    const desiredY = mix('twist') + pointerX * .27 + dragX;
    const desiredX = -.16 - pointerY * .18 + dragY;
    rig.rotation.y = THREE.MathUtils.lerp(rig.rotation.y, desiredY, damp(4.8));
    rig.rotation.x = THREE.MathUtils.lerp(rig.rotation.x, desiredX, damp(4.8));
    rig.scale.setScalar(THREE.MathUtils.lerp(rig.scale.x, mix('scale'), damp(3)));
    const spread = mix('spread');
    rings.forEach((ring, i) => {
      ring.position.z = THREE.MathUtils.lerp(ring.position.z, (i - 1) * spread * .68, damp(3.1));
      ring.rotation.y = THREE.MathUtils.lerp(ring.rotation.y, ringSpecs[i].y + spread * (i - 1) * .32, damp(3.1));
    });
    chassis.position.z = THREE.MathUtils.lerp(chassis.position.z, spread * .38, damp(3));
    trajectories.scale.setScalar(1 + spread * .16);
    trajectories.rotation.y = spread * .42;
    nodeOrbits.scale.setScalar(1 + spread * .13);
    cyanLight.color.lerpColors(new THREE.Color(a.color), new THREE.Color(b.color), t);
    cyanLight.position.x = -3 + pointerX * 1.5;
    cyanLight.position.y = 2.8 - pointerY;
    if (!shouldReduceMotion()) {
      const elapsed = clock.getElapsedTime();
      core.rotation.y = elapsed * .12;
      coreWire.rotation.copy(core.rotation);
      ringGroup.rotation.z = Math.sin(elapsed * .13) * .025;
    }
    renderer.render(scene, camera);
    if (qaGeometry) {
      const rect = canvas.getBoundingClientRect();
      canvas.dataset.nodePoints = nodeMeshes.map(node => {
        const p = node.getWorldPosition(new THREE.Vector3()).project(camera);
        return `${(node.userData.project as Project).id}:${Math.round(rect.left + (p.x + 1) * rect.width / 2)},${Math.round(rect.top + (1 - p.y) * rect.height / 2)}`;
      }).join(';');
    }
    canvas.dataset.yaw = rig.rotation.y.toFixed(3);
    canvas.dataset.pitch = rig.rotation.x.toFixed(3);
    canvas.dataset.cameraZ = camera.position.z.toFixed(3);
    canvas.dataset.spread = spread.toFixed(3);
    canvas.dataset.motion = shouldReduceMotion() ? 'reduced' : 'full';
    frame++;
    sampleDuration += rawDt;
    if (frame >= 30) {
      const fps = frame / sampleDuration;
      canvas.dataset.fpsAverage = fps.toFixed(1);
      if (fps < 32) slowFrames++; else slowFrames = Math.max(0, slowFrames - 1);
      if (slowFrames >= 2 && quality > 1) { quality = 1; resize(); slowFrames = 0; canvas.dataset.quality = 'adaptive-low'; }
      frame = 0; sampleDuration = 0;
    }
  }
  function stop() {
    disposed = true;
    cancelAnimationFrame(raf);
    resizeObserver.disconnect();
    scene.traverse((object: any) => {
      if (object instanceof THREE.Mesh || object instanceof THREE.Points || object instanceof THREE.Line || object instanceof THREE.LineSegments) {
        object.geometry.dispose();
        const mats = Array.isArray(object.material) ? object.material : [object.material];
        mats.forEach((material: any) => material.dispose());
      }
    });
    renderer.dispose();
  }
  addEventListener('pagehide', stop, { once: true });
  document.addEventListener('visibilitychange', () => {
    if (disposed) return;
    if (document.hidden) cancelAnimationFrame(raf);
    else { lastTime = performance.now(); raf = requestAnimationFrame(render); }
  });
  canvas.dataset.mode = 'webgl';
  canvas.dataset.quality = quality <= 1 ? 'low' : 'standard';
  raf = requestAnimationFrame(render);
}
