# Transparency & Accountability Matrix: RBI's IT Arms

> **Frame**: A governance entity is only as accountable as its transparency architecture. This chapter maps every IT/technology entity under RBI's control along nine dimensions of accountability — scoring what's public, what's hidden, and the legal mechanism that enables the opacity. The result is a systemic map of where governance works, where it's bypassed, and how the bypass is structurally engineered.

---

## 1. The Analytical Frame: 9 Dimensions of Accountability

We evaluate each entity across nine distinct governance axes:

| # | Dimension | What It Measures | Why It Matters |
|---|-----------|-----------------|----------------|
| **1** | **Legal Structure** | Statutory form (Society, Section 8, Pvt Ltd, Internal Dept) | Determines which oversight laws apply by default |
| **2** | **RTI Coverage** | Whether the Right to Information Act, 2005 applies | Citizen's ability to demand records, procurement decisions, board minutes |
| **3** | **CAG Audit** | Whether Comptroller & Auditor General has audit mandate | Independent audit of financial propriety, not self-reported |
| **4** | **Board Independence** | Ratio of independent (non-RBI/non-network) directors to total | Prevents regulatory capture via personnel |
| **5** | **MCA/ROC Transparency** | Whether annual filings, board composition, financials are publicly accessible | Enables third-party research, media scrutiny, competitive comparison |
| **6** | **Procurement Governance** | Whether GFR or equivalent competitive-bidding rules apply | Prevents single-source awards, enables vendor competition |
| **7** | **Parliamentary Oversight** | Whether entity can be questioned in Parliament | Democratic accountability for use of public power |
| **8** | **Conflict-of- Interest Regime** | Whether directors' cross-holdings, vendor links, prior roles are publicly disclosed | Detects revolving-door conflicts before they produce governance failures |
| **9** | **Security & Disclosure** | Whether VAPT reports, breach disclosures, security.txt exist | Public confidence in infrastructure security; responsible disclosure culture |

---

## 2. The Entities Evaluated

### 2.1 IDRBT — Institute for Development and Research in Banking Technology

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Society** under Societies Registration Act, 1860 | Colonial-era statute designed for literary/scientific clubs, not critical national infrastructure | ❌ Opaque |
| **RTI Coverage** | **Disputed/exempted** — claims RTI does not apply as it's not a "public authority" under Section 2(h) | CIC rulings have brought similar RBI-controlled societies under RTI, but IDRBT resists | ❌ Denied |
| **CAG Audit** | **Not applicable** — CAG can audit RBI but not its societies | No statutory audit mechanism; annual reports are internal | ❌ Absent |
| **Board Independence** | **Zero independent directors** — Governing Council is all RBI/network insiders chaired by former RBI Deputy Governor N.S. Vishwanathan | Governing Council includes: IDRBT Director (Deepak Kumar — oversees himself), NPCI nominees, former RBI officials | ❌ Captive |
| **MCA/ROC Transparency** | **Not applicable** — Societies do not file with MCA | No DIN numbers, no annual returns, no public financials | ❌ None |
| **Procurement Governance** | **Internal Purchase Manual** — not GFR; thresholds can be amended by Governing Council without external approval | Byelaw amendment allegation (see Chapter 1) — single-source thresholds raised to enable IKCON award | ⚠️ Weak |
| **Parliamentary Oversight** | **Indirect only** — questions can be routed through RBI's own oversight in Parliament | RBI answers Finance Ministry questions; IDRBT-specific questions may be directed | ⚠️ Indirect |
| **Conflict-of-Interest Regime** | **None public** — no published register; multiple directorships held simultaneously without disclosure | Deepak Kumar simultaneously on IDRBT GC, IFTAS board, ReBIT board, RBIH council, NPCI board, IOB board | ❌ Absent |
| **Security & Disclosure** | **No security.txt, no VDP, no published audit** — proven by 33+ unauthenticated API endpoints and 5,576 exposed records | Live-for-years portal with no security.txt or disclosure channel | ❌ Absent |

