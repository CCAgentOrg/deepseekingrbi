# Adversarial Review: DeepSeeking Accountability in RBI

> **Date**: 2026-07-19  
> **Role**: Adversarial editor — find what's weak, what's missing, what could be attacked by a critical reader or by the institutions under scrutiny.

---

## Cross-Cutting Issues

### 1. Overuse of insider shorthand
The executive summary opens with "IDRBT, IFTAS, ReBIT, RBIH, NPCI" — seven acronyms in one sentence with zero parenthetical expansion. A reader new to the topic (e.g., a journalist, foreign policy researcher, CIC member) bounces. **Fix**: First use of each acronym in each section gets a parenthetical gloss ("Reserve Bank Information Technology Private Limited").

### 2. No "audience" framing
The report doesn't state who it's written for. The tone oscillates between academic paper, investigative journalism, and activist document. This creates credibility gaps: legal readers will want sourcing standards, journalists want narrative hooks, general readers want stakes. **Fix**: Add a brief "Who This Is For" note at the top of each chapter or in the introduction.

### 3. Source markers in body text are inconsistent
Some inline claims have `[^n]` markers, others don't. The website HTML needs the same care — missing footnotes degrade trust. The big one: the security breach numbers (33 APIs, 5,576 records, 1,072 orphans) need to cite Medianama [^1] on every paragraph where they appear, not just the first.

### 4. No "if true" / confidence qualifier on the most explosive claim
The byelaw amendment allegation (§1.4) is the strongest charge (deliberate rule manipulation to benefit a connected vendor), but it's graded 🔴 *Allegation only* — and the text handles this well *except* the executive summary. The exec summary says "a portal managing the internet identity of every Indian bank was built by an untendered vendor" without noting the byelaw amendment *allegation*. This means the summary is technically accurate but a careful reader will note the grade gap.

### 5. Named entity disclosure
Deepak Kumar and Mahesh Jarati are named as central actors. The report should state explicitly whether either was contacted for comment and, if not, why. This is standard investigative practice; omitting it is a liability if the report is attacked for bias.

### 6. Visual navigability
The markdown is dense. Chapter 3's entity map is textual. A network diagram, even a simple one, would transform reader comprehension. Consider a Sankey or graph diagram of who sits where.

---

## Chapter 1: The IKCON Award

###   Strengths
- Source grading table at §1.8 is excellent — one of the best features of the report.
- The self-oversight paradox in §1.3 is clearly explained and well-evidenced.
- Alternate Explanations (§1.6) adds credibility by pre-empting counter-arguments.
- Responses to Likely Defenses (§1.7) is a strong closing move.

###   Weaknesses

#### §1.1 The Contract
- **No exposure window**: "33+ unauthenticated API endpoints" needs the timeframe — the portal was live for *over 13 months* before discovery (Medianama: 8 June → 25 June 2026). That's the headline, not a detail.
- **No harm framing**: What does "5,576 user records exposed" mean in practice? Are these live credentials? Could they enable bank domain hijacking? The report assumes the reader connects the dots. Spell it out: "Every Indian bank's domain registrar credentials were exposed — the equivalent of giving a hacker the master key to the banking sector's internet identity."
- **Orphan Super Admin accounts**: 1,072 orphan Super Admins is extraordinary — it means the system had *more Super Admins than active user accounts* at some ratios. Why wasn't there permission hygiene? This suggests no operational security at all.

#### §1.2 The Vendor
- **IKCON revenue gap**: You correctly note ₹3.9 Cr revenue (FY2025) but don't compare it to the likely contract value. A .bank.in portal for 1,500 banks, with CA integration, a registrar dashboard, 22 employee accounts — what would a competitive tender have valued this at? Even a rough estimate (e.g., "₹50 lakh to ₹2 Cr annually for maintenance, comparable to registrar SaaS platforms") would strengthen the case that a ₹3.9 Cr company was over-extended.
- **Track record**: "No prior domain registry management" is stated but not elaborated. How many people can register a domain? How many TLD registries operate in India? What makes this unusual? A brief explainer on what running a domain registry requires (DNSSEC, CA integration, registrar infrastructure, 24/7 uptime) would help a non-technical reader.

#### §1.3 Key Actors
- **Deepak Kumar timeline**: "Appointed 2 May 2024" — but the portal was live in early 2024. If he didn't approve the contract, who did? The report needs to acknowledge that the contract decision likely preceded him, and shift the critique to: (a) the systemic incentives that allow such awards, (b) his failure to remediate once in charge.
- **Mahesh Jarati caveat**: The caveat note after §1.3 is good. But it's buried. Consider elevation to an explicit "Confidence Note" box.
- **Lack of motivation analysis**: Why would Mahesh Jarati move from IFTAS to IKCON? The report says "textbook revolving-door" but doesn't examine possible motivations (better pay at a private firm, equity stake in IKCON, role in building the system he helped design). Even speculation with ⚠️ markers would enrich the narrative.

