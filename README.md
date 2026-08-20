<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>README Preview — KAIZER-2002</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #010409; display: flex; justify-content: center; padding: 32px 16px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }

  .readme {
    width: 860px;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    overflow: hidden;
    color: #e6edf3;
  }

  .readme-header {
    background: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 10px 16px;
    font-size: 13px;
    color: #8b949e;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .readme-header span { color: #e6edf3; font-weight: 600; }

  .content { padding: 0 32px 0; }

  /* ─── HERO ─── */
  .hero {
    width: calc(100% + 64px);
    margin: 0 -32px;
    display: block;
    line-height: 0;
  }
  .hero img { width: 100%; display: block; }

  /* ─── FOOTER BANNER ─── */
  .footer-banner {
    width: calc(100% + 64px);
    margin: 0 -32px;
    display: block;
    line-height: 0;
  }
  .footer-banner img { width: 100%; display: block; }

  /* ─── NAME / INTRO ─── */
  .intro { text-align: center; padding: 28px 0 18px; }

  /* Glitch + shimmer name animation */
  .name-glitch {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -0.5px;
    position: relative;
    display: inline-block;
    background: linear-gradient(90deg, #e6edf3 0%, #7c3aed 30%, #58a6ff 55%, #3fb950 80%, #e6edf3 100%);
    background-size: 250% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: nameShimmer 4s linear infinite;
  }

  @keyframes nameShimmer {
    0%   { background-position: 0% center; }
    100% { background-position: 250% center; }
  }

  /* Wave letters */
  .wave-name { display: inline-flex; gap: 0; }
  .wave-name span {
    display: inline-block;
    animation: waveLetter 1.8s ease-in-out infinite;
    font-size: 32px;
    font-weight: 800;
    background: linear-gradient(135deg, #e6edf3, #7c3aed, #58a6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .wave-name span:nth-child(1)  { animation-delay: 0.00s; }
  .wave-name span:nth-child(2)  { animation-delay: 0.06s; }
  .wave-name span:nth-child(3)  { animation-delay: 0.12s; }
  .wave-name span:nth-child(4)  { animation-delay: 0.18s; }
  .wave-name span:nth-child(5)  { animation-delay: 0.24s; }
  .wave-name span:nth-child(6)  { animation-delay: 0.30s; }
  .wave-name span:nth-child(7)  { animation-delay: 0.36s; }
  .wave-name span:nth-child(8)  { animation-delay: 0.42s; }
  .wave-name span:nth-child(9)  { animation-delay: 0.48s; }
  .wave-name span:nth-child(10) { animation-delay: 0.54s; }
  .wave-name span:nth-child(11) { animation-delay: 0.60s; }
  .wave-name span:nth-child(12) { animation-delay: 0.66s; }
  .wave-name span:nth-child(13) { animation-delay: 0.72s; }
  .wave-name span:nth-child(14) { animation-delay: 0.78s; }
  .wave-name span:nth-child(15) { animation-delay: 0.84s; }
  .wave-name span:nth-child(16) { animation-delay: 0.90s; }
  .wave-name span:nth-child(17) { animation-delay: 0.96s; }
  .wave-name span:nth-child(18) { animation-delay: 1.02s; }
  .wave-name span:nth-child(19) { animation-delay: 1.08s; }
  .wave-name span:nth-child(20) { animation-delay: 1.14s; }

  @keyframes waveLetter {
    0%, 60%, 100% { transform: translateY(0); }
    30%            { transform: translateY(-8px); }
  }

  .intro .role {
    font-size: 13px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7c3aed;
    font-weight: 600;
    margin: 10px 0 8px;
  }

  /* ─── TAGLINE WORD REVEAL ─── */
  .tagline-animated {
    font-size: 14px;
    color: #8b949e;
    margin-bottom: 16px;
    line-height: 1.7;
  }
  .tagline-animated .w {
    display: inline-block;
    opacity: 0;
    transform: translateY(10px);
    animation: wordReveal 0.45s cubic-bezier(0.22,1,0.36,1) forwards;
  }
  .tagline-animated .w.accent {
    color: #a78bfa;
    font-weight: 600;
    position: relative;
    animation: wordRevealAccent 0.45s cubic-bezier(0.22,1,0.36,1) forwards;
  }
  /* staggered delays — 11 words */
  .tagline-animated .w:nth-child(1)  { animation-delay: 0.8s; }
  .tagline-animated .w:nth-child(2)  { animation-delay: 1.0s; }
  .tagline-animated .w:nth-child(3)  { animation-delay: 1.2s; }
  .tagline-animated .w:nth-child(4)  { animation-delay: 1.4s; }
  .tagline-animated .w:nth-child(5)  { animation-delay: 1.6s; }
  .tagline-animated .w:nth-child(6)  { animation-delay: 1.8s; }
  .tagline-animated .w:nth-child(7)  { animation-delay: 2.0s; }
  .tagline-animated .w:nth-child(8)  { animation-delay: 2.2s; }
  .tagline-animated .w:nth-child(9)  { animation-delay: 2.4s; }
  .tagline-animated .w:nth-child(10) { animation-delay: 2.6s; }
  .tagline-animated .w:nth-child(11) { animation-delay: 2.8s; }
  @keyframes wordReveal {
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes wordRevealAccent {
    to { opacity: 1; transform: translateY(0); text-shadow: 0 0 12px rgba(167,139,250,0.45); }
  }
  .badges { display: flex; flex-wrap: wrap; justify-content: center; gap: 5px; }
  .badges img { height: 20px; }

  /* ─── DIVIDER ─── */
  .divider { border: none; border-top: 1px solid #30363d; margin: 22px 0; }

  /* ─── SECTION HEADER ─── */
  .section-title {
    font-size: 18px;
    font-weight: 700;
    color: #e6edf3;
    border-bottom: 1px solid #30363d;
    padding-bottom: 8px;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* ─── TECH STACK ─── */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 6px;
  }
  .tech-category {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 12px 14px;
  }
  .tech-category h4 {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #7c3aed;
    margin-bottom: 10px;
  }
  .tech-badges { display: flex; flex-wrap: wrap; gap: 4px; line-height: 1; }
  .tech-badges img { height: 22px; }

  /* ─── GETO ─── */
  .geto-row {
    display: flex;
    align-items: flex-end;
    margin-top: 6px;
  }
  .geto-col { flex: 1; }
  .geto-img { width: 200px; flex-shrink: 0; }
  .geto-img img { width: 100%; display: block; }

  /* ─── ANALYTICS + CATKITTY FRAME ─── */
  .analytics-section { position: relative; }

  /* floating catkitties around the analytics header */
  .cats-frame {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 4px;
    height: 90px;
    overflow: visible;
  }
  .cats-frame .cat { position: absolute; }
  .cats-frame .cat-tl { left: 0;   top: 0;   width: 75px; animation: floatCat 3.2s ease-in-out infinite; }
  .cats-frame .cat-tr { right: 0;  top: 0;   width: 75px; animation: floatCat 2.8s ease-in-out infinite 0.4s; transform: scaleX(-1); }
  .cats-frame .cat-bl { left: 90px; bottom: 0; width: 55px; animation: floatCat 3.6s ease-in-out infinite 0.9s; opacity: 0.85; }
  .cats-frame .cat-br { right: 90px; bottom: 0; width: 55px; animation: floatCat 3.0s ease-in-out infinite 1.4s; transform: scaleX(-1); opacity: 0.85; }

  .cats-frame .analytics-label {
    font-size: 18px;
    font-weight: 700;
    color: #e6edf3;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: none;
    margin: 0;
    padding: 0;
    z-index: 1;
  }

  @keyframes floatCat {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-9px); }
  }
  .cats-frame .cat-tr { animation: floatCatFlip 2.8s ease-in-out infinite 0.4s; }
  .cats-frame .cat-br { animation: floatCatFlip 3.0s ease-in-out infinite 1.4s; }
  @keyframes floatCatFlip {
    0%, 100% { transform: scaleX(-1) translateY(0); }
    50%       { transform: scaleX(-1) translateY(-9px); }
  }

  /* analytics underline */
  .analytics-underline {
    border-bottom: 1px solid #30363d;
    margin-bottom: 18px;
  }

  /* stats layout */
  .analytics-layout {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    margin-bottom: 12px;
  }
  .stats-col { flex: 1; display: flex; flex-direction: column; gap: 8px; }
  .stats-col img { width: 100%; display: block; border-radius: 6px; }
  .evange-col {
    width: 138px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-top: 8px;
  }
  .evange-col img { width: 130px; border-radius: 6px; }

  /* ─── 3D GRAPH ─── */
  .contrib-graph {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 8px;
    text-align: center;
  }
  .contrib-graph img { width: 100%; display: block; border-radius: 4px; }
  .contrib-placeholder {
    background: #0d1117;
    border: 1px dashed #30363d;
    border-radius: 6px;
    padding: 32px;
    color: #6e7681;
    font-size: 13px;
    font-style: italic;
  }

  /* ─── PROJECTS ─── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 12px;
  }
  .projects-row2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    max-width: calc(66.66% + 6px);
    margin-bottom: 6px;
  }
  .project-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 14px;
    transition: border-color 0.2s;
  }
  .project-card:hover { border-color: #7c3aed; }
  .project-card h3 {
    font-size: 14px;
    font-weight: 700;
    color: #58a6ff;
    margin-bottom: 6px;
  }
  .project-card p {
    font-size: 12px;
    color: #8b949e;
    line-height: 1.5;
  }

  /* ─── QUOTE ─── */
  .quote-section { text-align: center; margin-bottom: 20px; }
  .quote-section img { max-width: 100%; border-radius: 6px; }
</style>
</head>
<body>
<div class="readme">

  <div class="readme-header">
    📄 <span>README.md</span>
  </div>

  <!-- ══════════════════════════════════════════ -->
  <!-- 1. PROGRAMMER HERO — full width           -->
  <!-- ══════════════════════════════════════════ -->
  <div class="hero">
    <img
      src="./assets/Programmer1.gif"
      alt="Developer coding animation">
  </div>

  <div class="content">

    <!-- ══════════════════════════════════════════ -->
    <!-- 2. NAME / INTRO — wave letter animation   -->
    <!-- ══════════════════════════════════════════ -->
    <div class="intro">

      <!-- Wave animation: each character is a separate span -->
      <div class="wave-name" aria-label="Swapnil Nandi Utsha">
        <span>S</span><span>w</span><span>a</span><span>p</span><span>n</span><span>i</span><span>l</span>
        <span>&nbsp;</span>
        <span>N</span><span>a</span><span>n</span><span>d</span><span>i</span>
        <span>&nbsp;</span>
        <span>U</span><span>t</span><span>s</span><span>h</span><span>a</span>
      </div>

      <p class="role">Software Developer</p>
      <p class="tagline-animated">
        <span class="w">Building</span>
        <span class="w">practical,</span>
        <span class="w accent">production-ready</span>
        <span class="w">applications</span>
        <span class="w">across</span>
        <span class="w accent">mobile,</span>
        <span class="w accent">backend,</span>
        <span class="w">and</span>
        <span class="w accent">web.</span>
      </p>

      <div class="badges">
        <a href="https://discord.gg/chcotaco7189"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" alt="Discord"></a>
        <a href="https://facebook.com/utsha.swapnil"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white" alt="Facebook"></a>
        <a href="https://instagram.com/kaizer_san_"><img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=instagram&logoColor=white" alt="Instagram"></a>
        <a href="https://linkedin.com/in/swapnil-nandi-utsha"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
        <a href="https://pinterest.com/swapnilnandiutsha"><img src="https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=pinterest&logoColor=white" alt="Pinterest"></a>
        <a href="https://stackoverflow.com/users/33047687"><img src="https://img.shields.io/badge/Stackoverflow-FE7A16.svg?logo=stack-overflow&logoColor=white" alt="Stack Overflow"></a>
        <a href="https://codepen.io/Swapnil-Nandi"><img src="https://img.shields.io/badge/CodePen-000000.svg?logo=codepen&logoColor=white" alt="CodePen"></a>
        <a href="https://mastodon.social/@swapnilnandi"><img src="https://img.shields.io/badge/Mastodon-%232B90D9.svg?logo=mastodon&logoColor=white" alt="Mastodon"></a>
        <a href="mailto:swapnilnandiutsha@gmail.com"><img src="https://img.shields.io/badge/Email-D14836.svg?logo=gmail&logoColor=white" alt="Email"></a>
      </div>
    </div>

    <hr class="divider">

    <!-- ══════════════════════════════════════════ -->
    <!-- 3. TECH STACK — icon badges by category   -->
    <!-- ══════════════════════════════════════════ -->
    <div class="section-title">⌨ Tech Stack</div>

    <div class="tech-grid">
      <div class="tech-category">
        <h4>Backend</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
          <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
          <img src="https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js">
          <img src="https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white" alt="Go">
        </div>
      </div>

      <div class="tech-category">
        <h4>Frontend</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript">
          <img src="https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
          <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React">
          <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
        </div>
      </div>

      <div class="tech-category">
        <h4>Mobile</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white" alt="Dart">
          <img src="https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React Native">
        </div>
      </div>

      <div class="tech-category">
        <h4>Database</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
          <img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
          <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
          <img src="https://img.shields.io/badge/Prisma-3982CE?style=for-the-badge&logo=Prisma&logoColor=white" alt="Prisma">
        </div>
      </div>

      <div class="tech-category">
        <h4>AI / ML</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow">
          <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch">
          <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" alt="Keras">
          <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
          <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
          <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
        </div>
      </div>

      <div class="tech-category">
        <h4>DevOps &amp; Tools</h4>
        <div class="tech-badges">
          <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
          <img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle">
          <img src="https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell">
          <img src="https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white" alt="Solidity">
        </div>
      </div>
    </div>

    <!-- Geto right-anchored below tech grid -->
    <div class="geto-row">
      <div class="geto-col"></div>
      <div class="geto-img">
        <img src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/Geto.gif" alt="Geto">
      </div>
    </div>

    <hr class="divider">

    <!-- ══════════════════════════════════════════ -->
    <!-- 4. GITHUB ANALYTICS + CATKITTY FRAME     -->
    <!-- ══════════════════════════════════════════ -->
    <div class="analytics-section">

      <!-- 4 floating catkitties around the section title (like reference) -->
      <div class="cats-frame">
        <img class="cat cat-tl" src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/catkitty.gif" alt="">
        <img class="cat cat-tr" src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/catkitty.gif" alt="">
        <img class="cat cat-bl" src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/catkitty.gif" alt="">
        <img class="cat cat-br" src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/catkitty.gif" alt="">
        <div class="analytics-label"> GitHub Analytics</div>
      </div>
      <div class="analytics-underline"></div>

      <!-- Stats + Evangelion side column -->
      <div class="analytics-layout">
        <div class="stats-col">
          <img src="https://github-readme-stats.shion.dev/api?username=KAIZER-2002&theme=vision-friendly-dark&hide_border=false&include_all_commits=true&count_private=true" alt="GitHub Stats">
          <img src="https://streak-stats.demolab.com/?user=KAIZER-2002&theme=vision-friendly-dark&hide_border=false" alt="Streak Stats">
          <img src="https://github-readme-stats.shion.dev/api/top-langs/?username=KAIZER-2002&theme=vision-friendly-dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact" alt="Top Languages">
        </div>

        <div class="evange-col">
          <img src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/evangelion.gif" alt="Evangelion">
        </div>
      </div>

      <!-- 3D Contribution Graph -->
      <div class="contrib-graph">
        <div class="contrib-placeholder">
          🌐 &nbsp;<strong style="color:#3fb950;">profile-3d-contrib/profile-night-green.svg</strong><br><br>
          Generated by <code>yoshi389111/github-profile-3d-contrib@v0.9.3</code> — appears here after workflow runs
        </div>
      </div>
    </div>

    <hr class="divider">

    <!-- ══════════════════════════════════════════ -->
    <!-- 5. FEATURED PROJECTS — 5 cards (3 + 2)   -->
    <!-- ══════════════════════════════════════════ -->
    <div class="section-title"> Featured Projects</div>

    <!-- Row 1: 3 cards -->
    <div class="projects-grid">
      <div class="project-card">
        <h3> ExpenseFlow</h3>
        <p>Android first personal expense tracker built with Flutter, Drift/SQLite, Riverpod and GoRouter.</p>
      </div>
      <div class="project-card">
        <h3> JyotishAI</h3>
        <p>AI powered Vedic astrology platform with modular backend, RAG pipeline, vector search and provider agnostic AI architecture.</p>
      </div>
      <div class="project-card">
        <h3> AI Voice Receptionist</h3>
        <p>Intelligent voice based reception system using LLMs and speech pipelines to handle inbound calls and queries autonomously.</p>
      </div>
    </div>

    <!-- Row 2: 2 cards centered -->
    <div class="projects-row2">
      <div class="project-card">
        <h3> SorryNotSorry</h3>
        <p>A social platform concept built around unfiltered authentic expression no virtue signalling just honesty.</p>
      </div>
      <div class="project-card">
        <h3> KidsHub</h3>
        <p>A safe, curated digital learning space for children interactive content, parental controls and progress tracking.</p>
      </div>
    </div>

    <hr class="divider">

    <!-- ══════════════════════════════════════════ -->
    <!-- 6. QUOTE                                  -->
    <!-- ══════════════════════════════════════════ -->
    <div class="quote-section">
      <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="Random Dev Quote">
    </div>

  </div><!-- /content -->

  <!-- ══════════════════════════════════════════ -->
  <!-- 7. KOYOMI ARARAGI — full-width footer      -->
  <!-- ══════════════════════════════════════════ -->
  <div class="footer-banner">
    <img
      src="https://raw.githubusercontent.com/KAIZER-2002/KAIZER-2002/main/assets/Koyomi%20Araragi.gif"
      alt="Koyomi Araragi">
  </div>

</div><!-- /readme -->
</body>
</html>