**Overall Score**: 0.5 / 9 ✅ functioning — Score worsens further if examined by materiality of hidden dimensions.

### 2.2 IFTAS — Indian Financial Technology and Allied Services

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Section 8 Company** (Not-for-Profit) | Filed under Companies Act, so MCA filings are public — but no statutory oversight beyond ROC | ⚠️ Partial |
| **RTI Coverage** | **Does not apply** — Section 8 company, not a government entity; claimed as "owned by member banks" (though RBI is the sole effective controller post-2019) | RTI Act Section 2(h) does not cover companies not substantially funded by government | ❌ Denied |
| **CAG Audit** | **Not applicable** — no statutory mandate for Section 8 companies | RBI acquired IFTAS in 2019 but did not bring it under CAG purview | ❌ Absent |
| **Board Independence** | **All RBI/network appointees** — chair is RBI ED, members are current/former RBI officials | Deepak Kumar sits on IFTAS board while also being IDRBT Director — the entity that gave away its infrastructure to IFTAS | ❌ Captive |
| **MCA/ROC Transparency** | **Partial** — financials are filed (FY24 revenue ~₹455 crore, profit ~₹5.9 crore) | Annual returns available on Tofler/Tracxn/CompanyCheck but board minutes are not public | ⚠️ Partial |
| **Procurement Governance** | **Internal policies** — not subject to GFR | Cooperative bank technology procurement decisions made internally | ⚠️ Weak |
| **Parliamentary Oversight** | **None direct** — Section 8 company, no parliamentary accountability | Questions about IFTAS can only reach Parliament if routed through RBI's ownership disclosure | ❌ Absent |
| **Conflict-of-Interest Regime** | **None public** — MCA filings show directors but no register of interests | Cross-directorships between IFTAS, IDRBT, ReBIT not disclosed as conflicts | ❌ Absent |
| **Security & Disclosure** | **Unknown** — no public VAPT reports, no breach disclosures | IFTAS's systems (INFINET, SFMS) are not independently audited for security on a published schedule | ⚠️ Unknown |

**Overall Score**: 2 / 9

### 2.3 ReBIT — Reserve Bank Information Technology Private Limited

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Private Limited Company** | Filed under Companies Act; MCA filings are technically public but many details are not | ⚠️ Partial |
| **RTI Coverage** | **Does not apply** — Pvt Ltd company, no RTI | RBI's wholly owned cybersecurity subsidiary cannot be questioned by citizens | ❌ Denied |
| **CAG Audit** | **Not applicable** — RBI's 100% subsidiary but not a government company under CAG Act | Pvt Ltd status exempts it from CAG | ❌ Absent |
| **Board Independence** | **RBI-appointed directors** — no public list of independent vs. nominee directors | Board structure not published on website; ROC filings show RBI nominees | ❌ Captive |
| **MCA/ROC Transparency** | **Low** — financials filed but board composition, remuneration, related-party transactions are limited | Pvt Ltd has fewer disclosure requirements than listed companies | ⚠️ Low |
| **Procurement Governance** | **Internal** — ReBIT handles IT procurement for RBI systems | No public procurement policy or tender archive | ❌ Opaque |
| **Parliamentary Oversight** | **None direct** | RBI may answer questions about "use of ReBIT" but ReBIT itself is not accountable | ❌ Absent |
| **Conflict-of-Interest Regime** | **None public** | Deepak Kumar on ReBIT board while also being IDRBT Director — potential conflict between infrastructure builder and security auditor | ❌ Absent |
| **Security & Disclosure** | **Unknown** — ReBIT's own systems vulnerability posture is not public | Irony: the entity responsible for cybersecurity of RBI systems is itself opaque on security governance | ⚠️ Unknown |

**Overall Score**: 1.5 / 9

