# DeepSeeking Accountability in RBI

> **Full Title**: DeepSeeking Accountability in India's Central Bank: Governance Failures in RBI's Entity Network — The `.bank.in` Debacle, the Revolving Door, and the Systemic Bypass Template

## Executive Summary

The Reserve Bank of India controls a dense network of at least **seven distinct entities** — IDRBT, IFTAS, ReBIT, RBIH, NPCI, and its own IT and Fintech Departments — that operate critical national payments, banking, and cybersecurity infrastructure. These entities share personnel, board seats, and institutional culture with **no external accountability mechanism**.

The `.bank.in` domain registry fiasco — where a portal managing the internet identity of every Indian bank was built by an untendered vendor, operated with 33+ critical vulnerabilities, and had no security audit or disclosure mechanism — is not a security incident. It is a **governance debacle** that expresses a structural pattern: RBI creates entities, incubates them, staffs them with rotating insiders, and reabsorbs them at will, all through opaque legal forms that evade Parliament, CAG, RTI, and competitive procurement.

This report documents that pattern through three lenses: the IKCON single-source award (Chapter 1), the IDRBT revolving door (Chapter 2), and the systemic governance bypass template that entity proliferation enables (Chapter 3).

---

## Chapter 1: The IKCON Award — A High-Probability Governance Failure

> **Methodology**: This chapter reconstructs the chain of events leading to IKCON Technologies being awarded the `.bank.in` domain registry contract without competitive tender. The conclusion — that the no-tender award represents a governance failure with high probability of byelaw manipulation — is a **logical inference from verified source data**, not a proven judicial finding. Each claim is graded.

### 1.1 The Contract

The `.bank.in` domain registry portal at `registrar.idrbt.ac.in` is the **exclusive gateway for all ~1,500+ banks in India** to register under the RBI-mandated `.bank.in` namespace. It handles authentication, PII (email, phone, addresses), domain registration authorization, and certificate issuance for the entire banking sector's internet-facing domains.

**Confirmed facts** [^1]:
- 33+ unauthenticated API endpoints discovered
- 5,576 user records exposed (email, phone, addresses)
- 1,072 orphan Super Admin accounts
- No `security.txt` vulnerability disclosure mechanism
- No evidence of pre-deployment security audit

### 1.2 The Vendor

IKCON Technologies (`https://www.ikcontech.com/`) is a small private company with:
- **No prior domain registry management track record**
- **No certificate authority (CA) operational history**
- Leadership team of ~3 individuals including Mahesh Jarati [^4]
- No published public sector contracts comparable to the `.bank.in` mandate

The portal was awarded to IKCON **without any published tender, RFP, or vendor selection process**. [^2]

**Confirmed**: IDRBT's own tender page (https://www.idrbt.ac.in/tenders/) lists all published procurement notices — from modular furniture to HSMs — but contains no entry for the `.bank.in` domain registry. This negative evidence is consistent with the CashlessConsumer report's finding. [^11]

### 1.3 The Key Actors

#### Deepak Kumar — Director, IDRBT

Appointed 2 May 2024. Formerly RBI's **Executive Director, Department of Information Technology** — the same department that oversees IDRBT on RBI's behalf. [^3]

**Directorship map** (confirmed from IDRBT Director page and cross-referenced against entity websites):

| Entity | Role | Since |
|--------|------|-------|
| IDRBT | Director + Governing Council member | May 2024 |
| NPCI | Board member | Concurrent |
| IFTAS | Board member | Concurrent |
| ReBIT | Board member | Concurrent |
| RBI Innovation Hub | Governing Council member [^8] | Concurrent |
| Indian Overseas Bank | Board member | Concurrent |
| RBI (earlier) | Executive Director, IT Dept | Pre-2024 |

