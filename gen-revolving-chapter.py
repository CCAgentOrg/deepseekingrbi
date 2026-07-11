import json, os

data = json.load(open("/home/workspace/deepseekingrbi/annexures/revolving-door-data.json"))
people = data["people"]

# Classify
def classify(p):
    c = p.get("classification", "")
    if "RBI Insider" in c: return "RBI Insider"
    if "Ecosystem" in c: return "Ecosystem"
    if "Independent" in c: return "Independent"
    return "Unknown"

counts = {"RBI Insider": 0, "Ecosystem": 0, "Independent": 0, "Unknown": 0}
for p in people.values():
    counts[classify(p)] += 1
total = sum(counts.values())

lines = []
lines.append("# Chapter 5: The Revolving Door — A Database of Overlaps")
lines.append("")
lines.append(f"> **Total Identifiable Individuals**: {total} across all entities")
lines.append("")
lines.append("## Summary Statistics")
lines.append("")
lines.append(f"| Classification | Count | Percentage |")
lines.append(f"|---------------|-------|-----------|")
for cat in ["RBI Insider", "Ecosystem", "Independent", "Unknown"]:
    if counts[cat] > 0:
        pct = round(counts[cat]/total*100)
        lines.append(f"| **{cat}** | {counts[cat]} | {pct}% |")
lines.append("| **Total** | **{total}** | **100%** |")
lines.append("")

# Multi-entity holders
multi = {k: v for k, v in people.items() if len(v.get("entities", [])) >= 2}
sorted_multi = sorted(multi.items(), key=lambda x: len(x[1].get("entities", [])), reverse=True)

lines.append("## Multi-Entity Holders (Revolving Door Index)")
lines.append("")
lines.append("The following individuals hold roles in **2 or more** of the entities surveyed:")
lines.append("")
lines.append(f"| Name | Classification | Entities | Roles |")
lines.append(f"|------|---------------|----------|-------|")
for name, p in sorted_multi:
    ents = p.get("entities", [])
    roles = p.get("roles", [])
    if isinstance(roles, list):
        roles_str = "; ".join(roles[:3])
        if len(roles) > 3:
            roles_str += f" (+{len(roles)-3} more)"
    else:
        roles_str = roles
    lines.append(f"| **{name}** | {classify(p)} | {len(ents)} ({', '.join(ents[:4])}) | {roles_str} |")

lines.append("")
lines.append("### Deepak Kumar: The Ultimate Insider")
lines.append("")
lines.append("Deepak Kumar holds or has held positions in **8 entities**:")
for ent in people.get("Deepak Kumar", {}).get("entities", []):
    lines.append(f"- {ent}")
lines.append("")
lines.append("He is simultaneously:")
lines.append("- **Supervisor** (RBI ED, IT Department — oversaw IDRBT, IFTAS, ReBIT)")
lines.append("- **Operator** (Director, IDRBT — now running the entity he used to oversee)")
lines.append("- **Board member** (IFTAS, ReBIT, RBIH, NPCI, IOB — all entities his current role interacts with)")
lines.append("- **Oversight subject** (Member of IDRBT Governing Council — the body that oversees him)")
lines.append("")
lines.append("> This is not a conflict of interest. This is the **elimination of the possibility of conflict** by making one person the entire chain.")

os.makedirs("/home/workspace/deepseekingrbi/chapters", exist_ok=True)
with open("/home/workspace/deepseekingrbi/chapters/revolving-door.md", "w") as f:
    f.write("\n".join(lines) + "\n")
print("Written revolving-door.md")