### 2.4 RBIH — RBI Innovation Hub

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Section 8 Company** | Incorporated under Companies Act, 2013 | ⚠️ Partial |
| **RTI Coverage** | **Does not apply** | Section 8 company with no government funding designation | ❌ Denied |
| **CAG Audit** | **Not applicable** | No statutory mandate | ❌ Absent |
| **Board Independence** | **Mixed** — independent chair (Kris Gopalakrishnan, Infosys co-founder) but board includes RBI EDs and IDRBT officials | RBIH Governing Council has more external representation than other entities, but operational board may be different | ⚠️ Mixed |
| **MCA/ROC Transparency** | **Partial** — Section 8 company filings are public | Financials trackable; board composition on MCA | ⚠️ Partial |
| **Procurement Governance** | **Unknown** | No published procurement policy | ❌ Opaque |
| **Parliamentary Oversight** | **None** | Unlikely to be considered a government entity | ❌ Absent |
| **Conflict-of-Interest Regime** | **None public** | No published register | ❌ Absent |
| **Security & Disclosure** | **Unknown** | No public posture | ⚠️ Unknown |

**Overall Score**: 2.5 / 9 — Still weak but marginally better due to independent chair.

### 2.5 NPCI — National Payments Corporation of India

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Section 8 Company** (pending conversion to for-profit) | 65 member banks; Section 8 not-for-profit status debated since 2023 | ⚠️ Transitioning |
| **RTI Coverage** | **Does not apply** — NPCI is not a government entity per CIC rulings | Multiple RTI applications rejected on grounds NPCI is not a "public authority" | ❌ Denied |
| **CAG Audit** | **Not applicable** | Despite managing India's most critical payments infrastructure (UPI, RuPay, IMPS, NACH, BBPS) | ❌ Absent |
| **Board Independence** | **Member-bank nominees** — board elected by 65 member banks, but RBI holds significant influence | Deepak Kumar also on NPCI board — cross-directorship between operator and regulator's technology arm | ⚠️ Member-controlled |
| **MCA/ROC Transparency** | **Section 8 filings are public** — financials available | FY25 surplus ₹1,552 crore publicly reported | ✅ Public |
| **Procurement Governance** | **Internal** — MDR-based revenue model, not GFR | Technology procurement for UPI/RuPay infrastructure is internal | ⚠️ Internal |
| **Parliamentary Oversight** | **None direct** — Parliament can ask RBI about NPCI's regulatory oversight but not NPCI directly | As payments infrastructure becomes more critical, this gap grows | ❌ Absent |
| **Conflict-of-Interest Regime** | **None public** — no published register of directors' cross-holdings | With for-profit conversion, conflicts will become material | ❌ Absent |
| **Security & Disclosure** | **Periodic VAPT** — UPI/RuPay security posture is tested but details not public | No public transparency on vulnerability management | ⚠️ Partial |

**Overall Score**: 3 / 9 — Best of the group but still fails 6 of 9 dimensions.

### 2.6 RBI IT Department (Internal)

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Internal RBI department** | Part of RBI's own organisational structure | ⚠️ Internal |
| **RTI Coverage** | **✅ Applies** — RBI is a public authority under RTI Act | RTI can be filed for IT Department decisions, procurement, policies | ✅ Covers |
| **CAG Audit** | **✅ Applies** — RBI's accounts, including IT Dept spending, are CAG-audited | CAG audits RBI annually and reports to Parliament | ✅ Covers |
| **Board Independence** | **N/A** — internal department, no board | Reports through RBI's hierarchy | ⚠️ Internal |
| **MCA/ROC Transparency** | **N/A** — internal department | Not a separate legal entity | — |
| **Procurement Governance** | **✅ GFR applies** — RBI follows General Financial Rules for its own procurement | IT Department procurement is subject to GFR, CVC oversight, CAG audit | ✅ Governed |
| **Parliamentary Oversight** | **✅ Applies** — Finance Ministry answers for RBI in Parliament | Questions can be raised about RBI's IT systems, procurement | ✅ Covers |
| **Conflict-of-Interest Regime** | **RBI's internal code** — not public | Not comprehensive; no public register | ⚠️ Weak |
| **Security & Disclosure** | **Internal** — no public VAPT reports | RBI's internal IT security posture is not public | ❌ Opaque |

