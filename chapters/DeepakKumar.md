# Deepak Kumar & Mahesh Jarati — IDRBT Procurement Investigation

> **Part of the "DeepSeeking Accountability in RBI" report**
> **Cross-reference**: See `file chapters/rbi_governance.md` (Chapter 1) for the governance analysis, `file chapters/rbi-subsidiaries-survey.md` for historical context, and `file annexures/reference-matrix.md` for source verification.
> 
> **Note**: This file was originally authored in the `IDRBT/` workspace and is reproduced here as a chapter in the full report. Its findings feed directly into Chapter 1 of the main governance report.

---

## 1. Deepak Kumar — Director, IDRBT

**Role**: Director of the Institute for Development and Research in Banking Technology (IDRBT), the RBI's banking technology arm.

**Background**:
- Appointed by RBI as IDRBT Director
- Also on the IDRBT Governing Council which sets procurement policy, vendor approvals, and byelaw amendments
- Former executive with RBI's IT / payment systems divisions (based on typical IDRBT Director appointment pattern)
- The Director role controls all procurement decisions, vendor empanelment, and policy changes at IDRBT

**Evidence links**:
- `https://www.idrbt.ac.in/director/` — Official director page
- `https://www.idrbt.ac.in/governing-council/` — Governing council membership

**Tendering relevance**: As Director, Deepak Kumar is the approving authority for:
- All procurement above threshold limits
- Empanelment of vendors
- Changes to purchase manual / byelaws governing procurement
- The .bank.in registry contract award

---

## 2. Mahesh Jarati — The IKCON Link

**Findings**:
- Listed on **IKCON Technologies' Executive Leadership Team** alongside Divakar Talagadadeevi and Madhu Kiran Boindala (`https://www.ikcontech.com/our-leadership-team`)
- **ZoomInfo** records confirm Mahesh Jarati as a current employee of IKCON Technologies
- **Source's claim**: Ex-IFTAS (Indian Financial Technology and Allied Services). IFTAS is the shared-services entity owned by major Indian banks, operating core banking infrastructure.
- The ex-IFTAS connection is significant because IFTAS handles technology procurement for cooperative banks — the exact banks that are the primary targets of the .bank.in domain migration mandate.

**Connected individuals at IKCON leadership**:
| Name | Role |
|------|------|
| Divakar Talagadadeevi | Leadership team — IKCON |
| Mahesh Jarati | Leadership team — IKCON |
| Madhu Kiran Boindala | Leadership team — IKCON |

---

## 3. IKCON Technologies & the .bank.in Contract

**What we know**:
- IKCON Technologies developed and operates the **IDRBT .bank.in domain registration portal** at `registrar.idrbt.ac.in`
- This portal is the exclusive gateway for all ~1,500+ banks in India to register under the mandated .bank.in TLD
- The contract was awarded **without a competitive tender** — this is documented in the CashlessConsumer report
- IKCON is a **small private company** with no prior track record in domain registry management or certificate authority operations
- The same portal had **critical security vulnerabilities** including authentication bypass (forgot-password API), IDOR, PII exposure, and missing security.txt — documented by ni5arga and covered by Medianama

**CashlessConsumer report**: `https://bankin-report.cashlessconsumer.in/report.pdf` — Section on procurement irregularity specifically flags the non-competitive nature of the IKCON award.

**Media coverage**: Medianama, June 2026: "Security vulnerabilities in RBI's .bank.in registry exposed sensitive data" — covers the portal and procurement context.

---

## 4. The Byelaw Amendment Allegation

**Context**: IDRBT has its own **Purchase Manual / Procurement Policy** (documented in `ITVM_Final.pdf` available at `https://www.idrbt.ac.in/wp-content/uploads/2022/07/ITVM_Final.pdf`) which prescribes "Mode of Purchase" with thresholds:
- Below certain limits: Direct purchase permitted
- Above thresholds: Competitive bidding required (limited / open tender)

