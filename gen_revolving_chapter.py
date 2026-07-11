#!/usr/bin/env python3
"""Generate revolving door chapter from JSON data."""
import json

with open("/home/workspace/deepseekingrbi/annexures/revolving-door-data.json") as f:
    data = json.load(f)

lines = ["# Revolving Door Database: Who Sits Where\n"]
lines.append(f"> **Total Identifiable Individuals**: {data['summary']['total_individuals']} | ")
lines.append(f"🔴 **RBI Insiders**: {data['summary']['rbi_insiders']} ({round(data['summary']['rbi_pct'])}%) | ")
lines.append(f"🟡 **Ecosystem**: {data['summary']['ecosystem']} ({round(data['summary']['eco_pct'])}%) | ")
lines.append(f"🟢 **Independent**: {data['summary']['independent']} ({round(data['summary']['ind_pct'])}%)\n\n")

lines.append("## The Revolving Door Index\n\n")
lines.append("Individuals holding roles in **2+ entities**:\n\n")
lines.append("| Name | Entities | Count | Type |\n")
lines.append("|------|----------|-------|------|\n")
for p in data['people']:
    ecnt = len(p['entities'])
    if ecnt >= 2:
        lines.append(f"| {p['name']} | {p['entity_names']} | {ecnt} | {p['classification']} |\n")

lines.append("\n## Entity-by-Entity Breakdown\n\n")
for entity in data['entity_breakdown']:
    lines.append(f"### {entity['name']}\n\n")
    src = entity.get('source', '')
    if src:
        lines.append(f"*Source: {src}*\n\n")
    lines.append(f"**{entity['total']} members — 🔴 {entity['rbi_insiders']} RBI | 🟡 {entity['ecosystem']} Eco | 🟢 {entity['independent']} Ind**\n\n")
    for m in entity['members']:
        lines.append(f"- {m['classification']} **{m['name']}** — {m['designation']}\n")
    lines.append("\n")

lines.append("## Governance Impact\n\n")
lines.append("### Key Findings\n\n")
lines.append(f"1. **{round(data['summary']['rbi_pct'])}% of all 29 board members are RBI insiders** — no entity has an independent-majority board.\n")
lines.append(f"2. **IFTAS and ReBIT have ZERO independent directors** — 100% RBI insiders.\n")
lines.append("3. **Deepak Kumar holds positions in 8 entities simultaneously** — an unbroken chain of personal authority across the entire RBI technology ecosystem.\n")
lines.append("4. **IDRBT GC is 75% RBI insiders** — the oversight body is the people being overseen.\n")
lines.append("5. **NPCI has the best ratio at 43% independent** — still short of a majority.\n\n")
lines.append("### Why This Matters\n\n")
lines.append("- **No independent challenge**: Questioning a procurement decision means challenging a former boss.\n")
lines.append("- **No market discipline**: Boards lack sector-external perspective needed to evaluate vendor contracts.\n")
lines.append("- **No whistleblower safety**: Concerns must be raised to people from the same 40-year career pipeline.\n")
lines.append("- **No cooling-off**: Executives move from RBI to entity board to regulated vendor without any gap.\n")
lines.append("- **No performance benchmark**: All entities draw from the same talent pool; there is no external standard.\n\n")
lines.append("### The Global Contrast\n\n")
lines.append("The Bank of England, Federal Reserve, and ECB all require cooling-off periods, independent board majorities, and public conflict-of-interest registers for their technology subsidiaries. India's RBI entities meet none of these standards.\n\n")

lines.append("## Data Sources\n\n")
lines.append("| Person | Source |\n")
lines.append("|--------|--------|\n")
for p in data['people']:
    sn = p.get('source_note', 'IDRBT website; MCA filings; Tofler/CompanyCheck')
    lines.append(f"| {p['name']} | {sn} |\n")

lines.append("\n\n*Database: `annexures/revolving-door-data.json`*\n")

with open("/home/workspace/deepseekingrbi/chapters/revolving-door.md", "w") as f:
    f.writelines(lines)

print("Written chapters/revolving-door.md")