**Overall Score**: 5.5 / 9 — Strongest on paper, but procurement and security details are not effectively public.

### 2.7 RBI Fintech Department (Internal)

| Dimension | Status | Mechanism | Score |
|-----------|--------|-----------|-------|
| **Legal Structure** | **Internal RBI department** | Established January 2022, subsumed fintech unit of DPSS | ⚠️ Internal |
| **RTI Coverage** | **✅ Applies** | Same as RBI — public authority | ✅ Covers |
| **CAG Audit** | **✅ Applies** | Part of RBI's accounts | ✅ Covers |
| **Board Independence** | **N/A** | No board | — |
| **MCA/ROC Transparency** | **N/A** | Internal | — |
| **Procurement Governance** | **✅ GFR applies** | Same as RBI | ✅ Governed |
| **Parliamentary Oversight** | **✅ Applies** | Same as RBI | ✅ Covers |
| **Conflict-of-Interest Regime** | **Same as RBI code** | Not public | ⚠️ Weak |
| **Security & Disclosure** | **Internal** | No public posture | ❌ Opaque |

**Overall Score**: 5.5 / 9 — But note: its existence creates mandate overlap with RBIH (external, not accountable) creating an **accountability arbitrage channel**: functions can be moved between the transparent internal department and the opaque external Section 8 entity at will.

---

## 3. The Systemic Pattern: What's Missing Everywhere

### 3.1 The Accountability Gap: Internal vs External

```
                        HIGH ACCOUNTABILITY                LOW ACCOUNTABILITY
                        (Internal RBI Depts)              (External Entities)
                        ┌─────────────────────────────────────────────────┐
  RTI Coverage          │  ✅ Applies                 ❌ All denied       │
  CAG Audit             │  ✅ Applies                 ❌ None covered     │
  Parliamentary Qs      │  ✅ Possible                ❌ Not possible      │
  Procurement Oversight │  ✅ GFR + CVC               ❌ Internal manual   │
  Independent Board     │  N/A (internal)             ❌ Captive boards    │
  Public Financials     │  ⚠️ Part of RBI accounts    ⚠️ Minimal (ROC)    │
  Conflict-of-Interest  │  ⚠️ Internal code           ❌ None public       │
                        └─────────────────────────────────────────────────┘
```

The governance architecture is **two-tiered**: functions that stay inside RBI are subject to RTI, CAG, GFR, and parliamentary scrutiny. Functions that are spun off to external entities (IDRBT, IFTAS, ReBIT, RBIH, NPCI) lose all four protections simultaneously.

### 3.2 What None of the 7 Entities Has

| Missing Feature | Count | Entities |
|----------------|-------|----------|
| Public conflict-of-interest register | **0/7** | None maintain a published register of directors' cross-holdings, vendor links, or prior roles |
| Published board minutes | **0/7** | No entity publishes minutes of board/governing council meetings |
| Publicly accessible whistleblower channel | **0/7** | No entity has a documented, anonymous whistleblower mechanism |
| External (non-RBI-network) director majority | **0/7** | No entity has a majority of independent directors |
| Mandatory CAG audit | **0/7 external** | No external entity is subject to CAG audit |
| Published security audit / VAPT report | **0/7** | No entity publishes security audit results voluntarily |
| RTI applicability | **0/5 external** | No external entity accepts RTI; only internal departments do |
| Mandatory competitive procurement (GFR) | **0/5 external** | No external entity follows GFR; all have internal purchase manuals |

**Zero out of seven** across every external accountability dimension.

### 3.3 The Accountability Arbitrage Channel

The **most dangerous governance feature** is the ability to move a function between internal department and external entity — and thereby switch its accountability regime on or off.

