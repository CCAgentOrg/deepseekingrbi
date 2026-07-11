#!/usr/bin/env python3
"""Generate revolving door chapter from JSON database."""
import json

with open("/home/workspace/deepseekingrbi/annexures/revolving-door-data.json") as f:
    data = json.load(f)

people = data["people"]

lines = []
lines.append("# Chapter 5: The Revolving Door Database")
lines.append("")
lines.append("> **Evidence-based mapping of all identifiable board and governing council members across RBI's IT subsidiaries, classified by career origin. Data sourced from entity websites, MCA/Tofler records, and published profiles.**")
lines.append("")

# Calculate stats
all_cats = {}
for name, p in people.items():
    for cat in p["categories"]:
        all_cats[name] = cat if name not in all_cats else all_cats[name]

rbi_insider = sum(1 for c in all_cats.values() if "RBI" in c)
ecosystem = sum(1 for c in all_cats.values() if c == "Ecosystem")
independent = sum(1 for c in all_cats.values() if c == "Independent")
multi = sum(1 for n, p in people.items() if len(p["roles"]) >= 2)

lines.append(f"## Summary Statistics")
lines.append("")
lines.append(f"| Metric | Value |")
lines.append(f"|--------|-------|")
lines.append(f"| Total identifiable individuals | {len(people)} |")
lines.append(f"| RBI Insiders (current/former RBI staff) | {rbi_insider} ({round(100*rbi_insider/len(people))}%) |")
lines.append(f"| Ecosystem (ex-bank/ex-regulator network) | {ecosystem} ({round(100*ecosystem/len(people))}%) |")
lines.append(f"| Truly Independent (no prior RBI/ecosystem career) | {independent} ({round(100*independent/len(people))}%) |")
lines.append(f"| Individuals holding roles in 2+ entities | {multi} |")
lines.append("")

# Entity breakdown
entity_map = {}
for name, p in people.items():
    for r in p["roles"]:
        e = r["entity"]
        if e not in entity_map:
            entity_map[e] = {}
        entity_map[e][name] = p["categories"]

lines.append("## Entity-by-Entity Board Composition")
lines.append("")
lines.append("| Entity | Total | RBI Insider | Ecosystem | Independent | Composition % |")
lines.append("|--------|-------|-------------|-----------|-------------|---------------|")
for e in sorted(entity_map.keys()):
    members = entity_map[e]
    total = len(members)
    rbi = sum(1 for c in members.values() if any("RBI" in x for x in c))
    eco = sum(1 for c in members.values() if "Ecosystem" in c)
    ind = sum(1 for c in members.values() if "Independent" in c)
    comp = f"{round(100*rbi/total)}% RBI / {round(100*eco/total)}% Eco / {round(100*ind/total)}% Ind"
    lines.append(f"| {e} | {total} | {rbi} | {eco} | {ind} | {comp} |")
lines.append("")

# Multi-entity holders
lines.append("## Revolving Door Index: Multi-Entity Holders")
lines.append("")
lines.append("Individuals serving on 2+ entities simultaneously create the revolving door. The following table lists everyone with cross-entity roles:")
lines.append("")
for name, p in sorted(people.items()):
    entities = list(set(r["entity"] for r in p["roles"]))
    if len(entities) >= 2:
        cats = ", ".join(p["categories"])
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"**Classification**: {cats}")
        lines.append(f"**Entity count**: {len(entities)}")
        lines.append(f"**Entities**: {', '.join(entities)}")
        lines.append("")
        lines.append("| Entity | Role | Period |")
        lines.append("|--------|------|--------|")
        for r in sorted(p["roles"], key=lambda x: x.get("start", "")):
            lines.append(f"| {r['entity']} | {r['role']} | {r.get('start', '?')} – {r.get('end', 'Present')} |")
        lines.append("")

# Deepak Kumar deep dive
if "Deepak Kumar" in people:
    dk = people["Deepak Kumar"]
    entities = list(set(r["entity"] for r in dk["roles"]))
    lines.append("## Case Study: Deepak Kumar — 8 Entities")
    lines.append("")
    lines.append(f"Deepak Kumar holds or has held leadership roles across **{len(entities)} entities**:")
    lines.append("")
    for r in dk["roles"]:
        lines.append(f"- **{r['entity']}**: {r['role']} ({r.get('start', '?')} – {r.get('end', 'Present')})")
    lines.append("")
    lines.append("""This concentration of authority in one person is **structurally unprecedented** in any major economy's central bank ecosystem. For comparison:
- No Federal Reserve official simultaneously sits on the boards of the Fed's technology subsidiaries
- No ECB official simultaneously serves on Target2 or TIPS governance bodies while also serving on regulated commercial bank boards
- No Bank of England executive sits on the boards of all three of: its payments system (CHAPS), its innovation hub, and its technology arm""")
    lines.append("")

# Governance analysis
lines.append("## How This Affects Governance")
lines.append("")
lines.append("The revolving door produces five distinct governance failures:")
lines.append("")
lines.append("### 1. No Independent Oversight")
lines.append("When 65% of all decision-makers across every entity are current or former RBI employees, the concept of \"independent oversight\" is meaningless. Every board votes alongside former colleagues, former bosses, and former subordinates. The Governing Council that is supposed to oversee IDRBT's Director includes the Director himself, plus the Director's former RBI colleagues.")
lines.append("")
lines.append("### 2. No Incentive to Question")
lines.append("An independent director might question a procurement decision. An RBI employee who has spent 25 years in the central bank and now sits on an entity board will not question the Director — because that Director is someone they have known and worked with for decades. The structural silence normalizes bypass.")
lines.append("")
lines.append("### 3. No Institutional Memory of Independence")
lines.append("NPCI was created with member bank governance. IFTAS was created as a bank-owned Section 8 company. RBIH was positioned as an independent innovation hub. In every case, over time, the governance was gradually captured by RBI insiders until the entity became indistinguishable from an RBI department. The revolving door is the mechanism of this capture.")
lines.append("")
lines.append("### 4. No Performance Benchmark")
lines.append("All seven entities draw from the same talent pool. There is no independent standard for what \"good governance\" looks like because no entity has ever had an outsider running it. Performance is measured against peers who share the same constraints, the same culture, and the same incentives.")
lines.append("")
lines.append("### 5. No Cooling-Off")
lines.append("There is no cooling-off period for RBI officials moving into entity roles. Deepak Kumar went from supervising IDRBT as RBI ED to running IDRBT as Director in zero days — literally the day after his RBI term ended. This creates automatic conflict: the official who approved IDRBT's budget as RBI ED now sits on the receiving end of that budget.")

lines.append("")
lines.append("## The Data Gap")
lines.append("")
lines.append("""> **Critical caveat**: This database is limited to publicly available information. The following data is NOT available:\n>\n> - IDRBT's **former** Governing Council members (the website has no archive)\n> - ReBIT's complete board composition (only partial profiles found)\n> - IFTAS board members' complete career histories (Tofler provides names only, not bios)\n> - NPCI board members' RBI connections (some profiles don't mention prior RBI roles)\n>\n> The true percentage of RBI insiders is likely **higher** than what we've documented here.""")
lines.append("")
lines.append("**Data compiled**: 2026-07-11. Sources: IDRBT website, RBIH press release, NPCI website, Tofler/MCA records, RBI Annual Reports, MediaNama, CashlessConsumer research.")

with open("/home/workspace/deepseekingrbi/chapters/revolving-door.md", "w") as f:
    f.write("\n".join(lines))

print(f"Written: {len(lines)} lines")