#### §1.4 Byelaw Amendment
- **GC meeting timing**: You note the 80th GC meeting on 21 June 2024 (49 days after Kumar's appointment) as a possible venue. This is good detective work. But where is the 79th GC meeting date? If the 79th meeting was in early 2024 and no procurement change appears in those minutes, the 80th meeting becomes more suspect. Work the timeline backwards.
- **Threshold ambiguity**: The report says "raised single-source procurement thresholds" but doesn't give a *sense* of what the threshold might have been. Industry standard for government IT procurement in India: ₹25 lakhs or below for single source; above that, competitive bidding is mandatory under GFR 2024 for government entities. Even though IDRBT is not technically under GFR, this comparison gives a benchmark. Add it.

#### §1.5 Safeguards That Failed
- **CAG exemption**: Strong legal analysis. Add the specific legal provision (Section 19 of the CAG Act, 1971 — applies to "any body or authority… established by or under any Central Act"). IDRBT is registered under the AP Societies Registration Act, 1350 Fasli — a state law. That's the precise mechanism of CAG bypass.
- **RTI exemption**: The report cites "Annexure D" for RTI claims against IDRBT. This annexure does not appear to exist in the published files. Either add it or remove the reference.

#### §1.6 Alternate Explanations
- **Counter-argument A** (lawful single-source): The report's response is good but could be stronger by asking: "If the byelaws were followed, why has IDRBT not published the single-source justification — a standard requirement under any procurement framework?" This turns absence of evidence into an evidence point.
- **Counter-argument C** (IKCON subcontracting): The ₹3.9 Cr revenue point is solid. Bolster it: ₹3.9 Cr revenue means IKCON had approximately 20-25 employees at prevailing IT services billing rates. Managing a TLD registrar for 1,500+ banks, with CA integration, security compliance, and 24/7 operations, would typically require a team of 8-12 *just for operations* — and that's before development, security, and management overhead. 22 IKCON employee accounts on the portal support this concern rather than alleviating it.

#### §1.7 Responses to Likely Defenses
- **"Patched within 17 days" response**: Good. Add: "Moreover, the fact that the vulnerabilities were not discovered internally but by external researchers is itself a governance failure. A properly resourced security operations center — which a national domain registry should have — would have found these during routine testing."
- **"The contract was too small" response**: This is the strongest response in the section. Consider moving it up.
- **Missing defense: "No harm occurred."** This is the most likely defense from IDRBT/RBI — "the data was encrypted, no breach was confirmed, no bank was compromised." Pre-empt it: "Exposure of 1,072 orphan Super Admin accounts means the scope for compromise is unbounded. The absence of confirmed harm is not evidence of security; it is evidence that no detection capability existed."

#### §1.8 Source Grading
- Excellent. Add: the `Guardians of the .bank.in Garden` report from webhosting.today as a cross-source for the no-tender finding.
- Consider adding a "What Would Upgrade the 🔴 Claims" column.

---

## Chapter 2: The Revolving Door

###   Strengths
- The Deepak Kumar directorship map is devastating evidence.
- The "placeholder" observation (Nikhila's 3-month tenure) is sharp.
- The IFTAS clawback section is one of the most original findings in the report.

###   Weaknesses

*(Detailed review to follow when we reach Chapter 2.)*

---

## Chapter 3: Proliferation

###   Strengths
- The governance bypass template (§3.3) is a powerful analytical contribution.
- The cross-entity comparison table (§3.5) should be on the website front page.
- NPCI for-profit conversion analysis is well-timed given ongoing debates.

###   Weaknesses

*(Detailed review to follow when we reach Chapter 3.)*

---

## Recommendations (Priority Order)

1. ** [P0] Write the RTI applications recommended in §1.4** — the strongest path to upgrade the 🔴 allegation.
2. ** [P0] Build the revolving-door network map as a diagram** (not just text) — this visual is the report's most shareable asset.
3. ** [P1] Add "Contacted for Comment" / "No Harm Occurred" defenses** to Chapter 1.
4. ** [P1] Fill the missing Annexure D** or remove its citation.
5. ** [P1] Create the website chapter pages with the updated markdown** — the site currently has a static snapshot that needs re-sync.
6. ** [P2] Add the ₹3.9 Cr → contract value comparison** to §1.2.
7. ** [P2] Backfill the parenthetical acronym expansions** in the executive summary and chapter intros.

---

## Process Note

This review was conducted as an adversarial edit: assuming the worst possible reader (an IDRBT/RBI spokesperson, a skeptical journalist, a CIC member evaluating an RTI appeal). Every weakness identified is an attack surface that can be closed before publication. The strongest feature of the report is its source grading system — it is the reason the report should be taken seriously despite the 🔴 allegations.
