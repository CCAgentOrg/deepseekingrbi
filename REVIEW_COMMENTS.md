# Adversarial Review: DeepSeeking Accountability in RBI

> **Date**: 2026-07-19  
> **Role**: Adversarial editor — find what's weak, what's missing, what could be attacked by a critical reader or by the institutions under scrutiny.

---

## Status Dashboard

| # | Issue | Status | Details |
|---|-------|--------|---------|
| C1 | Overuse of insider shorthand | ✅ **Done** | Executive summary + chapter intros now gloss acronyms on first use |
| C2 | Audience framing | ✅ **Done** | "Why This Report Exists" section added at line 14 |
| C3 | Source markers inconsistent | ✅ **Done** | Security breach data (33 APIs, 5,576 records) now cited on every relevant paragraph. The Register added as [^20] |
| C4 | "if true" / confidence qualifier | ✅ **Done** | Exec summary accurately hedged; byelaw allegation noted as 🔴 |
| C5 | Named entity disclosure | ✅ **Done** | "Contacted for Comment" section added to §1.3 |
| C6 | Visual navigability (diagram) | ⏳ **Open** | Ch2 has a text diagram. Network graph still needs a shareable D2 diagram. See P0 |
| 1.1 | Exposure window / harm framing | ✅ **Done** | "13+ months" and "Every Indian bank's domain registrar" framing added |
| 1.2 | IKCON revenue gap / contract value | ✅ **Done** | "Revenue vs. contract value" section with GFR ₹25L benchmark added. Track record explainer added |
| 1.3 | Deepak timeline caveat | ✅ **Done** | Acknowledged in §1.7 defense response |
| 1.3 | Mahesh motivation analysis | ✅ **Done** | **Possible motivations** block with equity, domain continuity, benign interpretations |
| 1.4 | GC meeting timing / 79th meeting gap | ✅ **Done** | 79th meeting gap analysis added |
| 1.4 | Threshold ambiguity (GFR comparison) | ✅ **Done** | GFR 2024 ₹25 lakhs benchmark added |
| 1.5 | CAG exemption / legal provision | ✅ **Done** | Section 19 of CAG Act, 1971 + AP Societies Act analysis |
| 1.5 | RTI exemption / Annexure D | ✅ **Resolved** | "Annexure D" not present in chapter — was never an existing ref. Reference matrix linked instead |
| 1.6 | Counter-argument A stronger response | ✅ **Done** | "Why hasn't IDRBT published the single-source justification?" question added |
| 1.6 | Counter-arg C capacity analysis | ✅ **Done** | 22 employees / operations team size analysis added |
| 1.7 | "No harm occurred" defense | ✅ **Done** | Directly addressed in defense responses |
| 1.7 | External researchers / SOC failure | ✅ **Done** | Added to "Patched within 17 days" defense |
| 1.8 | "Guardians" cross-source | ✅ **Done** | The Register (June 2026) added as [^20]; webhosting.today already [^19] |
| 1.8 | "What Would Upgrade" column | ❌ **Open** | Remaining — good to add but low priority |
| P0 | RTI applications | ❌ **Open** | Not yet drafted. Template needed |
| P0 | Revolving door network diagram | ⏳ **Open** | Text diagram exists; dedicated D2/image asset needed |
| P1 | Annexure D | ✅ **Resolved** | Not present in chapter |
| P1 | Website chapter pages re-sync | ✅ **Done** | CSS fixed, paths corrected, site live at deepseekingrbi.cashlessconsumer.in |
| P2 | Revenue comparison | ✅ **Done** | GFR benchmark + contract value estimate added |
| P2 | Acronym expansions | ✅ **Done** | Parenthetical expansions added |

---

## Cross-Cutting Issues

### 1. ✅ Overuse of insider shorthand
**Status: Fixed.** Executive summary and chapter intros now gloss each acronym on first use ("Reserve Bank Information Technology Private Limited", etc.). Remaining risk: some paragraph-level references may still assume reader familiarity.

### 2. ✅ No "audience" framing
**Status: Fixed.** "Why This Report Exists" section added directly after the executive summary, identifying three audiences (journalists, policy advocates, general public) with what each should expect.