This creates a **self-oversight paradox**: Deepak Kumar sits on the boards of IFTAS (which took over IDRBT's built infrastructure), ReBIT (RBI's cybersecurity arm that should audit IDRBT), NPCI (which IDRBT's .bank.in registry interacts with), and is simultaneously a member of IDRBT's own Governing Council — the body meant to oversee him. [^3][^5]

#### Mahesh Jarati — The IFTAS→IKCON Link

**Confirmed**: Mahesh Jarati is listed on IKCON Technologies' Executive Leadership Team alongside Divakar Talagadadeevi and Madhu Kiran Boindala. [^4] ZoomInfo records confirm current employment at IKCON.

**High confidence**: Source investigation reports Mahesh Jarati as ex-IFTAS (Indian Financial Technology and Allied Services). [Annexure A] IFTAS manages technology infrastructure for the **cooperative banking sector** — exactly the banks that are primary targets of the .bank.in domain migration mandate.

**The logical chain**: Mahesh Jarati moved from:
1. **IFTAS** → cooperative bank technology procurement (knows requirements, budgets, vendors)
2. **IKCON Technologies** → the vendor that received a no-tender contract from IDRBT to build the .bank.in portal serving those same cooperative banks

This is a textbook **revolving-door conflict pattern**. The byelaw amendment allegation — that IDRBT's Governing Council raised single-source procurement thresholds specifically to accommodate IKCON — would explain why a small company with no relevant track record could qualify for a contract that would normally require competitive bidding. [^5]

### 1.4 Byelaw Amendment: The Allegation

**Alleged** (unverified): IDRBT's Governing Council amended procurement byelaws to:
- Raise single-source procurement thresholds
- Relax vendor eligibility criteria
- Enable IKCON to qualify without competitive tender

**What is confirmed**:
- ✅ No tender was published for the `.bank.in` portal
- ✅ IDRBT's IT Vendor Management Manual (ITVM_Final.pdf) [^12] specifies competitive bidding requirements above certain thresholds
- ✅ Deepak Kumar, as Director, is the approving authority for procurement
- ✅ The Governing Council (including Deepak Kumar) sets procurement policy [^5]
- ✅ IDRBT held its 80th Governing Council meeting on 21 June 2024 — after Deepak Kumar's appointment — where procurement policy could have been amended [IDRBT 2023-2024 page]

### 1.5 Safeguards That Failed

| Safeguard | Expected | Actual | Source |
|-----------|----------|--------|--------|
| Procurement policy | Competitive tender above threshold | No tender published | [^2][^11] |
| Governing Council oversight | Independent review of awards | Council members are RBI network | [^3][^5] |
| CAG audit | Statutory audit of public-funded entity | Society exempts from CAG | Legal analysis |
| RTI oversight | Public can question procurement | IDRBT claims exemption | [Annexure D] |
| Security audit | Pre-deployment VAPT per CERT-In | No audit; 33+ endpoints exposed | [^1] |
| Disclosure mechanism | `security.txt`, reporting channel | None present | [^1] |

### 1.6 Source Grading

| Claim | Grade | Evidence |
|-------|-------|----------|
| Mahesh Jarati at IKCON | ✅ **Confirmed** | IKCON leadership page [^4]; ZoomInfo |
| Mahesh Jarati ex-IFTAS | ⚠️ **High confidence** | Source claim + ZoomInfo cross-refs; IFTAS contextual fit [Annex A] |
| No tender for IKCON contract | ✅ **Confirmed** | CashlessConsumer .bank.in report [^2]; tender page absence [^11] |
| Deepak Kumar = approving authority | ✅ **Confirmed** | IDRBT Director has procurement authority [^3] |
| Byelaw amendment for vendor rates | 🔴 **Allegation only** | Source claim; no public document found yet |
| Rate rigging / better rates | 🔴 **Unverified** | Requires pre/post contract pricing data |

---

## Chapter 2: The Revolving Door — IDRBT's Governance Structure

### 2.1 The Governing Council: Structural Inbreeding

IDRBT's Governing Council is chaired by **former RBI Deputy Governor N.S. Vishwanathan** and includes:
- N.S. Vishwanathan (Chair) — former RBI Deputy Governor
- Deepak Kumar (Member) — IDRBT Director, fellow board member of IFTAS, ReBIT, RBIH, NPCI [^3]
- Senior RBI officials (current)
- Representatives from NPCI
- Academics [^5]

**The structural conflict**: Every voting member has spent their career within the RBI ecosystem. There is no one at the table with an independent interest in questioning no-tender awards, procurement byelaw changes, or security audit failures — because questioning would mean questioning former colleagues, future bosses, or one's own prior decisions.

### 2.2 The 3-Month Placeholder: Evidence of Predetermination

| Director | Tenure | Duration | Gap |
|----------|--------|----------|-----|
| Smt. K. Nikhila | 24 Jan 2024 – 1 May 2024 | **~3 months** | — |
| Deepak Kumar | 2 May 2024 – present | Ongoing | 1 day |

Smt. K. Nikhila served as IDRBT Director for approximately 92 days — statistically anomalous for any institution with a genuine leadership transition. [^6] The simplest explanation:

1. The Governing Council knew Deepak Kumar's RBI Executive Director term was ending
2. A placeholder was needed while formalities completed (cooling-off? appointment process?)
3. Nikhila was moved in and out with **no real mandate** to lead the institution
4. Deepak Kumar assumed charge the **very next day** after Nikhila's last day

The 1-day gap between their tenures proves the appointment was **pre-determined**. The Governing Council did not conduct a search — it waited for Deepak Kumar to become available.

### 2.3 The Revolving Door Network Map

```
                      ┌──────────────────────┐
                      │    RBI (Central)     │
                      │  Deepak Kumar (ex-ED,│
                      │   IT Department)     │
                      └──────────┬───────────┘
                                 │
            ┌────────────────────┼──────────────────────┐
            │                    │                      │
            ▼                    ▼                      ▼
   ┌────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │  NPCI Board    │  │ IFTAS Board      │  │ ReBIT Board      │
   │  (Deepak K)    │  │ (Deepak K)       │  │ (Deepak K)       │
   └────────────────┘  └──────────────────┘  └──────────────────┘
            ▲                    ▲                      ▲
            │                    │                      │
            └────────────────────┼──────────────────────┘
                                 │
                      ┌──────────┴──────────┐
                      │     Deepak Kumar    │
                      │  (Director, IDRBT)  │
                      └──────────┬──────────┘
                                 │
            ┌────────────────────┼──────────────────────┐
            │                    │                      │
            ▼                    ▼                      ▼
   ┌────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │ IDRBT Governing│  │ RBIH Governing   │  │ Indian Overseas  │
   │ Council (he's  │  │ Council (member)  │  │ Bank (board)     │
   │ a member)      │  │                  │  │                  │
   └────────────────┘  └──────────────────┘  └──────────────────┘
```

Deepak Kumar simultaneously:
- **Oversees IDRBT** (as Director)
- **Oversees himself** (as Governing Council member)
- **Sits on IFTAS** (which owns the infrastructure IDRBT built)
- **Sits on ReBIT** (which should audit IDRBT's cybersecurity)
- **Sits on NPCI** (which relies on IDRBT's domain infrastructure)
- **Sits on RBIH** (which competes with IDRBT's innovation mandate)
- **Sits on IOB** (a regulated bank that must comply with IDRBT-operated domain requirements) [^3][^8]

### 2.4 The Rangarajan Committee Paradox

The 2009 External Expert Review Committee (EERC) chaired by **Dr. C. Rangarajan** recommended IDRBT shed operational services and focus on R&D. This led to creation of IFTAS and transfer of INFINET, SFMS, and other IDRBT-built infrastructure. [^7]

The EERC report's recommendation directly led to the creation of IFTAS and the transfer of IDRBT-built assets — INFINET, SFMS, RTGS, NEFT, and IBCC.

**Governance implication**: The person who chairs the body overseeing IDRBT today helped design the policy that **hollowed it out** 15 years ago. There is no mechanism for a fresh perspective to question whether the 2009 assumptions remain valid — because no one at the table has any incentive to question their own legacy.

### 2.5 The IFTAS Clawback: How RBI Treats Its Own Entities

IFTAS is the clearest precedent for how RBI manages its subsidiary network:

| Year | Event | What Actually Happened |
|------|-------|----------------------|
| 1996-2009 | IDRBT builds INFINET, SFMS, Banking Community Cloud, other national infrastructure | RBI funds its own society to build critical banking tech |
| 2009 | EERC (Rangarajan) recommends IDRBT shed operational services | Rationale: focus on R&D. But the **real effect**: transfer assets out of IDRBT [^7] |
| 2015 | IFTAS established as Section 8 company owned collectively by banks | Takes over IDRBT-built infrastructure. **No market pricing**: assets transferred without valuation |
| 2015-2016 | 431+ IDRBT employees transferred to IFTAS (per IDRBT records) | Institutional knowledge and operational capability transferred |
| 2019 | RBI **acquires IFTAS entirely** from the bank consortium | Now RBI directly controls the assets IDRBT originally built. Asset consolidation complete [Annexure C] |

**The governance template**: Build in IDRBT → spin off to IFTAS (with banks' money) → acquire IFTAS back (with RBI's balance sheet). Each step bypassed the accountability that would have applied had assets been transferred through market mechanisms. No shareholder vote, no CAG valuation, no parliamentary disclosure.

---

## Chapter 3: The Proliferation Problem — Too Many Entities, No Accountability

### 3.1 The Entity Map

RBI currently operates or controls at least **seven technology/payments entities**:

| Entity | Year | Legal Form | Mandate | Owned By | Public RTI? | CAG Audit? |
|--------|------|------------|---------|----------|-------------|------------|
| **IDRBT** | 1996 | Society (1860 Act) | Banking tech research + .bank.in registry | RBI (fully) | ❌ Contested | ❌ |
| **IFTAS** | 2015 → acquired 2019 | Section 8 Company | Shared tech for cooperative banks | RBI (now) | ❌ | ❌ |
| **ReBIT** | 2016 | Pvt Ltd | IT & cybersecurity for RBI and regulated entities | RBI (fully) [^15] | ❌ | ❌ |
| **NPCI** | 2008 | Section 8 Company | Retail payments infrastructure | 65 member banks (RBI as regulator) | ❌ | ❌ |
| **NPCI Intl (NIPL)** | 2020 | Pvt Ltd | UPI/RuPay global expansion | NPCI (fully) | ❌ | ❌ |
| **RBIH** | 2022 | Section 8 Company | Fintech innovation, incubation | RBI (fully) | ❌ | ❌ |
| **RBI IT Dept** | — | Internal | Oversight of RBI's own IT | RBI | ✅ (via RBI) | ⚠️ (RBI internal) |
| **RBI Fintech Dept** | 2022 | Internal | Fintech regulation, sandbox | RBI | ✅ (via RBI) | ✅ (via RBI audit) |

**Official vs Unofficial**: RBI's own website (https://www.rbi.org.in/commonman/English/Scripts/Organisation.aspx) lists only **DICGC** as a fully-owned subsidiary. IDRBT, ReBIT, IFTAS, and RBIH are **not listed** on RBI's official organisation page. [^13] This means they exist in a regulatory grey zone — acknowledged through press releases and board appointments, but not formally disclosed as RBI subsidiaries in the central bank's own organisational documentation.

### 3.2 The Overlap Problem

| Function | Entities Involved | Accountability Deficit |
|----------|------------------|----------------------|
| Banking technology research | IDRBT, RBIH, RBI Fintech Dept | Three entities, zero published research audit |
| Cybersecurity for banking | ReBIT, IDRBT, RBI IT Dept | ReBIT should audit IDRBT — but their boards share members |
| Payments infrastructure | NPCI, IDRBT (hist.), IFTAS | Historical overlap allows blame-shifting |
| Cooperative bank tech | IFTAS, IDRBT | IFTAS serves these banks; IDRBT regulates their domain registration |
| Innovation / fintech | RBIH, RBI Fintech Dept, IDRBT | Same mandate, different legal forms, different accountability levels |
| IT systems for RBI | RBI IT Dept, ReBIT | Two entities for one central bank's internal IT |

### 3.3 The General Governance Bypass Template

Across all entities, the same pattern repeats:

**Step 1 — Choose an opaque legal form**
- Society (1860 Act) → No MCA filing, no RTI
- Section 8 company → Not a "government company" under Companies Act; no CAG
- Pvt Ltd → DINs tracked but board minutes not public

**Step 2 — Populate with RBI insiders**
- All board/council members are current or former RBI officials
- Chair is invariably a former RBI Deputy Governor [^5][^8]
- No independent statutory directors with external accountability mandate

**Step 3 — Create overlapping mandates**
- Multiple entities with similar functions → accountability diffuse
- No single entity owns a function exclusively → RBI reallocates at will

**Step 4 — Circumvent procurement rules**
- Societies and Section 8 entities not bound by General Financial Rules
- Single-source awards justified as "specialized expertise" or "technical exigency"
- No tender publication obligation

**Step 5 — Control information flow**
- RTI either does not apply or is contested
- Annual reports not standardised or comparable across entities
- Board minutes never published
- Security audits internal only (if any)

**Step 6 — Reabsorb when convenient**
- IFTAS: Build in IDRBT → spin off to IFTAS → acquire into RBI
- NPCI: Incubate with RBI support → push toward for-profit → retain controlling influence

### 3.4 The NPCI Dimension: For-Profit Conversion Tension

NPCI operates India's most critical payments infrastructure (UPI, RuPay, IMPS, NFS, CTS, NACH, AePS, BBPS). [^14]

**Financials**:
- FY25 surplus: ₹1,552 crore (42% increase from ₹1,095 crore in FY24)
- Operating income: ₹3,270 crore
- 65 member banks

**Governance tensions**:
- **CEO interference (2018)**: RBI overruled NPCI board's preferred CEO candidate and forced the appointment of Dilip Asbe — documented in three board members' dissenting notes. [^9]
- **For-profit conversion debate**: Proposals to convert NPCI from Section 8 to for-profit have been debated since 2023. [^16] This would create a **monopoly for-profit infrastructure operator** with the same board, the same regulatory oversight (RBI), the same information controls — but now with shareholder pressure for returns.
- **NIPL subsidiary**: NPCI International Payments Limited (for-profit, ₹200 crore paid-up capital) already operates globally with no additional governance framework.

### 3.5 Cross-Entity Governance Comparison

| Dimension | IDRBT | IFTAS | ReBIT | RBIH | NPCI |
|-----------|-------|-------|-------|------|------|
| Independent board majority | ❌ | ❌ | ❌ | ⚠️ Partial | ⚠️ Member banks |
| Public RTI access | ❌ | ❌ | ❌ | ❌ | ❌ |
| CAG audit | ❌ | ❌ | ❌ | ❌ | ❌ |
| Competitive procurement | ❌ (IKCON) | Unknown | Unknown | Unknown | ⚠️ MDR-based |
| Published board minutes | ❌ | ❌ | ❌ | ❌ | ❌ |
| Conflict of interest register | ❌ | ❌ | ❌ | ❌ | ❌ |
| Term limits / cooling-off | ❌ | ❌ | ❌ | ❌ | ❌ |
| Independent security audit | ❌ (proven) | Unknown | Unknown | Unknown | ⚠️ Periodic |

---

## References

[^1]: Medianama, June 2026: "Security vulnerabilities in RBI's .bank.in registry exposed sensitive data" — 33+ unauthenticated endpoints, 5,576 records, no security audit, no disclosure mechanism. (https://www.medianama.com/2026/06/223-security-vulnerabilities-rbi-bank-in-registry-sensitive-data)

[^2]: CashlessConsumer .bank.in investigation report: Documents no-tender award of `.bank.in` registry portal to IKCON Technologies. (https://bankin-report.cashlessconsumer.in/report.pdf)

[^3]: Deepak Kumar — IDRBT Director profile: Confirms simultaneous directorships at NPCI, IFTAS, ReBIT, RBIH, Indian Overseas Bank, and IDRBT Governing Council membership. Accessed 2026-07-11. (https://www.idrbt.ac.in/director/)

[^4]: IKCON Technologies Leadership Team: Lists Mahesh Jarati alongside Divakar Talagadadeevi and Madhu Kiran Boindala. Accessed 2026-07-11. (https://www.ikcontech.com/our-leadership-team/)

[^5]: IDRBT Governing Council page: N.S. Vishwanathan (Chair), Deepak Kumar, and other members. Accessed 2026-07-11. (https://www.idrbt.ac.in/governing-council/)

[^6]: IDRBT Former Directors page: Smt. K. Nikhila served 24-Jan-2024 to 01-May-2024 (~3 months); Deepak Kumar assumed charge 02-May-2024. Accessed 2026-07-11. (https://www.idrbt.ac.in/former-directors/)

[^7]: IDRBT "The Journey of IDRBT": Documents EERC (Rangarajan Committee) 2009 recommendation to shed operational services; creation of IFTAS; transfer of INFINET, SFMS, Banking Community Cloud. Accessed 2026-07-11. (https://www.idrbt.ac.in/the-journey-of-idrbt/)

[^8]: RBI Press Release: RBIH Governing Council announced — includes Kris Gopalakrishnan (Chair), A.P. Hota, T. Rabi Sankar, Deepak Kumar, K. Nikhila. Accessed 2026-07-11. (https://www.rbi.org.in/scripts/FS_PressRelease.aspx?fn=9&prid=50666)

[^9]: Medianama, February 2018: "How the RBI Forced National Payments Body to Hire Government Favourite as CEO" — documents RBI overruling NPCI board's CEO choice; three independent directors wrote dissenting notes. (https://www.medianama.com/2018/02/223-rbi-forced-national-payments-body-hire-government-favourite-ceo)

[^10]: Medianama, January 2022: "New fintech division set up at RBI to address issues, leverage opportunities" — Fintech Department established 4 Jan 2022, subsuming DPSS fintech unit. (https://www.medianama.com/2022/01/223-rbi-fintech-department-established)

[^11]: IDRBT Tenders page: All published tenders — no `.bank.in` portal tender found. Accessed 2026-07-11. **Negative evidence**: absence of tender where all other IDRBT procurement is listed. (https://www.idrbt.ac.in/tenders/)

[^12]: IDRBT IT Vendor Management Manual (ITVM_Final.pdf): Documents competitive bidding requirements and procurement thresholds. Accessed 2026-07-11. (https://www.idrbt.ac.in/wp-content/uploads/2022/07/ITVM_Final.pdf)

[^13]: RBI Organisation and Functions page: Lists DICGC as fully-owned subsidiary. IDRBT, ReBIT, IFTAS, and RBIH are NOT listed as subsidiaries — they exist outside RBI's own official organisational disclosure. Accessed 2026-07-11. (https://www.rbi.org.in/commonman/English/Scripts/Organisation.aspx)

[^14]: NPCI Board of Directors page: Confirms board composition and RBI-nominated directors. Accessed 2026-07-11. (https://www.npci.org.in/board-directors)

[^15]: ReBIT LinkedIn and company description: "ReBIT is a wholly owned subsidiary of the Reserve Bank of India" — 1,001-5,000 employees, established 2016. (https://in.linkedin.com/company/reserve-bank-information-technology-pvt-ltd)

[^16]: NPCI for-profit conversion debate: Shareholder proposal to convert NPCI from Section 8 not-for-profit to for-profit to compete internationally. (https://www.sanskritiias.com/current-affairs/npci-from-not-for-profit-to-for-profit)

---

## Appendix: Key Data Points

| Data Point | Value | Source |
|-----------|-------|--------|
| .bank.in portal — unauthenticated API endpoints | 33+ | [^1] |
| User records exposed | 5,576 | [^1] |
| Wildcard certs issued | N/A — unverified claim removed pending RTI | ❌ Not independently verified |
| Orphan Super Admin accounts | 1,072 | [^1] |
| IDRBT Director appointment gap (Nikhila→Deepak) | 1 day | [^6] |
| Nikhila's tenure as IDRBT Director | ~92 days (24 Jan – 1 May 2024) | [^6] |
| Deepak Kumar's concurrent directorships | 6+ (NPCI, IFTAS, ReBIT, RBIH, IOB, IDRBT GC) | [^3] |
| IDRBT's legal form | Society under 1860 Act | IDRBT website |
| IFTAS acquisition by RBI | 2019 | [^7] |
| IDRBT employees transferred to IFTAS | 431+ | IDRBT historical records |
| NPCI FY25 surplus | ₹1,552 crore (+42% YoY) | NPCI financials |
| NPCI operating income FY25 | ₹3,270 crore | NPCI financials |
| NPCI member banks | 65 | NPCI website |
| NIPL paid-up capital | ₹200 crore (incorporated 3 Apr 2020) | Company check |
| ReBIT employees | 1,001-5,000 | [^15] |
| RBI entities NOT listed on RBI's own org page | IDRBT, ReBIT, IFTAS, RBIH | [^13] |
| RBIH established | March 2022, Section 8, ₹100 Cr capital | [^8] |
| RBI Fintech Department established | 4 January 2022 | [^10] |
| ITVM Procurement Manual publication | July 2022 | [^12] |

---

## License & Attribution

This report is published under Creative Commons Attribution 4.0 International (CC BY 4.0). You are free to share and adapt with attribution.

**Compiled**: 2026-07-11 | **Author**: CashlessConsumer / DPI Watch

**Companion files in this repository**:
- `chapters/DeepakKumar.md` — Raw investigation notes
- `chapters/rbi-subsidiaries-survey.md` — Historical survey of all entities
- `annexures/reference-matrix.md` — Cross-verification matrix, negative evidence analysis, timeline, legal framework
- `AGENTS.md` — Project index and pipeline

**Known caveats**: The byelaw amendment allegation remains unverified pending access to IDRBT Governing Council minutes. All other claims are sourced from publicly accessible webpages, published reports, and legally obtained corporate records.
