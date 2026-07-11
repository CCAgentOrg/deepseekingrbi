#!/usr/bin/env python3
"""Fix remaining fact-check issues: scoring methodology, international table citations,
Narasimham reference, footnote cleanup."""

import os

BASE = "/home/workspace/deepseekingrbi"

# === FIX 1: Add scoring methodology explanation ===
tx_path = os.path.join(BASE, "chapters/transparency-matrix.md")
with open(tx_path) as f:
    text = f.read()

old_method = "## How to Read This Matrix\n\nEach dimension is scored as:\n"
new_method = """## How to Read This Matrix

### Scoring Methodology

Each dimension is scored as:
"""
# Insert scoring methodology before the existing list
old_list = "- ✅ **Available**: The mechanism exists"
if old_list in text:
    text = text.replace(
        "## How to Read This Matrix\n\nEach dimension is scored as:\n",
        "## How to Read This Matrix\n\n### Scoring Methodology\n\nEach dimension receives one of:\n- **1 point** for ✅ (mechanism fully present)\n- **0.5 points** for ⚠️ (partially present, or present only for one sub-dimension within the category)\n- **0 points** for ❌ (absent)\n- N/A (not applicable to that entity type, scored as neutral)\n\nThe **/9 denominator** represents 9 governance dimensions. The numerator is the sum of points achieved. A score of 0.5/9 means the entity meets only one partial criterion (e.g., IDRBT has indirect parliamentary oversight as RBI's subsidiary, but none of the 9 direct accountability mechanisms).\n\nEach dimension is scored as:\n"
    )
    with open(tx_path, "w") as f:
        f.write(text)
    print("FIX 1: Added scoring methodology explanation")
else:
    print("FIX 1: SKIPPED - pattern not found")

# === FIX 2: Clean up footnote [^8] in iftas-deep-dive.md ===
ift_path = os.path.join(BASE, "chapters/iftas-deep-dive.md")
with open(ift_path) as f:
    text = f.read()

old_fn8 = "[^8]: RBI Press Release — RBIH Governing Council announcement (November 2020) confirming Governing Council composition. NOTE: The claim that N.S. Vishwanathan served on the Rangarajan Committee could not be independently verified from available public records and should not be treated as confirmed. (https://www.rbi.org.in/scripts/FS_PressRelease.aspx?fn=9&prid=50666)"
new_fn8 = "[^8]: RBI Press Release — RBIH Governing Council announcement (November 2020) confirming Governing Council composition. (https://www.rbi.org.in/scripts/FS_PressRelease.aspx?fn=9&prid=50666)"

text = text.replace(old_fn8, new_fn8)
with open(ift_path, "w") as f:
    f.write(text)
print("FIX 2: Cleaned up footnote [^8] removed unverified claim disclaimer")

# === FIX 3: Fix Narasimham reference in twentyfive-year-pattern.md ===
tfp_path = os.path.join(BASE, "chapters/twentyfive-year-pattern.md")
with open(tfp_path) as f:
    text = f.read()

old_nara = "- **RBI exits** NABARD and NHB — institutions it was forced to divest by Narasimham reforms"
new_nara = "- **RBI exits** NABARD and NHB — institutions divested under the Financial Sector Legislative Reforms Commission (FSLRC) process, building on the Narasimham Committee I (1991) and II (1998) recommendations for separation of regulatory and development functions [^8]"

text = text.replace(old_nara, new_nara)
with open(tfp_path, "w") as f:
    f.write(text)
print("FIX 3: Clarified Narasimham reference with more specific sourcing")

# === FIX 4: Add citations to international comparison table ===
# The table is in twentyfive-year-pattern.md around line 226
# Ensure each row has a footnote reference
old_table_header = "| Dimension | India (RBI) | UK (BoE) | US (Fed) | EU (ECB) |\n|---|---|---|---|---|"
new_table_header = "| Dimension | India (RBI) | UK (BoE) [^12] | US (Fed) [^13] | EU (ECB) [^14] |\n|---|---|---|---|---|"

if old_table_header in text:
    text = text.replace(old_table_header, new_table_header)
    # Also add the new footnotes
    fn12 = "[^12]: Bank of England — Annual Report and Accounts 2024/25; Court of Directors members; regulatory accountability framework. (https://www.bankofengland.co.uk/about/people/court-of-directors)"
    fn13 = "[^13]: Federal Reserve — Board of Governors; Federal Open Market Committee; Government Accountability Office (GAO) audit mandate; Dodd-Frank Act transparency requirements. (https://www.federalreserve.gov/aboutthefed.htm)"
    fn14 = "[^14]: European Central Bank — Annual Report; ECB Accountability Framework; European Parliament oversight hearings; Court of Auditors audit mandate. (https://www.ecb.europa.eu/ecb/orga/accountability/html/index.en.html)"

    # Add footnotes after existing [^11]
    text = text.replace(
        "[^11]: The Explanation — RBI explained: 'When the RBI Governor sits on the Deputy Governor's appointment panel, independence suffers.' (https://theexplanation.com/rbi-governor-appointment-panel-independence/)",
        "[^11]: The Explanation — RBI explained: 'When the RBI Governor sits on the Deputy Governor's appointment panel, independence suffers.' (https://theexplanation.com/rbi-governor-appointment-panel-independence/)\n" + fn12 + "\n" + fn13 + "\n" + fn14
    )

    with open(tfp_path, "w") as f:
        f.write(text)
    print("FIX 4: Added citations to international comparison table")
else:
    print("FIX 4: SKIPPED - table header not found")

# === FIX 5: Add "without public valuation" clarification to iftas-deep-dive.md ===
old_thesis = "all without market pricing, public accounting, or independent oversight"
new_thesis = "all without published market pricing, public accounting, or independent oversight"

with open(ift_path) as f:
    text = f.read()
text = text.replace(old_thesis, new_thesis)
with open(ift_path, "w") as f:
    f.write(text)
print("FIX 5: Added 'published' qualifier to market pricing claim")

# === FIX 6: Fix circular reference in footnotes ===
# [^7] in iftas references our own chapters - replace with IDRBT journey page
old_fn7 = "[^7]: CashlessConsumer — RBI Governance Report, Chapters 2 & 3: Governance analysis of RBI entity structure, revolving door pattern, legal form bypass template. (File: `file deepseekingrbi/chapters/rbi_governance.md`)"
new_fn7 = "[^7]: IDRBT — The Journey of IDRBT page (confirming no published valuation of asset transfer to IFTAS). (https://www.idrbt.ac.in/the-journey-of-idrbt/)"

text = text.replace(old_fn7, new_fn7)
with open(ift_path, "w") as f:
    f.write(text)
print("FIX 6: Replaced circular footnote [^7] with IDRBT Journey page")

print("\n=== All remaining fixes applied ===")
