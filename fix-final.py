#!/usr/bin/env python3
"""Fix final batch: scoring methodology, international table citations, Narasimham ref."""
import os

BASE = "/home/workspace/deepseekingrbi"

# === FIX 1: Add scoring methodology note to transparency-matrix.md ===
path = os.path.join(BASE, "chapters/transparency-matrix.md")
with open(path) as f:
    text = f.read()

# Insert methodology note after line 11 (after the first paragraph)
scoring_note = """\n### Methodology: Scoring Explained\n\nEach entity is scored on 9 dimensions. Per dimension: ✅ = 1 point (mechanism functions), ⚠️ = 0.5 points (partial/indirect), ❌ = 0 points (absent/denied). Maximum total = 9. The score measures **transparency & accountability architecture**, not operational performance, security posture, or mandate fulfilment. A low score means the entity has structural opacity — not that it performs its function poorly.\n\n"""

# Insert right after "The result is a systemic map..."
insertion_marker = "bypass is structurally engineered.\n\n---"
if insertion_marker in text:
    text = text.replace(insertion_marker, "bypass is structurally engineered.\n" + scoring_note + "\n---")
    with open(path, "w") as f:
        f.write(text)
    print("FIX 1: Added scoring methodology note")
else:
    print("FIX 1: SKIPPED - marker not found")

# === FIX 2: Add citations to international comparison table ===
path2 = os.path.join(BASE, "chapters/twentyfive-year-pattern.md")
with open(path2) as f:
    text2 = f.read()

# Add source note after the international comparison table
old_table_end = "India is an outlier among major economies — its central bank's technology arms operate with less external accountability than any comparable institution in the G20.\n\n---"
citations_block = """India is an outlier among major economies — its central bank's technology arms operate with less external accountability than any comparable institution in the G20. [^12]\n\n**Sources for international comparison**: BoE PSR governance structure [^13]; FedWire/FedNow oversight under FRB Act [^14]; ECB T2S governance and ECA audit mandate [^15]; UK FOI applicability to BoE [^16]; US GAO audit authority over Fed [^17]; EU transparency regulation applicability to ECB [^18].\n\n---"""

if old_table_end in text2:
    text2 = text2.replace(old_table_end, citations_block)
    with open(path2, "w") as f:
        f.write(text2)
    print("FIX 2: Added international comparison citations")
else:
    print("FIX 2: SKIPPED - table end marker not found")

# === FIX 3: Add specific citations for international sources ===
new_footnotes = """
[^13]: Bank of England — Payment Systems Regulator: Governance structure, independent board, accountability to Parliament. (https://www.psr.org.uk/about-us/governance/)
[^14]: Federal Reserve Financial Services — FedWire and FedNow oversight; GAO audit authority under 31 U.S.C. § 714. (https://www.frbservices.org/)
[^15]: European Central Bank — T2S governance and European Court of Auditors mandate under TFEU Article 287. (https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html)
[^16]: UK Freedom of Information Act 2000 — BoE designated as public authority under Schedule 1. (https://www.legislation.gov.uk/ukpga/2000/36/schedule/1)
[^17]: U.S. Government Accountability Office — GAO audit authority over Federal Reserve under 31 U.S.C. § 714. (https://www.gao.gov/about/what-gao-does/)
[^18]: EU Transparency Regulation (EC) No 1049/2001 — Applicability to ECB documents. (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32001R1049)
"""

if "[^18]:" not in text2:
    text2 += new_footnotes
    with open(path2, "w") as f:
        f.write(text2)
    print("FIX 3: Added international source footnotes to references")
else:
    print("FIX 3: SKIPPED - footnotes already exist")

# === FIX 4: Clarify Narasimham Committee reference ===
if "Narasimham" in text2 and "1991" not in text2.split("Narasimham")[0]:
    text2 = text2.replace(
        "Narasimham reforms",
        "Narasimham Committee I (1991) and II (1998) recommendations on financial sector reform, which led to RBI divestment from development finance institutions"
    )
    with open(path2, "w") as f:
        f.write(text2)
    print("FIX 4: Clarified Narasimham Committee reference")
else:
    print("FIX 4: SKIPPED")

print("\n=== All fixes complete ===")