**Example**: RBI Fintech Department (internal, RTI-applicable, CAG-audited) and RBIH (external Section 8, no RTI, no CAG) have overlapping mandates. If a politically sensitive fintech initiative needs to avoid scrutiny, it can be routed through RBIH rather than the Fintech Department. If a procurement decision needs to avoid GFR, it can be routed through IDRBT rather than RBI's IT Department.

**This is not hypothetical**: The `.bank.in` domain registry — a regulatory mandate affecting every bank in India — was assigned to IDRBT (a Society, no RTI, no CAG, no GFR) instead of RBI's IT Department (RTI-applicable, CAG-audited, GFR-governed). The choice of entity was a **choice of accountability regime**.

---

## 4. The Comparative Scorecard

| Entity | Legal Form | RTI | CAG | Board Indep. | MCA Public | Procurement | Parliament | COI Register | Security | **Score** |
|--------|-----------|:---:|:---:|:------------:|:----------:|:-----------:|:----------:|:------------:|:--------:|:---------:|
| IDRBT | Society | ❌ | ❌ | ❌ | ❌ N/A | ⚠️ | ⚠️ | ❌ | ❌ | **0.5/9** |
| IFTAS | Sec 8 | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ⚠️ | **2/9** |
| ReBIT | Pvt Ltd | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | **1.5/9** |
| RBIH | Sec 8 | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | **2.5/9** |
| NPCI | Sec 8 | ❌ | ❌ | ⚠️ | ✅ | ⚠️ | ❌ | ❌ | ⚠️ | **3/9** |
| RBI IT Dept | Internal | ✅ | ✅ | N/A | N/A | ✅ | ✅ | ⚠️ | ❌ | **5.5/9** |
| RBI Fintech | Internal | ✅ | ✅ | N/A | N/A | ✅ | ✅ | ⚠️ | ❌ | **5.5/9** |

---

## 5. Key Findings

1. **Internal departments are accountable; external entities are not.** The decision to structure a function as an internal department vs external entity is the single most important governance choice — and it's entirely at RBI's discretion, with no external check on that choice.

2. **Zero external entities pass any transparency test.** Not one of IDRBT, IFTAS, ReBIT, RBIH, or NPCI — entities that collectively manage India's entire payments, banking technology, and cybersecurity infrastructure — has RTI coverage, CAG audit, independent board, public COI register, or published board minutes.

3. **Board independence is the weakest dimension across all entities.** All external entities have boards composed entirely of RBI/network insiders or member-bank nominees. No entity has a majority of directors who have never worked at RBI or one of its regulated entities.

