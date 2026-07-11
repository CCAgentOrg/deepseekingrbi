#!/usr/bin/env python3
"""Build book PDF, GitHub Pages site, and push to CCAgentOrg/deepseekingrbi."""

import subprocess, os, sys

REPO_DIR = "/home/workspace/deepseekingrbi"
os.chdir(REPO_DIR)

def run(cmd, cwd=REPO_DIR, timeout=120):
    print(f"$ {cmd}")
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        print(f"STDERR: {r.stderr[:500]}")
    print(f"STDOUT: {r.stdout[:500]}")
    return r.returncode, r.stdout, r.stderr

# 1. Set up remote
print("=== Setting up remote ===")
run("git remote add origin https://github.com/CCAgentOrg/deepseekingrbi.git")

# 2. Push to GitHub
print("=== Pushing to GitHub ===")
run("git push -u origin main", timeout=60)

# 3. Try PDF build with pandoc
print("=== Building PDF ===")
run(
    'pandoc book/full-book.md -o book/deepseekingrbi.pdf '
    '--from markdown+yaml_metadata_block+footnotes+fenced_code_blocks '
    '--pdf-engine=xelatex '
    '-V mainfont="DejaVu Sans" -V sansfont="DejaVu Sans" -V monofont="DejaVu Sans Mono" '
    '--highlight-style=tango --toc --toc-depth=2 -N '
    '-V toc-own-page=true -V titlepage=true -V titlepage-color=1a1a2e '
    '-V titlepage-text-color=ffffff -V page-background=',
    timeout=180
)

# 4. Build GitHub Pages site
print("=== Building GitHub Pages ===")
# Create website dir
os.makedirs("website", exist_ok=True)

# Write index.html
index_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DeepSeeking Accountability in RBI</title>
<style>
:root { --bg: #0f0f1a; --fg: #e0dcd0; --accent: #d4a853; --card: #1a1a2e; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'DejaVu Sans', system-ui, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.7; }
.container { max-width: 800px; margin: 0 auto; padding: 2rem; }
header { text-align: center; padding: 4rem 0 2rem; }
h1 { font-size: 2.2rem; color: var(--accent); margin-bottom: 0.5rem; }
.subtitle { font-size: 1.1rem; color: #888; margin-bottom: 2rem; }
.cta { display: inline-block; background: var(--accent); color: #0f0f1a; padding: 0.8rem 2rem; border-radius: 6px; text-decoration: none; font-weight: bold; margin: 0.5rem; }
.cta:hover { opacity: 0.9; }
section { margin: 3rem 0; }
h2 { color: var(--accent); border-bottom: 1px solid #333; padding-bottom: 0.5rem; margin-bottom: 1rem; }
ul { list-style: none; }
li { padding: 0.5rem 0; border-bottom: 1px solid #1a1a2e; }
li::before { content: "› "; color: var(--accent); font-weight: bold; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
footer { text-align: center; padding: 2rem; color: #555; font-size: 0.9rem; }
.repo-link { margin-top: 2rem; text-align: center; }
.badge { display: inline-block; background: #24292e; color: #fff; padding: 0.4rem 1rem; border-radius: 4px; text-decoration: none; font-size: 0.9rem; }
.badge:hover { opacity: 0.9; }
</style>
</head>
<body>
<div class="container">
<header>
<h1>DeepSeeking Accountability in RBI</h1>
<p class="subtitle">Governance Failures in India's Central Bank Entity Network</p>
<a class="cta" href="book/deepseekingrbi.pdf">Download PDF Report</a>
<a class="cta" href="https://github.com/CCAgentOrg/deepseekingrbi">View on GitHub</a>
</header>

<section>
<h2>About This Report</h2>
<p>This report investigates the governance architecture of RBI's technology and payments subsidiaries — IDRBT, IFTAS, ReBIT, RBIH, NPCI — and the systemic failures that enabled the <strong>.bank.in security debacle</strong>, the <strong>IKCON single-source contract award</strong>, and the <strong>IFTAS clawback</strong> asset transfer.</p>
</section>

<section>
<h2>Chapters</h2>
<ul>
<li>1. The IKCON Award — A High-Probability Governance Failure</li>
<li>2. The Revolving Door — IDRBT's Governance Structure</li>
<li>3. The Proliferation Problem — Too Many Entities, No Accountability</li>
<li>4. IFTAS Deep-Dive — The Clawback That Revealed the System</li>
<li>5. Transparency & Accountability Matrix</li>
</ul>
</section>

<section>
<h2>Key Findings</h2>
<ul>
<li><strong>.bank.in portal</strong> awarded to IKCON Technologies without competitive tender — 33+ unauthenticated API endpoints, 5,576 records exposed</li>
<li><strong>Deepak Kumar</strong> sits on 6+ boards simultaneously — IDRBT Director while on NPCI, IFTAS, ReBIT, RBIH, and IOB boards</li>
<li><strong>IFTAS clawback</strong> — RBI built infrastructure through IDRBT, spun it off, then reabsorbed it without market pricing</li>
<li><strong>RTI exemption</strong> — All entities use opaque legal forms (Society, Section 8, Pvt Ltd) to avoid public accountability</li>
<li><strong>Revolving door</strong> — Same executives rotate between RBI → entity board → back to RBI with no cooling-off periods</li>
</ul>
</section>

<section>
<h2>Annexures & Data</h2>
<ul>
<li><a href="annexures/reference-matrix.md">Reference Matrix</a> — Cross-verified source grades for every claim</li>
<li><a href="chapters/iftas-deep-dive.md">IFTAS Deep Dive</a> — Governance, finances, revolving doors</li>
<li><a href="chapters/transparency-matrix.md">Transparency Matrix</a> — 9-dimension accountability audit across all entities</li>
</ul>
</section>

<div class="repo-link">
<a class="badge" href="https://github.com/CCAgentOrg/deepseekingrbi">CCAgentOrg/deepseekingrbi on GitHub</a>
</div>

<footer>
<p>DeepSeeking Accountability in RBI &mdash; Published 2026-07-11 by CashlessConsumer / DPI Watch</p>
<p>This work is dedicated to the public domain. Cite freely.</p>
</footer>
</div>
</body>
</html>
"""

with open("website/index.html", "w") as f:
    f.write(index_html)

# Copy book and annexures into website
import shutil
for src in ["book/deepseekingrbi.pdf"]:
    if os.path.exists(src):
        shutil.copy(src, "website/")
for d in ["chapters", "annexures"]:
    dst = os.path.join("website", d)
    shutil.copytree(d, dst, dirs_exist_ok=True)

# Add website files to git and push
run("git add -A", timeout=10)

# Set up GitHub Pages via gh API
print("=== Configuring GitHub Pages ===")
# First commit
run('git commit -m "Add website, PDF build, reference data"', timeout=10)
run("git push -u origin main", timeout=60)

# Enable Pages via gh
run('gh api repos/CCAgentOrg/deepseekingrbi/pages -X POST -f source.branch=main -f source.path=/website 2>&1 || echo "Pages config may need manual setup"', timeout=30)

print("=== DONE ===")
print("Site should be at: https://CCAgentOrg.github.io/deepseekingrbi/")
print("Repo: https://github.com/CCAgentOrg/deepseekingrbi")