### 3. ✅ Source markers in body text
**Status: Mostly fixed.** The security breach data (33 APIs, 5,576 records, 1,072 orphans) is now cited [^1] on every paragraph where it appears. The Register article (June 2026) added as [^20], cited alongside the no-tender finding. Still audit the full document for orphan claims missing footnotes.

### 4. ✅ "If true" / confidence qualifier
**Status: Fixed.** Executive summary correctly limits itself to confirmed facts and identifies the byelaw amendment as allegation-grade. The exec summary does not overstate.

### 5. ✅ Named entity disclosure
**Status: Fixed.** "Contacted for Comment" section added to §1.3 documenting outreach attempts to IDRBT and IKCON, with explanation of why Deepak Kumar and Mahesh Jarati were not directly contacted.

### 6. ⏳ Visual navigability
**Status: Text diagram exists in Chapter 2 but no renderable network graph.** Priority item for the website — a D2 diagram visualizing the revolving-door connections would be the most shareable asset of the report.

---

## Chapter 1: The IKCON Award

### ✅§1.1 The Contract
- Exposure window: Added "13+ months before discovery". ✅
- Harm framing: Added "the digital equivalent of controlling the registrar for `.gov.in`". ✅
- Orphan Super Admin accounts: Added context about permission hygiene failure. ✅

### ✅§1.2 The Vendor
- Revenue gap: Added GFR comparison (₹25 lakhs threshold for government entities) and contract value estimate (₹50 lakh–₹2 Cr annually for comparable registrar SaaS). ✅
- Track record: Added explainer on what running a TLD registry requires (DNSSEC, CA integration, registrar infrastructure, 24/7 uptime). ✅

### ✅§1.3 Key Actors
- Deepak Kumar timeline: Contract predates him; acknowledged in §1.7. ✅
- Mahesh Caveat: Elevated with explicit **Confidence note** box. ✅
- Motivation analysis: **Possible motivations** block added with four hypotheses, including benign interpretation. ✅

### ✅§1.4 Byelaw Amendment
- 79th meeting gap: Explicit question added about what changed between 79th and 80th meetings. ✅
- Threshold ambiguity: GFR 2024 ₹25 lakhs benchmark added for context. ✅

### ✅§1.5 Safeguards That Failed
- CAG exemption: Legal mechanism precisely documented (Section 19 CAG Act + AP Societies Registration Act, 1350 Fasli). ✅
- RTI exemption: Reference matrix linked; "Annexure D" not present. ✅

### ✅§1.6 Alternate Explanations
- Counter-arg A: Added piercing question about IDRBT's failure to publish single-source justification. ✅
- Counter-arg C: Bolstered with personnel comparison (22 IKCON accounts vs. 8-12 typical ops team for a TLD registry). ✅

### ✅§1.7 Responses to Likely Defenses
- "Patched within 17 days": Added SOC failure point. ✅
- "No harm occurred": New defense pre-emptively addressed. ✅
- Missing defenses: All major likely defenses now covered. ✅

### ❌§1.8 Source Grading
- "What Would Upgrade the 🔴 Claims" column: Not yet added. Consider adding a fourth column to the source grading table indicating what evidence would upgrade each 🔴 claim.

---

## Status Summary

| Bucket | Count |
|--------|-------|
| ✅ Done | 22 |
| ⏳ Open (in progress) | 2 |
| ❌ Open (not started) | 2 |

## Priority Next Steps

1. ** [P0] RTI applications** — Draft and file the three recommended RTI applications (procurement byelaws, 79th/80th GC meeting minutes, single-source award justification)
2. ** [P0] Revolving-door network diagram** — Generate a D2 diagram from the text map in §2.3, upload as asset, embed on website
3. ** [P1] "What Would Upgrade" column** — Add to §1.8 source grading table
4. ** [P2] Full document footnote audit** — Ensure every factual claim in Chapters 2-3 has a source marker

---

## Process Note

This review was conducted as an adversarial edit: assuming the worst possible reader (an IDRBT/RBI spokesperson, a skeptical journalist, a CIC member evaluating an RTI appeal). Every weakness identified is an attack surface that can be closed before publication. The strongest feature of the report is its source grading system — it is the reason the report should be taken seriously despite the 🔴 allegations.
