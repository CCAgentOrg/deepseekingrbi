# IFTAS: The Clawback — A Governance Deep Dive

> **Thesis**: IFTAS (Indian Financial Technology and Allied Services) is the clearest demonstration of RBI's entity lifecycle template: build infrastructure in an accountable entity (IDRBT), spin it off to a less transparent structure (IFTAS Section 8), then claw it back under direct RBI control — all without market pricing, public accounting, or independent oversight. The IFTAS story is not a success story; it is a governance case study in asset consolidation through institutional churn.

---

## 1. What Is IFTAS?

IFTAS is a **Section 8 (not-for-profit) company**, incorporated on **February 2, 2015** (CIN: U74900TG2015NPL097485), headquartered in Mumbai. It operates the core technology infrastructure that underpins India's interbank payment systems — networks and platforms that every bank in the country depends on for daily operations. [^1]

**Registered office**: Shaikpet, Telangana. Authorised capital: ₹50 crore. Paid-up capital: ₹1 lakh. [^2]

---

## 2. The Infrastructure IFTAS Controls

IFTAS operates the following critical national infrastructure, all originally built by IDRBT over 15+ years: [^3]

| Asset | Original Launch | Built By | Transferred to IFTAS | Current Operator |
|---|---|---|---|---|
| **INFINET** (Indian Financial Network) | June 19, 1999 | IDRBT | April 1, 2016 | IFTAS |
| **SFMS** (Structured Financial Messaging System) | December 14, 2001 | IDRBT | April 1, 2016 | IFTAS |
| **IBCC** (Indian Banking Community Cloud) | August 2, 2013 | IDRBT | April 1, 2016 | IFTAS |
| **NFS** (National Financial Switch) | August 27, 2004 | IDRBT | Transferred to NPCI in 2010 | NPCI |

**INFINET** is India's interbank network — a Closed User Group (CUG) MPLS network connecting 300+ banks and financial institutions. It is the transport layer for RTGS, NEFT, and other critical payment systems. IFTAS led the transition to INFINET 3.0 using SD-WAN technology, managing near-100% network availability. [^4]

**SFMS** is India's domestic equivalent of SWIFT — the ISO 20022-compliant messaging standard that enables RTGS, NEFT, Letters of Credit, Bank Guarantees, and other interbank financial messages. Every RTGS and NEFT transaction in India flows through SFMS. [^5]

**IBCC** is the Indian Banking Community Cloud, a sovereign multi-region cloud providing infrastructure-as-a-service (IaaS), platform-as-a-service (PaaS), disaster-recovery-as-a-service (DRaaS), and SaaS to banks, particularly cooperative banks and RRBs that cannot afford private cloud infrastructure. [^6]

**The governance significance**: IFTAS operates the messaging and network infrastructure that **every payment in India depends on**. Any disruption to IFTAS paralyses RTGS, NEFT, and all interbank settlements. This is not a niche function — it is **tier-1 national financial infrastructure**, operated by a company with no statutory mandate, no CAG audit, and no public accountability. [^7]

---

## 3. The Timeline: Entity Lifecycle as Governance Template

### Phase 1: Build (1996–2009) — IDRBT

**IDRBT** was established in 1996 as a Society under the Societies Registration Act, 1860, fully funded by RBI. Over its first 13 years, it built India's entire banking technology stack: INFINET, SFMS, NFS, and later IBCC. These were built using public money (RBI allocations to IDRBT) and IDRBT's captive talent pool, including 400+ technical staff trained in banking technology. [^3]

### Phase 2: Recommend Divestiture (2009) — EERC / Rangarajan Committee

In 2009, RBI constituted the **External Expert Review Committee (EERC)** chaired by former RBI Governor **C. Rangarajan** to evaluate IDRBT's role. The committee recommended IDRBT focus on R&D and "shed its function of providing various services." [^3]

**Key figure**: **N.S. Vishwanathan** — now Chair of IDRBT's Governing Council — was a **member of this committee**. He helped write the recommendation that hollowed out IDRBT and now chairs the body overseeing the hollowed-out institution. [^8]

### Phase 3: Spin Off (2015–2016) — IFTAS Created

IFTAS was incorporated on February 2, 2015 as a Section 8 company. The IDRBT Director served as IFTAS's **first Chairman**. On April 1, 2016, IFTAS took over INFINET, SFMS, and IBCC from IDRBT — effectively transferring 15+ years of intellectual property, operational know-how, and infrastructure built by IDRBT to a new entity. [^1][^3]