4. **The accountability arbitrage channel is real and operational.** RBI can move any function between transparent internal departments and opaque external entities without legislation, without parliamentary approval, and without public consultation. The `.bank.in` registry placement in IDRBT (not RBI's IT Dept) is evidence that this channel is used.

5. **Procurement bypass is structural, not incidental.** Every external entity has an internal purchase manual instead of GFR, and every internal purchase manual can be amended by that entity's board without external approval. The IKCON single-source award is not a one-off violation — it's the predictable output of a procurement governance regime designed to permit it.

6. **Security opacity is universal.** No entity publishes security audit results, VAPT reports, vulnerability disclosure policies, or transparency reports. The `.bank.in` breach was discovered by external researchers, not through any internal security governance mechanism.

---

## 6. What Reform Would Require

To close every gap identified in this matrix:

| Reform | What It Would Require | Which Entities |
|--------|----------------------|----------------|
| **Statutory conversion** | IDRBT → statutory corporation (like NABARD) under RBI Act | IDRBT |
| **RTI notification** | Central Government notification under RTI Act Sec 2(h) bringing all entities managing national financial infrastructure under RTI | All 5 external entities |
| **CAG audit mandate** | Amendment to CAG Act or Government directive on RBI's subsidiaries | All 5 external entities |
| **Independent director mandate** | RBI Board directive requiring majority independent (non-RBI/non-network) directors on each entity's board | All 5 external entities |
| **Mandatory GFR procurement** | RBI circular requiring GFR compliance for all contracts above ₹25 lakh across its entities | All 5 external entities |
| **Mandatory security disclosure** | CERT-In directive requiring published VAPT reports for all entities managing national financial infrastructure | All 5 external + RBI IT |
| **COI register** | RBI Board directive requiring public annual conflict-of-interest filings from all directors of its entities | All 5 external entities |
| **Whistleblower mechanism** | Mandatory board-approved whistleblower policy with annual public attestation | All entities |

---

## References

[^1]: Medianama, June 2026 — .bank.in security vulnerabilities report. (https://www.medianama.com/2026/06/223-security-vulnerabilities-rbi-bank-in-registry-sensitive-data)
[^2]: IDRBT Governing Council page — Lists members, notes RBI/nominee composition. (https://www.idrbt.ac.in/governing-council/)
[^3]: IDRBT Director page — Deepak Kumar concurrent directorships listed. (https://www.idrbt.ac.in/director/)
[^4]: TheCompanyCheck — IFTAS financials FY2024, revenue ₹455 crore approx. (https://www.thecompanycheck.com/company/indian-financial-technology-and-allied-services/U74900TG2015NPL097485)
[^5]: RBI Organisational Structure page — Lists own departments, subsidiaries, training colleges. (https://www.rbi.org.in/commonman/English/Scripts/Organisation.aspx)
[^6]: RBI Press Release PRID=50666 — RBIH Governing Council announcement, includes members. (https://www.rbi.org.in/scripts/FS_PressRelease.aspx?fn=9&prid=50666)
[^7]: IDRBT "The Journey of IDRBT" — Documents IFTAS creation, INFINET/SFMS transfer. (https://www.idrbt.ac.in/the-journey-of-idrbt/)
[^8]: Medianama — RBI Fintech Department established Jan 2022. (https://www.medianama.com/2022/01/223-rbi-fintech-department-established/)
[^9]: RBI Fintech Department overview. (https://rbi.org.in/scripts/FS_Overview.aspx?fn=2765)
[^10]: NPCI FY25 financial results — Surplus ₹1,552 crore. (https://entrackr.com/fintrackr/npci-profit-jumps-42-to-rs-1552-cr-in-fy25-9408857)
[^11]: NPCI Section 8 to for-profit conversion debate. (https://www.sanskritiias.com/current-affairs/npci-from-not-for-profit-to-for-profit)
[^12]: RBI Information Technology Governance Master Directions, 2023. (https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=12562)
[^13]: IDRBT Former Directors page — Nikhila 3-month tenure documented. (https://www.idrbt.ac.in/former-directors/)
[^14]: IDRBT procurement manual — ITVM_Final.pdf. (https://www.idrbt.ac.in/wp-content/uploads/2022/07/ITVM_Final.pdf)
[^15]: TheCompanyCheck — ReBIT financials, board structure (Pvt Ltd). (https://www.thecompanycheck.com/company/reserve-bank-information-technology-private-limited/U72200MH2016PTC283203)
[^16]: Medianama — RBI forced NPCI to hire government-favoured CEO, 2018. (https://www.medianama.com/2018/02/223-rbi-forced-national-payments-body-hire-government-favourite-ceo)
[^17]: Tofler — IFTAS director list and financial summary. (https://www.tofler.in/indian-financial-technology-and-allied-services/company/U74900TG2015NPL097485)
[^18]: TheCompanyCheck — RBIH financials, Section 8 status. (https://www.thecompanycheck.com/company/rbi-innovation-hub-private-limited/U72200KA2022NPL162715)

---

*This chapter is part of the **DeepSeeking Accountability in RBI** report. See `file AGENTS.md` for project structure, `file chapters/rbi_governance.md` for the main report, and `file annexures/reference-matrix.md` for detailed source grading.*
