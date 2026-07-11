#!/usr/bin/env python3
"""Build the DeepSeekingRBI GitHub Pages website from markdown chapters."""

import os, re, html as htmlmod
from pathlib import Path

BASE = Path("/home/workspace/deepseekingrbi")
WEBSITE = BASE / "website"
CHAPTERS_DIR = WEBSITE / "chapters"
ANNEXURES_DIR = WEBSITE / "annexures"
ASSETS_DIR = WEBSITE / "assets"
CSS_HREF = "/deepseekingrbi/assets/style.css"

# Ensure dirs
for d in [CHAPTERS_DIR, ANNEXURES_DIR, ASSETS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def slug(name):
    return name.lower().replace(" ", "-").replace(":", "").replace("—", "").replace("(", "").replace(")", "").replace("'", "")

def wrap(title, body, is_index=False):
    nav = """
    <header>
      <div class="logo">Deep<span>Seeking</span> RBI</div>
      <nav>
        <a href="/deepseekingrbi/">Home</a>
        <a href="/deepseekingrbi/chapters/chapter-1">Ch.1 - IKCON</a>
        <a href="/deepseekingrbi/chapters/chapter-2">Ch.2 - Revolving Door</a>
        <a href="/deepseekingrbi/chapters/revolving-door-database">Revolving Door DB</a>
        <a href="/deepseekingrbi/chapters/chapter-3">Ch.3 - Proliferation</a>
        <a href="/deepseekingrbi/chapters/iftas-deep-dive">IFTAS</a>
        <a href="/deepseekingrbi/chapters/transparency-matrix">Transparency</a>
        <a href="/deepseekingrbi/book/full-book">Full Book</a>
        <a href="/deepseekingrbi/DeepSeeking_RBI_Report.pdf">PDF</a>
      </nav>
    </header>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)} — DeepSeeking Accountability in RBI</title>
<link rel="stylesheet" href="{CSS_HREF}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
{nav}
<div class="{'hero' if is_index else 'chapter'}">
{body}
</div>
<footer>
  <p><strong>DeepSeeking Accountability in RBI</strong> — A governance investigation by <a href="https://cashlessconsumer.in">CashlessConsumer</a> | <a href="https://github.com/CCAgentOrg/deepseekingrbi">GitHub</a></p>
</footer>
</body>
</html>"""

def md_to_html(md_text, is_index=False):
    """Convert a subset of markdown to HTML."""
    # Strip YAML frontmatter --- ... ---
    lines = md_text.splitlines()
    if lines and lines[0].strip() == '---':
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_idx = i
                break
        if end_idx is not None:
            lines = lines[end_idx + 1:]
            md_text = '\n'.join(lines).strip()
    lines = md_text.split('\n')
    html = []
    in_table = False
    table_mode = None  # 'header', 'body'
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headers
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            content = m.group(2)
            # Handle references in headers
            refs = re.findall(r'\[\^(\d+)\]', content)
            content = re.sub(r'\[\^(\d+)\]', r'<sup><a href="#ref-\1">[\1]</a></sup>', content)
            # Handle inline code
            content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
            # Handle emphasis
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
            # Handle links
            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', content)
            html.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue
        
        # Horizontal rules
        if line.strip() in ('---', '***', '___'):
            html.append('<hr>')
            if in_table:
                html.append('</tbody></table>')
                in_table = False
            i += 1
            continue
        
        # Blockquote
        if line.startswith('> '):
            content = line[2:]
            # Handle bold/links in blockquotes
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', content)
            content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
            html.append(f'<blockquote><p>{content}</p></blockquote>')
            i += 1
            continue
        
        # Table
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            tag = 'th' if not in_table else ('th' if table_mode == 'header' else 'td')
            
            if not in_table:
                html.append('<table>')
                if not re.match(r'^\|[\s\-:]+\|', line):
                    html.append('<thead><tr>')
                    for c in cells:
                        html.append(f'<th>{c}</th>')
                    html.append('</tr></thead><tbody>')
                    table_mode = 'body'
                in_table = True
            elif re.match(r'^\|[\s\-:]+\|', line):
                table_mode = 'body'
            else:
                html.append('<tr>')
                for c in cells:
                    # Handle links in table cells
                    c = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', c)
                    c = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', c)
                    c = re.sub(r'`([^`]+)`', r'<code>\1</code>', c)
                    html.append(f'<{tag}>{c}</{tag}>')
                html.append('</tr>')
            
            i += 1
            continue
        else:
            if in_table:
                html.append('</tbody></table>')
                in_table = False
        
        # Empty lines
        if not line.strip():
            i += 1
            continue
        
        # Regular paragraph
        content = line
        
        # Handle footnotes at end
        m = re.match(r'^\[(\^?\d+)\]:\s+(.+)$', content)
        if m:
            ref_id = m.group(1).lstrip('^')
            ref_text = m.group(2)
            ref_text = re.sub(r'\(([^)]+)\)', r'<a href="\1">\1</a>', ref_text)
            html.append(f'<p class="footnote" id="ref-{ref_id}"><strong>[{ref_id}]</strong> {ref_text}</p>')
            i += 1
            continue
        
        # Bold
        content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
        # Italic
        content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
        # Code
        content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
        # Links
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', content)
        # References
        content = re.sub(r'\[\^(\d+)\]', r'<sup><a href="#ref-\1">[\1]</a></sup>', content)
        # File references
        content = re.sub(r'`file\s+([^`]+)`', r'<code>\1</code>', content)
        
        html.append(f'<p>{content}</p>')
        i += 1
    
    if in_table:
        html.append('</tbody></table>')
    
    return '\n'.join(html)

def build():
    chapters = [
        ("preface", "Preface: When Journalism Fails", "book/preface.md"),
        ("chapter-1", "Chapter 1: The IKCON Award", "chapters/rbi_governance.md"),
        ("chapter-2", "Chapter 2: The Revolving Door at IDRBT", "chapters/rbi_governance.md"),
        ("revolving-door-database", "Revolving Door Database", "chapters/revolving-door.md"),
        ("chapter-3", "Chapter 3: Too Many Entities, No Accountability", "chapters/rbi_governance.md"),
        ("iftas-deep-dive", "Chapter 4: IFTAS Deep-Dive", "chapters/iftas-deep-dive.md"),
        ("transparency-matrix", "Chapter 5: Transparency & Accountability Matrix", "chapters/transparency-matrix.md"),
        ("historical-survey", "Historical Survey of RBI Subsidiaries", "chapters/rbi-subsidiaries-survey.md"),
    ]
    
    # Nav links
    nav_links = [
        ("/deepseekingrbi/", "Home"),
        ("/deepseekingrbi/chapters/preface", "Preface"),
        ("/deepseekingrbi/chapters/chapter-1", "Ch.1 - IKCON"),
        ("/deepseekingrbi/chapters/revolving-door-database", "Revolving Door DB"),
        ("/deepseekingrbi/chapters/iftas-deep-dive", "IFTAS"),
        ("/deepseekingrbi/chapters/transparency-matrix", "Transparency"),
        ("/deepseekingrbi/book/full-book", "Full Book"),
    ]
    
    # Build main index
    with open(BASE / "book" / "cover.md") as f:
        cover = f.read()
    
    index_html = """
<h1>DeepSeeking Accountability in RBI</h1>
<h2>Governance Failures in India's Central Bank Entity Network</h2>
<p><strong>Author:</strong> CashlessConsumer</p>
<p><strong>Date:</strong> July 2026</p>
<p>This investigation explores systemic governance failures within India's central bank entity network, examining how overlapping mandates, lack of accountability, and structural conflicts have enabled regulatory capture and weakened oversight mechanisms.</p>
"""
    
    # Add chapter list
    index_html += """
<h2 style="margin-top:3rem;">Chapters</h2>
<ol class="chapter-list" style="margin-top:1rem;">
<li><span class="title"><a href="chapters/chapter-1">Chapter 1: The IKCON Award</a></span><br><span class="desc">Reconstructing the high-probability governance failure — no-tender award, byelaw amendment allegations, and the IFTAS→IKCON revolving door.</span></li>
<li><span class="title"><a href="chapters/chapter-2">Chapter 2: The Revolving Door at IDRBT</a></span><br><span class="desc">Deepak Kumar's simultaneous directorships, the 3-month placeholder appointment, and the Governing Council's structural conflicts.</span></li>
<li><span class="title"><a href="chapters/revolving-door-database">Revolving Door Database</a></span><br><span class="desc">Evidence-backed analysis of 29 identifiable individuals across 6 entities — 65% are RBI insiders. Entity-by-entity classification with governance impact.</span></li>
<li><span class="title"><a href="chapters/chapter-3">Chapter 3: Too Many Entities, No Accountability</a></span><br><span class="desc">How seven RBI-controlled entities with overlapping mandates create diffuse responsibility and zero external oversight.</span></li>
<li><span class="title"><a href="chapters/iftas-deep-dive">Chapter 4: IFTAS — The Clawback That Explains Everything</a></span><br><span class="desc">The 2009 Rangarajan Committee, INFINET/SFMS transfer, 2019 RBI acquisition — the template for asset consolidation.</span></li>
<li><span class="title"><a href="chapters/transparency-matrix">Chapter 5: Transparency & Accountability Matrix</a></span><br><span class="desc">9-dimension accountability audit of all RBI IT arms across RTI, CAG, legal structure, and board independence.</span></li>
<li><span class="title"><a href="chapters/historical-survey">Historical Survey of RBI Subsidiaries</a></span><br><span class="desc">Comprehensive historical overview of RBI's entity creation and governance patterns.</span></li>
</ol>
"""
    
    index_html += """
<h2 style="margin-top:3rem;">Download</h2>
<p><a href="/deepseekingrbi/DeepSeeking_RBI_Report.pdf" class="download-btn">📄 Download Full Report (PDF, 63 pages)</a></p>
"""
    
    with open(WEBSITE / "index.html", "w") as f:
        f.write(wrap("Home", index_html, is_index=True))
    
    print("Written: index.html")
    
    # Extract chapter sections from rbi_governance.md
    with open(BASE / "chapters" / "rbi_governance.md") as f:
        governance = f.read()
    
    # Split by ## Chapters
    ch1_start = governance.find("## Chapter 1:")
    ch2_start = governance.find("## Chapter 2:")
    ch3_start = governance.find("## Chapter 3:")
    
    ch1_text = governance[ch1_start:ch2_start] if ch1_start >= 0 else ""
    ch2_text = governance[ch2_start:ch3_start] if ch2_start >= 0 else ""
    ch3_text = governance[ch3_start:] if ch3_start >= 0 else ""
    
    # Also extract the intro (before Chapter 1)
    intro_text = governance[:ch1_start] if ch1_start >= 0 else ""
    
    # Write chapter 1 with intro
    full_ch1 = intro_text + "\n\n" + ch1_text
    with open(CHAPTERS_DIR / "chapter-1.html", "w") as f:
        f.write(wrap("Chapter 1", md_to_html(full_ch1)))
    print("Written: chapter-1.html")
    
    with open(CHAPTERS_DIR / "chapter-2.html", "w") as f:
        f.write(wrap("Chapter 2", md_to_html(ch2_text)))
    print("Written: chapter-2.html")
    
    with open(CHAPTERS_DIR / "chapter-3.html", "w") as f:
        f.write(wrap("Chapter 3", md_to_html(ch3_text)))
    print("Written: chapter-3.html")
    
    # IFTAS
    with open(BASE / "chapters" / "iftas-deep-dive.md") as f:
        iftas = f.read()
    with open(CHAPTERS_DIR / "iftas-deep-dive.html", "w") as f:
        f.write(wrap("IFTAS Deep-Dive", md_to_html(iftas)))
    print("Written: iftas-deep-dive.html")
    
    # Historical survey
    with open(BASE / "chapters" / "rbi-subsidiaries-survey.md") as f:
        survey = f.read()
    with open(CHAPTERS_DIR / "historical-survey.html", "w") as f:
        f.write(wrap("Historical Survey", md_to_html(survey)))
    print("Written: historical-survey.html")
    
    # Transparency matrix
    with open(BASE / "chapters" / "transparency-matrix.md") as f:
        matrix = f.read()
    with open(WEBSITE / "chapters" / "transparency-matrix.html", "w") as f:
        f.write(wrap("Transparency Matrix", md_to_html(matrix)))
    print("Written: transparency-matrix.html")
    
    # --- Build Preface ---
    with open(BASE / "book" / "preface.md") as f:
        preface_text = f.read()
    # Strip YAML frontmatter if present
    if preface_text.startswith("---"):
        parts = preface_text.split("---", 2)
        if len(parts) >= 3:
            preface_text = parts[2].strip()
    with open(CHAPTERS_DIR / "preface.html", "w") as f:
        f.write(wrap("Preface: When Journalism Fails", md_to_html(preface_text)))
    print("Written: preface.html")
    
    # Reference matrix annexure
    # Revolving door database
    with open(BASE / "chapters" / "revolving-door.md") as f:
        revolving = f.read()
    with open(CHAPTERS_DIR / "revolving-door-database.html", "w") as f:
        f.write(wrap("Revolving Door Database", md_to_html(revolving)))
    print("Written: revolving-door-database.html")

    with open(BASE / "annexures" / "reference-matrix.md") as f:
        ref_matrix = f.read()
    with open(ANNEXURES_DIR / "reference-matrix.html", "w") as f:
        f.write(wrap("Reference Matrix", md_to_html(ref_matrix)))
    print("Written: reference-matrix.html")
    
    # Full book
    book_path = BASE / "book" / "full-book.md"
    if book_path.exists():
        with open(book_path) as f:
            book = f.read()
        full_html = md_to_html(book)
        # Add TOC at top
        toc = """<h2>Table of Contents</h2>
<ol>
  <li><a href="#preface-when-journalism-fails">Preface: When Journalism Fails</a></li>
  <li><a href="#chapter-1-the-ikcon-award">Chapter 1: The IKCON Award</a></li>
  <li><a href="#chapter-2-the-revolving-door">Chapter 2: The Revolving Door</a></li>
  <li><a href="#chapter-3-too-many-entities">Chapter 3: Too Many Entities</a></li>
  <li><a href="#chapter-4-iftas">Chapter 4: IFTAS Deep-Dive</a></li>
  <li><a href="#chapter-5-transparency-matrix">Chapter 5: Transparency Matrix</a></li>
</ol>
"""
        full_html = toc + full_html
        with open(WEBSITE / "book" / "full-book.html", "w") as f:
            f.write(wrap("Full Report", full_html))
        print("Written: full-book.html")
    
    print("Website build complete.")

if __name__ == "__main__":
    build()