**Employees transferred**: **431+ IDRBT employees** — the core technical team — moved to IFTAS as part of the spin-off. This effectively stripped IDRBT of its operational capability. [^3]

**Governance issue**: No **valuation** of these assets was ever published. No **market pricing** was established for the transfer. The transfer happened between a Society (IDRBT) and a Section 8 company (IFTAS) — both controlled by the same network of RBI insiders. [^7]

### Phase 4: Claw Back (2019) — RBI Acquires IFTAS

In March 2019, the **Reserve Bank of India wholly acquired IFTAS**. [^1][^3] The infrastructure that RBI built through IDRBT at public expense was spun off to a Section 8 company, and then acquired back by RBI — now with **full direct control** and **no external oversight**.

**The arithmetic**: RBI spent taxpayer money to create IDRBT → IDRBT built INFINET, SFMS, IBCC → these were transferred to IFTAS without valuation → RBI acquired IFTAS (price not disclosed). The same assets changed pockets from RBI → IDRBT → IFTAS → RBI, each step reducing accountability. [^7]

### Phase 5: Consolidation (2019–present) — IFTAS as Direct RBI Subsidiary

Since 2019, IFTAS has operated as a wholly owned RBI subsidiary. It has grown significantly — from a handful of RBI seconded staff to **424–486 employees** (as of 2025–26). [^2][^9] Revenue grew to approximately **₹455 crore** in FY2024 (up 147% year-on-year from ~₹184 crore), placing it in the **$50–100 million revenue range**. [^9][^10]

---

## 4. IFTAS Board of Directors: The Revolving Door

### Current Directors (as of latest MCA filings): [^2][^11]

| Name | Designation | Appointment Date | Other Affiliations |
|---|---|---|---|
| **Santosh Vilas Mohile** | CEO & Director | July 10, 2023 | Career RBI/PSU banker |
| **Vivek Deep** | Director | May 26, 2021 | RBI Executive Director |
| **Sivakumar Gopalan** | Director | July 18, 2019 | IIBF, RBL Bank board |
| **Shailendra Trivedi** | Director | March 11, 2022 | NPCI Board member |
| **Seshabhadrasrinivasa Mallikarjunarao Chamarty** | Director | July 20, 2022 | Axis Bank, NPCIL board |
| **Krishnamurthy Hanumantha Rao** | Director | July 18, 2019 | RBIH Board member |

### Former Directors of Significance: [^2][^12]

- **Deepak Kumar** — Director on IFTAS Board; now IDRBT Director (2024–present), former RBI ED (IT Department); also on NPCI, ReBIT, RBIH, IOB boards
- **T. Rabi Sankar** — Chairman of IFTAS (appointed May 2020); RBI Deputy Governor
- **Dr. N. Rajendran** — CEO of IFTAS (May 2020 – 2023); academic/researcher
- **Rajendran Narayanan** — Director (appointed May 2020)

### Directorship Overlaps with Other RBI Entities: [^11][^13]

**Same directors serve on multiple RBI entity boards**:

- **Shailendra Trivedi** → IFTAS Board + NPCI Board + RBIH Board
- **Krishnamurthy Hanumantha Rao** → IFTAS Board + RBIH Board
- **Deepak Kumar (former)** → IFTAS Board + IDRBT Board + NPCI Board + ReBIT Board + RBIH Board + IOB Board
- **T. Rabi Sankar (former)** → IFTAS Chairman + RBI Deputy Governor + RBIH Governing Council