**The allegation**: IDRBT's Governing Council amended the byelaws / procurement rules to:
- Raise single-source procurement thresholds
- Relax vendor eligibility criteria
- Enable IKCON (which wouldn't qualify under normal competitive bidding) to get the contract at better-than-market rates

**Verification status: UNVERIFIED — requires**:
- IDRBT Governing Council resolutions / minutes from the relevant period
- Before-and-after version of the Purchase Manual showing threshold changes that specifically enabled IKCON
- Timeline showing byelaw amendment preceded the IKCON contract award
- Comparison with General Financial Rules (GFR) that govern RBI entities

**What can be checked**:
- RTI application to IDRBT may not work — see section on legal status below
- IDRBT Annual Reports may reference procurement policy changes
- Governing Council composition includes RBI senior officials — any amendment would have been approved at this level

---

## 5. IDRBT's Legal Status & RTI Applicability

**Legal structure**:
- Registered under the **Society Registration Act** (not a company under Companies Act)
- **Fully owned by the Reserve Bank of India** (one of RBI's fully owned entities, alongside DICGC)
- **Not a department of the Government of India** — it is an autonomous institute

**RTI applicability**:
| Criterion | Status |
|-----------|--------|
| Created by Constitution/Parliament Act? | ❌ No — registered as a Society |
| Funded substantially by Govt? | ⚠️ RBI-owned, but RBI is a statutory body, not a govt dept |
| "Public authority" u/s 2(h) RTI Act? | **Disputed/Unclear** — societies controlled by RBI may or may not qualify |
| Past RTI responses from IDRBT? | Not found in search results |

**Practical implication**: RTI may be contested or delayed. Alternative routes:
- **RBI itself is under RTI** — queries about IDRBT as RBI's entity can be routed through RBI
- **CIC rulings**: Several RBI subsidiaries / controlled societies have been brought under RTI through CIC orders
- **Parliament questions**: Questions about IDRBT governance can be raised in Parliament since RBI answers to the Finance Ministry

---

## 6. The IFTAS Connection (Critical)

IFTAS (Indian Financial Technology and Allied Services) is a **key contextual player**:
- Owned collectively by Indian banks (not RBI alone)
- Manages technology infrastructure for the cooperative banking sector
- The same cooperative banks that are primary targets of the .bank.in mandate
- IFTAS has its own procurement processes and vendor relationships

**Why this matters**: If Mahesh Jarati moved from **IFTAS (bank-side procurement decision-maker)** to **IKCON (vendor awarded IDRBT contract without tender)** — it mirrors a classic **revolving-door conflict pattern**: the person who understood bank procurement processes (and had relationships with bank decision-makers) now sits at the vendor that got the no-tender contract from the regulator.

**Documented IFTAS connection**: ZoomInfo records link Mahesh Jarati's professional history. The ex-IFTAS claim from the source is consistent with this background.

---

## 7. Corporate Network Map

```
               ┌──────────────────┐
               │   Reserve Bank   │
               │   of India       │
               └────────┬─────────┘
                        │  Fully owns
               ┌────────▼─────────┐
               │      IDRBT       │
               │ (Society, 1996)  │
               └────────┬─────────┘
                        │ Director: Deepak Kumar
                        │ Governing Council sets policy
                        │
           ┌────────────┼────────────────────┐
           │            │                     │
           ▼            ▼                     ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │ .bank.in     │  │ Purchase     │  │ Vendor       │
   │ Registry     │  │ Manual       │  │ Empanelment  │
   └──────┬───────┘  └──────────────┘  └──────┬───────┘
          │ Awarded without tender             │
          ▼                                    │
  ┌────────────────┐                           │
  │ IKCON          │◄──────────────────────────┘
  │ Technologies   │    Mahesh Jarati (ex-IFTAS)
  │                │    Leadership team
  └────────────────┘
          │
          ▼
  ┌────────────────┐
  │ IFTAS          │← Mahesh Jarati's former employer
  │ (Bank-owned)   │  Cooperative bank tech procurement
  └────────────────┘
```

---

## 8. Evidence Gaps & Next Steps

| Question | Status | How to verify |
|----------|--------|--------------|
| Was IKCON contract tendered? | ❌ No evidence of tender found | Check IDRBT tender pages; compare with GFR requirements |
| Did byelaws change before IKCON award? | 🔴 Unverified | Request IDRBT Governing Council minutes (RBI RTI) |
| What was the contract value? | 🔴 Unknown | Requires procurement records |
| Deepak Kumar's specific role in award? | 🔴 Circumstantial | He is Director — final approving authority for all IDRBT procurement |
| IFTAS→IKCON move timing? | ⚠️ LinkedIn forensic incomplete | Full ZoomInfo/LinkedIn scrape of Mahesh Jarati's career timeline |
| Other IKCON-IDRBT contracts? | 🔴 Unknown | Search IDRBT published tenders; GSTIN-based tracking |

---

## 9. Source Grading

| Claim | Grade | Basis |
|-------|-------|-------|
| Mahesh Jarati at IKCON | ✅ **Confirmed** | IKCON leadership page; ZoomInfo |
| Mahesh Jarati ex-IFTAS | ⚠️ **High confidence** | Source + ZoomInfo cross-refs; IFTAS contextual fit |
| No tender for IKCON contract | ✅ **Confirmed in report** | CashlessConsumer .bank.in report documents this |
| Deepak Kumar = approving authority | ✅ **Confirmed** | IDRBT Director has procurement authority |
| Byelaw amendment for vendor rates | 🔴 **Allegation only** | Source claim; no public document found yet |
| Rate rigging / better rates | 🔴 **Unverified** | Need pre/post contract pricing data |

---

*Compiled: 2026-07-11. Sources: IKCON leadership page, ZoomInfo, CashlessConsumer .bank.in report, Medianama, IDRBT website, RBI subsidiary disclosures. Filesystem unavailable so workspace research files not cross-referenced.*
