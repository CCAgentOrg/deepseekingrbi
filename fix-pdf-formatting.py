#!/usr/bin/env python3
"""Fix PDF formatting issues in full-book.md for pandoc/Eisvogel rendering."""

with open("/home/workspace/deepseekingrbi/book/full-book.md", "r") as f:
    text = f.read()

# ========== 1. Replace emoji with text markers ==========
replacements = [
    ("✅", "[✓]"),
    ("❌", "[✗]"),
    ("⚠️", "[!]"),   # with variation selector
    ("⚠", "[!]"),    # without variation selector
    ("🔴", "[●]"),   # red circle
    ("❓", "[?]"),   # question mark
    ("✅", "[✓]"),
    ("❌", "[✗]"),
    # n-dash and m-dash cleanup — keep m-dash but ensure spacing
    ("�", ""),  # replacement character
]
for old, new in replacements:
    text = text.replace(old, new)

# ========== 2. Add page breaks before major chapters ==========
# Insert \newpage before each H1 heading that starts a new chapter/section
# Be careful not to double-add
import re

# Add \newpage before H1 headings (lines starting with "# " that aren't the metadata block)
# But skip the first one (Preface) and the YAML frontmatter
lines = text.split("\n")
new_lines = []
in_yaml = False
yaml_done = False
h1_count = 0
for i, line in enumerate(lines):
    # Track YAML frontmatter
    if line.strip() == "---" and not yaml_done:
        if not in_yaml:
            in_yaml = True
            new_lines.append(line)
            continue
        else:
            in_yaml = False
            yaml_done = True
            new_lines.append(line)
            continue
    
    # Skip inside YAML
    if in_yaml:
        new_lines.append(line)
        continue
    
    # Handle H1 headings — add page break before (except for Preface which is first)
    stripped = line.strip()
    if stripped.startswith("# ") and not stripped.startswith("# "):
        h1_count += 1
        if h1_count > 1:
            # Add page break before this heading
            # Check for existing whitespace
            new_lines.append("")
            new_lines.append("\\newpage")
            new_lines.append("")
        new_lines.append(line)
    else:
        new_lines.append(line)

text = "\n".join(new_lines)

# ========== 3. Fix complex tables with line breaks in cells ==========
# Pipe tables can't have multi-line cells. Some tables in the book have 
# bullet lists or multiple paragraphs in cells. We need to convert those
# to something pandoc handles.

# Specifically fix the "governance pillar" table (Chapter 1) which has 
# line-break-separated content in cells
# Pattern: tables with many columns that have bullet-point-like content

# Fix table: Connected individuals table (IKCON leadership)
# This table has 3 columns with simple text - should work fine actually
# The issue may be that some cells have trailing spaces or special characters

# ========== 4. Ensure code-block network maps don't break across pages ==========
# Add page break hints before and after large ASCII art blocks
# The network maps are in code blocks (```) — add keep-together hints

# Find large code blocks (network maps) and surround with page break hints
def add_keep_together(match):
    content = match.group(0)
    # Only for blocks that look like network diagrams (contain ─ ┐ ┘ etc)
    if "─" in content or "┌" in content or "│" in content:
        # Add page break before and after
        return "\\newpage\n" + content + "\n\\pagebreak"
    return content

# Use a simple approach: find fenced code blocks and check if they're maps
code_block_pattern = re.compile(r"```[a-z]*\n.*?```", re.DOTALL)
text = code_block_pattern.sub(add_keep_together, text)

# ========== 5. Fix specific table rendering issues ==========
# Some tables have pipe characters in regular text that pandoc may misparse
# Tables with column alignment markers like |---| need to be proper

# Clean up table separator rows - ensure they have proper dashes
# Also fix any table row that has issues with leading/trailing pipes

# ========== 6. Add PDF-specific metadata ==========
# Add table-of-contents depth and ensure proper title page
metadata_block = text.split("---")[1] if text.startswith("---") else ""
if "table-use-row-colors: true" not in metadata_block:
    # Already has it
    pass

# ========== Write back ==========
with open("/home/workspace/deepseekingrbi/book/full-book.md", "w") as f:
    f.write(text)

print(f"Applied fixes. File size: {len(text)} chars")

# ========== 7. Now rebuild PDF ==========
import subprocess
result = subprocess.run(
    'pandoc book/full-book.md -o book/DeepSeeking_RBI_Report.pdf '
    '--from markdown+yaml_metadata_block+footnotes+fenced_code_blocks '
    '--pdf-engine=xelatex '
    '-V mainfont="DejaVu Sans" -V sansfont="DejaVu Sans" -V monofont="DejaVu Sans Mono" '
    '--highlight-style=tango --toc --toc-depth=2 -N '
    '-V toc-own-page=true -V titlepage=true -V titlepage-color=1a1a2e '
    '-V titlepage-text-color=ffffff',
    shell=True, capture_output=True, text=True, timeout=180,
    cwd="/home/workspace/deepseekingrbi"
)
if result.returncode == 0:
    print("PDF rebuild successful")
else:
    print("PDF rebuild FAILED:")
    print(result.stderr[:2000])