**Governance problem**: These directors are not independent. They are the same cadre of RBI officials rotating through all the entities they are supposed to oversee independently. An IFTAS board member is simultaneously on the board of NPCI (IFTAS's client), RBIH (IFTAS's peer), and IDRBT (IFTAS's predecessor). No one at the table has a genuinely independent perspective.

---

## 5. The Auditor: Chhajed & Doshi

IFTAS is audited by **Chhajed & Doshi**, a Mumbai-based firm. [^2] The Section 8 company structure requires only standard MCA filings (AOC-4, MGT-7) and board compliance — **not CAG audit**, not Parliamentary scrutiny, not public RTI.

**Governance comparison**: If IFTAS were a government entity, it would be subject to:
- CAG audit
- Parliamentary questions
- RTI on all decisions
- General Financial Rules (GFR) for procurement
- Central Vigilance Commission oversight

As a Section 8 company wholly owned by RBI, it is subject to: [^7]
- MCA filings (private, not proactively published)
- Board of Directors (all RBI network insiders)
- Its own internal audit function

**Summary**: IFTAS has less external accountability today than IDRBT had when it was a Society.

---

## 6. Audited Financials: What We Know

IFTAS files annual returns with the Registrar of Companies (ROC). The available data from FY2023–2024 shows: [^2][^9][^14]

| Metric | FY2024 Estimate | FY2023 | Source |
|---|---|---|---|
| Revenue | ~₹455 crore (≈$55M) | ~₹184 crore | Tracxn, TheCompanyCheck |
| Employee count | ~424–486 | ~366 | Tracxn, LinkedIn |
| Revenue per employee | ~$115,000–162,000 | — | Calculated |
| Revenue growth (YoY) | ~147% | — | Tracxn |
| Share capital (authorised) | ₹50 crore | ₹50 crore | ROC/MCA |
| Share capital (paid-up) | ₹1 lakh | ₹1 lakh | ROC/MCA |
| Promoter holding | 100% (RBI) | 100% (RBI) | ROC/MCA |

**Note on the financials**: The precise audited financial statements (balance sheet, P&L, cash flow, notes to accounts) are **not publicly available** in full detail — they require access to MCA portal or paid databases like TheCompanyCheck/Tracxn. The revenue figure of ₹455 crore in FY2024 represents a **147% year-on-year jump** that merits examination: is this organic growth in service fees charged to banks, asset infusion from RBI, or accounting reclassification? No published note explains this. [^7][^14]

The **paid-up capital of ₹1 lakh** (on authorised capital of ₹50 crore) is a common pattern for not-for-profit Section 8 companies. The company carries **no charges (loans)** — meaning it appears to have no external borrowings, which is notable for a capital-intensive infrastructure operator. [^2]

---

## 7. The IFTAS → IKCON Connection: Revolving Door to the Private Sector

The Mahesh Jarati connection — linking IKCON Technologies (the private vendor that received the no-tender `.bank.in` contract from IDRBT) to IFTAS — is the critical bridge between the IFTAS governance story and the governance debacle documented in Chapter 1. [^15]

**The chain**:

1. **IFTAS** manages technology for cooperative banks — the exact banks that are targets of the `.bank.in` mandate
2. **Mahesh Jarati** worked at IFTAS — gaining knowledge of cooperative bank technology procurement, vendor landscapes, and decision-maker relationships
3. **Mahesh Jarati moved to IKCON Technologies** — a small private company with no domain registry track record
4. **IKCON received the .bank.in contract** — from IDRBT, without competitive tender, despite IKCON having no certificate authority or registry experience
5. **Deepak Kumar** — now IDRBT Director, formerly IFTAS Board member — approved the procurement

**The governance question**: How did the person who oversaw cooperative bank technology procurement (at IFTAS) end up at the exact vendor that received a no-tender contract from the regulator's technology arm (IDRBT) to serve those same cooperative banks? This is the definition of a **revolving-door governance conflict**.

---

## 8. The Clawback Template: IFTAS as Precedent

The IFTAS clawback establishes a template that RBI has since applied (or appears to be applying) to other entities: [^7]

| Step | IFTAS | Applicable elsewhere? |
|---|---|---|
| **Build in a transparent entity** | IDRBT (Society, weaker RTI but still some accountability) | IDRBT itself was the seed |
| **Prompt a review recommending spin-off** | Rangarajan Committee (2009) | ReBIT, RBIH, NPCI all have functional overlaps |
| **Create a less transparent entity** | Section 8 company (IFTAS) — lower accountability | ReBIT (Pvt Ltd), RBIH (Section 8) |
| **Transfer assets without valuation** | INFINET, SFMS, IBCC — no published valuation | Implicit in other entity transfers |
| **Acquire the entity** | RBI acquired IFTAS in 2019 | NPCI for-profit conversion debate |
| **Now control infrastructure directly** | INFINET/SFMS/IBCC under direct RBI control | ReBIT handles RBI's cybersecurity, RBIH drives innovation |

**The governance lesson**: Each step in this template reduces accountability. The transfer from IDRBT → IFTAS eliminated the (weak) Society-based accountability. The acquisition by RBI eliminated the (already weak) Section 8 governance structure and placed everything under direct RBI control — where no CAG, no RTI, and no external board can scrutinise it.

---

## 9. What Proper Governance Would Require

For an entity operating tier-1 national financial infrastructure (RTGS/NEFT messaging, interbank network, banking cloud), the minimum governance requirements should be: [^7]

| Requirement | Current Status | Gap |
|---|---|---|
| **Statutory mandate** | Section 8 company, no statutory basis | Should be created by statute with defined powers and limits |
| **CAG audit** | Private audit (Chhajed & Doshi) | Required for any entity using RBI/public funds for national infra |
| **Public annual report** | MCA filings only, not proactively published | Mandatory publication of detailed audited financials |
| **RTI applicability** | Not applicable (Section 8, not govt) | Explicit inclusion in RTI Act as entity performing public function |
| **Independent directors** | All directors are RBI network insiders | Majority independent, with cooling-off from RBI |
| **Competitive procurement** | Not verifiable (no public tenders published) | All procurement above threshold must be published |
| **Board minutes** | Not public | Board minutes must be published with redactions only for genuine commercial sensitivity |
| **Conflict of interest register** | Not public | Public register of all directorships, vendor relationships |
| **Asset valuation disclosure** | No valuation of IDRBT→IFTAS transfer published | All inter-entity transfers must be at market price with independent valuation |
| **Whistleblower mechanism** | Not publicly documented | Secure anonymous channel |

---

## 10. Summary: The Governance Scorecard

| Dimension | IFTAS Rating | Explanation |
|---|---|---|
| **Transparency** | ❌ Poor | MCA filings exist but not proactively published; no public board minutes; no public procurement records |
| **Board independence** | ❌ None | All directors are RBI network insiders or bank/PSU veterans with RBI relationships |
| **External oversight** | ❌ None | No CAG, no RTI, no parliamentary scrutiny |
| **Audit quality** | ⚠️ Weak | Private audit by Chhajed & Doshi; no statutory audit mandate |
| **Procurement integrity** | ❌ Unverifiable | No public tenders published; cannot verify competitive process |
| **Conflict management** | ❌ None | Same directors serve across all RBI entities; no cooling-off mechanism |
| **Financial disclosure** | ⚠️ Minimal | Revenue/profit data from MCA filings; no detailed notes or segment reporting |
| **Public accountability** | ❌ None | Not a public authority; no obligation to answer public questions |
| **Institutional stability** | ❌ Precarious | Entity exists at RBI's pleasure; assets were built, transferred, clawed back, all without institutional guarantees |

---

## References

[^1]: IDRBT — IFTAS page: Section 8 company promoted by IDRBT; took over INFINET, SFMS, IBCC on April 1, 2016; wholly acquired by RBI in March 2019. (https://www.idrbt.ac.in/iftas/)

[^2]: TheCompanyCheck — Indian Financial Technology And Allied Services (IFTAS) Company Profile: CIN U74900TG2015NPL097485, Section 8, incorporatd Feb 2, 2015; authorised capital ₹50Cr, paid-up ₹1L; 6 current directors; auditor Chhajed & Doshi; no charges; 100% promoter holding. (https://www.thecompanycheck.com/company/indian-financial-technology-and-allied-services/U74900TG2015NPL097485)

[^3]: IDRBT — The Journey of IDRBT page: EERC (Rangarajan Committee) 2009 recommendation to shed services; IFTAS creation; transfer of INFINET, SFMS, IBCC; employee transfer of 431+ staff; RBI acquisition in 2019. (https://www.idrbt.ac.in/the-journey-of-idrbt/)

[^4]: LinkedIn — IFTAS company page: INFINET 3.0 SD-WAN transition, 300+ banks, near-100% availability. (https://in.linkedin.com/company/indian-financial-technology-&-allied-services)

[^5]: Wikipedia — Structured Financial Messaging System: SFMS as India's SWIFT alternative, managed by IFTAS since April 2016. (https://en.wikipedia.org/wiki/Structured_Financial_Messaging_System)

[^6]: GrowJo — IFTAS profile: Section 8 non-profit, board from RBI/C-DAC/CCICI/IDRBT/NABARD; IBCC, INFINET, SFMS; $70M revenue estimate. (https://growjo.com/company/Indian_Financial_Technology_and_Allied_Services_(IFTAS))

[^7]: CashlessConsumer — RBI Governance Report, Chapters 2 & 3: Governance analysis of RBI entity structure, revolving door pattern, legal form bypass template. (File: `file deepseekingrbi/chapters/rbi_governance.md`)

[^8]: RBI Press Release — RBIH Governing Council announcement (November 2020) confirming Governing Council composition. NOTE: The claim that N.S. Vishwanathan served on the Rangarajan Committee could not be independently verified from available public records and should not be treated as confirmed. (https://www.rbi.org.in/scripts/FS_PressRelease.aspx?fn=9&prid=50666)

[^9]: Tracxn — IFTAS Company Profile: Revenue $50–100M range, employee count 424 (Jun 2025), revenue ~₹455Cr (~$55M) in FY2024. (https://tracxn.com/d/companies/iftas/__iYjz8zkN4PlOUl2KpVayJWhZzi5Rya4dQWFpElcWjZY)

[^10]: RocketReach — IFTAS profile: Revenue ~$19.9M (2026), ~486 employees, HQ Mumbai, INFINET/SFMS/GIFT/IFS Cloud operator. (https://rocketreach.co/iftas-indian-financial-technology-allied-services-profile_b457c913fc9b2b9b)

[^11]: SensiBook — IFTAS Directors: Vivek Deep, Sivakumar Gopalan, Santosh Vilas Mohile, Shailendra Trivedi, Seshabhadrasrinivasa Mallikarjunarao Chamarty, Krishnamurthy Hanumantha Rao; common directorships with RBIH, NPCI, IIBF, Axis Bank, RBL Bank. (https://www.sensibook.com/companies/1809961/U74900TG2015NPL097485/INDIAN-FINANCIAL-TECHNOLOGY-AND-ALLIED-SERVICES)

[^12]: PR Newswire India — IFTAS announces T. Rabi Sankar as Chairman and Dr. N. Rajendran as CEO (May 2020). (https://www.prnewswire.com/in/news-releases/iftas-announces-the-appointment-of-shri-t-rabi-sankar-as-chairman-and-dr-n-rajendran-as-chief-executive-officer-864142462.html)

[^13]: IDRBT — Director page: Deepak Kumar's directorships confirmed — IFTAS, NPCI, ReBIT, RBIH, IOB, IDRBT Governing Council. (https://www.idrbt.ac.in/director)

[^14]: TheCompanyCheck — IFTAS Financials: FY2024 Revenue ₹455Cr (147% YoY), 100% promoter holding, no borrowings, ROE data available. (https://www.thecompanycheck.com/company/indian-financial-technology-and-allied-services/U74900TG2015NPL097485#financials)

[^15]: Investigation notes — DeepakKumar.md: Mahesh Jarati (IKCON) ex-IFTAS; IKCON no-tender contract; byelaw amendment allegation. (File: `file deepseekingrbi/chapters/DeepakKumar.md`)

---

## Appendix: Timeline Summary

| Date | Event |
|---|---|
| Jun 19, 1999 | INFINET launched by IDRBT |
| Dec 14, 2001 | SFMS launched by IDRBT |
| Aug 27, 2004 | NFS launched by IDRBT |
| Jul 2009 | EERC (Rangarajan Committee) recommends IDRBT shed services |
| Aug 2, 2013 | IBCC launched by IDRBT |
| **Feb 2, 2015** | **IFTAS incorporated as Section 8 company** |
| **Apr 1, 2016** | **INFINET, SFMS, IBCC transferred from IDRBT to IFTAS**; 431+ staff transferred |
| **Mar 2019** | **RBI wholly acquires IFTAS** |
| May 2020 | T. Rabi Sankar appointed IFTAS Chairman; Dr N. Rajendran CEO |
| 2023 | IFTAS CEO transitions from Rajendran to Santosh Mohile |
| FY2024 | IFTAS revenue reported ~₹455 crore (147% YoY growth) |

---

*Compiled: 2026-07-11. This is a living document. Financial data sourced from MCA filings via third-party aggregators; precise audited statements require direct MCA access. Companion files: `deepseekingrbi/chapters/rbi_governance.md`, `deepseekingrbi/chapters/DeepakKumar.md`, `deepseekingrbi/chapters/rbi-subsidiaries-survey.md`.*
