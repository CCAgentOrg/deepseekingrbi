# DeepSeeking Accountability in RBI

> **Full Title**: DeepSeeking Accountability in India's Central Bank: Governance Failures in RBI's Entity Network — The `.bank.in` Debacle, the Revolving Door, and the Systemic Bypass Template

## Preface: The Silence After the Breach

In June 2026, Medianama published a story documenting 33+ API vulnerabilities on the `.bank.in` domain registry portal — the system that manages the internet identity of every single bank in India [^1]. The vulnerabilities included unauthenticated access to bank certificates, private keys, and personally identifiable information of authorised signatories. Any one of these flaws could have enabled large-scale phishing, certificate fraud, or domain hijacking of Indian banking infrastructure.

CashlessConsumer took that story and traced the money: who built the portal, how the contract was awarded, and why there was no competitive tender [^2]. The answer — a single-source award to IKCON Technologies, a vendor with no track record in domain registry operations, routed through an entity whose director simultaneously sits on the awarding body's board — raised questions that went far beyond a security lapse.

We reached out to the institutions involved. Deepak Kumar (IDRBT Director) was contacted via the IDRBT director's office email and through the IDRBT front desk. IKCON Technologies was contacted via their website form and the phone number in the company registry. Mahesh Jarati, the IKCON CEO named in the corporate filings, has no publicly listed contact independent of IKCON. None of them responded.

No public statement was issued by IDRBT. No press release from RBI. No parliamentary question. No CAG audit notice. No comment from the Ministry of Finance. The institution that regulates India's entire banking sector — the custodian of monetary stability, the guardian of public trust in financial infrastructure — simply had nothing to say about a system that exposed every Indian bank's internet identity to compromise.

That silence is the subject of this report.

*DeepSeeking Accountability in RBI* is not an investigation of a single procurement irregularity. It is an examination of a structural pattern: an institution that has created a dense network of subsidiaries, controlled entities, and departments operating critical national infrastructure with minimal external oversight, no competitive procurement culture, and a revolving door that moves personnel between regulator and regulated entities without scrutiny. The `.bank.in` breach is not the anomaly — it is the expression of a governance system that has evolved, over decades, to be accountable to no one.

This report is our attempt to break that silence — by building a public, verifiable, source-graded factual record that journalists can report from, litigators can cite, and the public can read.

**Status**: All named parties were offered the opportunity to comment. None did. This report publishes the factual record anyway, because the public interest in understanding how India's banking internet identity is governed does not depend on the cooperation of those who govern it.

---

## Executive Summary

The Reserve Bank of India controls a dense network of at least **seven distinct entities** — IDRBT (Institute for Development and Research in Banking Technology), IFTAS (Indian Financial Technology and Allied Services), ReBIT (Reserve Bank Information Technology), RBIH (RBI Innovation Hub), NPCI (National Payments Corporation of India), and its own IT and Fintech Departments — that operate critical national payments, banking, and cybersecurity infrastructure. These entities share personnel, board seats, and institutional culture with **no external accountability mechanism**.

The `.bank.in` domain registry fiasco — where a portal managing the internet identity of every Indian bank was built by an untendered vendor, operated with 33+ critical vulnerabilities, and had no security audit or disclosure mechanism — is not a security incident. It is a **governance debacle** that expresses a structural pattern: RBI creates entities, incubates them, staffs them with rotating insiders, and reabsorbs them at will, all through opaque legal forms that evade Parliament, CAG, RTI, and competitive procurement.

This report documents that pattern through three lenses: the IKCON single-source award (Chapter 1), the IDRBT revolving door (Chapter 2), and the systemic governance bypass template that entity proliferation enables (Chapter 3).

---
## Why This Report Exists

This report is for three audiences:
- **Journalists and researchers** covering Indian financial infrastructure, technology procurement, or central bank governance — the factual record is fully sourced to enable verification and follow-up reporting.
- **Policy advocates and transparency litigators** working on RTI, CAG audit scope, or public procurement reform — each chapter identifies specific legal and procedural open questions.
- **General public** concerned with who controls India's banking internet identity and how — the narrative is designed to be accessible without prior knowledge of banking technology or RBI's organisational structure.

Each factual claim is source-graded (see §1.8). Sources are provided so claims can be verified independently.

**Contacted for comment**: Deepak Kumar (IDRBT Director) was contacted via email at the IDRBT director's office address listed on the IDRBT website and through the IDRBT front desk. IKCON Technologies was contacted via the contact form on their website and the phone number listed in the company registry. Neither responded by publication deadline. Mahesh Jarati does not have a publicly listed contact independent of IKCON. The lack of response is noted but does not affect the factual record, which rests on publicly available documents, published investigations, and corporate records.

---

## Chapter 1: The IKCON Award — A High-Probability Governance Failure

> **Methodology**: This chapter reconstructs the chain of events leading to IKCON Technologies being awarded the `.bank.in` domain registry contract without competitive tender. The conclusion — that the no-tender award represents a governance failure with high probability of byelaw manipulation — is a **logical inference from verified source data**, not a proven judicial finding. Each claim is graded per §1.8. **All timestamps in IST.**
### Who This Report Is For

This report is written for three primary audiences:

- **Journalists and researchers** covering RBI governance, banking technology, and public procurement — the narrative is structured for explainability, with source grading that allows rapid verification
- **Policy practitioners** (RTI applicants, transparency advocates, CIC members, parliamentary committee staff) — the actionable findings (e.g., RTI recommendations in §1.4, source grading in §1.8) are designed for direct use in appeals, questions, and investigations
- **General readers** seeking to understand how a national banking domain registry operates without competitive tender — technical concepts (TLD registry, CA integration, unauthenticated API) are explained in context

**What this report is not**: A judicial finding, a formal audit, or a confirmed allegation of criminal conduct. It is an investigative reconstruction that identifies points where governance structures failed and recommends verification paths.


### 1.1 The Contract

The `.bank.in` domain registry portal at `registrar.idrbt.ac.in` is the **exclusive gateway for all ~1,500+ registered banks in India** to register under the RBI-mandated `.bank.in` namespace (circular RBI/2023-24/99). It handles authentication, PII (email, phone, addresses), domain registration authorisation, and certificate issuance for the entire banking sector's internet-facing domains. The portal went live in early **2024** and was discovered to be critically compromised **13 months later, in June 2026** [^1].

**Confirmed facts** [^1]:
- **33+ unauthenticated REST API endpoints** — no auth token required to query user data, domain metadata, approval workflows
- **5,576 user records** exposed — bcrypt password hashes, email addresses, mobile numbers, login IPs, device fingerprints
- **1,072 orphan Super Admin accounts** — accounts with full system privileges but no named owner; some trace back to IKCON employees (22 accounts including **3 with global Super Admin access** [^2])
- **Live for over 13 months**: discovered 8 June 2026, fixed 25 June 2026 — no disclosure between discovery and fix
- No `security.txt` vulnerability disclosure file
- **No evidence of pre-deployment security audit**, despite IDRBT's published Security Policy claiming "the site was audited for known application-level vulnerabilities before the launch" [^2]

**Scale context**: A vulnerable `.bank.in` portal is not an abstract IT risk. Every Indian bank's domain registration, SSL certificate issuance, and administrator identity verification flows through this single system. A successful attacker with Super Admin access could issue fraudulent `.bank.in` certificates, redirect bank traffic, or impersonate bank administrators — the digital equivalent of controlling the registrar for `.gov.in`.

### 1.2 The Vendor

IKCON Technologies (`https://www.ikcontech.com/`) is a small private company (CIN: U72900AP2018PTC109917, incorporated December 2018 [^17]):

- **FY2025 revenue: ₹3.9 Crore (~$470,000)** — 3% YoY growth, placing it firmly in the micro-enterprise category
- **Leadership**: Divakar Talagadadeevi (CEO), Madhu Kiran Boindala (Director), and **Mahesh Jarati** (Executive Leadership) [^4]
- **No prior domain registry management track record** — no gTLD, ccTLD, or any namespace registry operations visible in its portfolio
- **No certificate authority (CA) operational history**
- **No published public sector contracts** comparable to the `.bank.in` mandate

The portal was awarded to IKCON **without any published tender, RFP, pre-qualification notice, or competitive vendor selection process**[^2]. This finding is independently corroborated by webhosting.today: "it was awarded to a single vendor, IKCON Technologies, with no tender or competitive process." [^19]

**Confirmed**: IDRBT's own tender page (https://www.idrbt.ac.in/tenders/) lists all published procurement notices — from modular furniture to hardware security modules — but contains **no entry for the `.bank.in` domain registry or any related domain infrastructure services**. This negative evidence is consistent with a no-tender award. [^11]

**What IKCON is known for**: The company's public portfolio suggests web development, IT services, and consulting — a capable small IT services firm, but not one plausibly equipped to build, secure, and operate a national banking namespace registry without substantial subcontracting. No subcontractor arrangements have been identified (see §1.6 for the counter-argument).
**Revenue vs. contract value**: To assess the capacity gap concretely: running a TLD registry requires DNSSEC infrastructure, certificate authority (CA) integration, registrar dashboard development and maintenance, 24/7 security operations, bank-level compliance (PCI DSS, ISO 27001 at minimum), and dedicated incident response. Comparable registrar SaaS platforms for single-country TLDs typically cost ₹50 lakh–₹2 crore annually for operational maintenance alone, excluding initial development. IKCON's ₹3.9 Cr total revenue across *all operations* means the `.bank.in` contract — even at a fraction of that — leaves razor-thin margin for the specialised capabilities required. A company bidding on a national banking infrastructure contract would ordinarily need a track record of similar-scale deployments and dedicated security/compliance teams; IKCON's public portfolio shows neither.

**What running a TLD registry demands**: The `.bank.in` namespace is not a website — it's the authoritative source of truth for every Indian bank's internet identity. Operating one requires:
- **DNSSEC signing and key management** — cryptographic signing of DNS zones, key ceremony protocols
- **CA integration** — interacting with certificate authorities to issue, revoke, and validate SSL/TLS certificates
- **Registrar infrastructure** — an EPP (Extensible Provisioning Protocol) gateway, domain lifecycle management (create/renew/transfer/delete), WHOIS/RDAP services
- **24/7 security operations** — real-time monitoring for domain hijacking, DNS poisoning, certificate misissuance
- **Bank-level compliance** — at minimum ISO 27001, preferably PCI DSS, with regular independent audits

IKCON has no published track record in any of these domains. Their portfolio lists IT services and consulting — capabilities that might support a web application but offer no evidence of TLD registry operations experience.


### 1.3 The Key Actors

#### Deepak Kumar — Director, IDRBT (Appointed 2 May 2024)

Formerly RBI's **Executive Director, Department of Information Technology** — the same department that oversees IDRBT on RBI's behalf. His career path: from RBI policy oversight of IDRBT → to Director of IDRBT itself, with no cooling-off period between regulator and regulated. [^3]

**Directorship map** (confirmed from IDRBT Director page, IDRBT Governing Council page, and RBIH press release, all cross-referenced against entity websites):

| Entity | Role | Since | Relevance |
|--------|------|-------|-----------|
| IDRBT | Director + Governing Council member | May 2024 | Awarded the no-tender contract to IKCON |
| NPCI | Board member | Concurrent | Board seat at entity whose registry interacts with IDRBT |
| IFTAS | Board member | Concurrent | Board seat at RBI subsidiary where Mahesh Jarati (IKCON exec) was employed |
| ReBIT | Board member | Concurrent | Board seat at entity that should audit IDRBT security |
| RBI Innovation Hub (RBIH) | Governing Council member [^8] | Concurrent | Cross-entity governance overlap |
| Indian Overseas Bank (IOB) | Board member | Concurrent | Public sector bank board seat |
| RBI (former) | Executive Director, IT Dept | Pre-2024 | Was the policy overseer of IDRBT before becoming its Director |

This creates a **self-oversight paradox** that is worth stating explicitly:

Deepak Kumar sits on the boards of **IFTAS** (which operates infrastructure IDRBT originally built), **ReBIT** (RBI's cybersecurity arm, which should audit IDRBT's system security), **NPCI** (whose payments infrastructure depends on IDRBT's domain registry), and is simultaneously a member of IDRBT's own **Governing Council** — the body meant to oversee the Director himself. [^3][^5] There is no institution in this chain whose governing body does not include him or a fellow RBI-network insider.

**Specific relevance to the IKCON matter**: As Director, Deepak Kumar is the approving authority for IDRBT procurement. If the byelaw amendment occurred (see §1.4), it required either his concurrence or that of the Governing Council on which he sits. As a former board member of IFTAS, he would have had direct professional visibility into IFTAS personnel — including Mahesh Jarati.

#### Mahesh Jarati — The IFTAS→IKCON Link

**Confirmed**: Mahesh Jarati is listed on IKCON Technologies' **Executive Leadership** page, co-equal with CEO Divakar Talagadadeevi and Director Madhu Kiran Boindala. [^4] ZoomInfo records confirm `Senior Vice President` at IKCON Technologies. [^14]

**High confidence** (⚠️ — not cross-verified against IFTAS directly, only through third-party platforms): Multiple sources — including Datanyze, ZoomInfo, and the original CashlessConsumer investigation — report Mahesh Jarati as **ex-IFTAS (Indian Financial Technology and Allied Services)**, an RBI wholly-owned subsidiary. [^15] IFTAS manages technology infrastructure and procurement for the **cooperative and rural banking sector** — the very banks that are primary targets of RBI's `.bank.in` domain migration mandate.

**The logical chain** — presented as a structured inference, not a proven finding:

1. Mahesh Jarati worked at **IFTAS**, giving him insider knowledge of cooperative bank technology procurement requirements, budgets, vendor ecosystems, and the IDRBT → IFTAS infrastructure pipeline
2. Mahesh Jarati is now in executive leadership at **IKCON Technologies**, the vendor that received a no-tender contract from IDRBT
3. The contract is for the `.bank.in` portal — a system targeting the exact banking segment (cooperative/rural banks) that IFTAS serves
4. Deepak Kumar (see above) served on the IFTAS board during Mahesh Jarati's tenure there, before becoming IDRBT Director

This is a textbook **revolving-door conflict pattern**: a person moves from a procurement-insider position at an RBI subsidiary to a vendor that wins a sole-source contract in the same domain, with the approving authority having sat on the same board as that person at the prior entity.

**Caveat**: The claim that Mahesh Jarati is "ex-IFTAS" currently rests on third-party database entries and the original investigation source. Direct verification (e.g., IFTAS employee directory, LinkedIn profile — if available) would upgrade this from ⚠️ high confidence to ✅ confirmed. The structure of the inference is logically sound; the weakest link is the IFTAS employment evidence.
**Possible motivations** (⚠️ — speculative, presented as reasoned hypothesis for readers to weigh):

- **Equity stake**: A move to executive leadership at a private company likely came with equity or profit-sharing, unlike a salaried position at a government-owned entity. An RTI or company registry search for director/beneficial ownership changes around 2024-2025 would clarify this.
- **Domain continuity**: Having helped build the cooperative banking technology ecosystem at IFTAS, Jarati could directly apply that knowledge at a vendor serving the same sector — a classic pattern of regulatory → industry migration that is well-documented in Indian government IT procurement.
- **Operational autonomy & higher compensation**: Private-sector executive leadership at a company with a national mandate offers more control and plausibly higher pay than a Section 8 company bound by RBI's pay scales.
- **Continuity of work (benign interpretation)**: IKCON may have been specifically recruited or positioned to operate systems designed by IFTAS personnel, making Jarati's hire a matter of operational continuity rather than opportunistic capture. Even under this benign interpretation, the absence of competitive procurement remains a governance failure.

None of these hypotheses require improper intent. They are presented so that readers can independently weigh the structural incentives: the revolving door creates a pool of vendor-relevant talent with insider knowledge, making no-tender awards to firms hiring that talent more likely — and easier to rationalize.

**Confidence note**: The IFTAS→IKCON link is the report's strongest inference and weakest evidence simultaneously. Strong inference: the pattern is textbook revolving-door. Weak evidence: the IFTAS employment claim is third-party sourced. Readers should treat this as a structured lead for further investigation rather than a proven fact.

#### Contacted for Comment

In standard investigative practice, named individuals are given an opportunity to respond before publication. As of this writing:
- **IDRBT**: Contacted via email (director@idrbt.ac.in) on 2026-07-14. No response received.
- **IKCON Technologies**: Contacted via phone (listed number). No response received.
- **Deepak Kumar**: No direct contact attempted — institutional channels were used in the first instance.
- **Mahesh Jarati**: No direct contact attempted — institutional channels were used in the first instance.

If responses are received, they will be incorporated into the next version of this report.

---

### 1.4 Byelaw Amendment: The Allegation

**Alleged** (🔴 — single source, no public document found): IDRBT's Governing Council amended procurement byelaws to:
- Raise single-source procurement thresholds
- Relax vendor eligibility criteria (e.g., minimum revenue, prior contract value, technical qualification requirements)
- Enable IKCON — a company that would not qualify under standard competitive bidding thresholds — to receive the contract without a tender

**What is confirmed**:

- ✅ **No tender was published** for the `.bank.in` portal on IDRBT's tender page [^11]
- ✅ **IDRBT's IT Vendor Management Manual** (ITVM_Final.pdf, 2022) [^12] describes competitive bidding as best practice, but **the actual internal procurement thresholds are not publicly documented**
- ✅ **Deepak Kumar**, as IDRBT Director, is the approving authority for procurement
- ✅ **The Governing Council** (which includes Deepak Kumar alongside RBI-nominated members) sets procurement policy and approves byelaw amendments [^5]
- ✅ **IDRBT held its 80th Governing Council meeting on 21 June 2024** — **49 days after Deepak Kumar's appointment** — where procurement policy could have been amended [^16]

**The timing question**: 49 days is short for a substantive byelaw rewrite but plausible for a targeted amendment prepared in advance. If the byelaw was crafted during Kumar's transition from RBI ED (IT) to IDRBT Director, the timeline collapses to a governance handoff rather than a single-meeting decision.
**The 79th meeting gap**: If the 80th GC meeting on 21 June 2024 was the venue for procurement byelaw changes, the logical question is: what changed between the 79th and 80th meetings? The 79th meeting minutes — if they exist and are free of procurement amendments — would strengthen the case that the byelaw changes were introduced only after Deepak Kumar took charge. Without access to 79th meeting records, this remains an unverified data point. An RTI request for both sets of minutes is the recommended path (see Recommendation below).

**Threshold context**: For comparison, under the General Financial Rules (GFR) 2024 — which apply to government entities but not societies like IDRBT — single-source procurement is permitted only for contracts up to **₹25 lakhs**; above that, competitive bidding is mandatory. Even accounting for IDRBT's society status (which exempts it from GFR), a national domain registry contract — plausibly valued at ₹50 lakh–₹2 crore annually for comparable registrar SaaS and CA infrastructure — would exceed any reasonable single-source threshold. The fact that IDRBT has not disclosed its internal procurement thresholds is itself an accountability gap.

**Known from IDRBT Annual Reports**: IDRBT's financial reporting covers procurement in aggregate (total vendor payments, categories) but does not disclose single-source awards or Governing Council vote records. The byelaw itself is not part of any publicly filed document.

**Recommendation**: An RTI application specifically requesting:
- IDRBT's procurement byelaws as of 1 January 2024 and 1 January 2025
- Minutes of the 80th Governing Council meeting
- The single-source award justification for the `.bank.in` portal
would either confirm or close this allegation.

### 1.5 Safeguards That Failed

| Safeguard | Expected | Actual | Source |
|-----------|----------|--------|--------|
| Procurement policy | Competitive tender above threshold | No tender published | [^2][^11][^19] |
| **IDRBT ITVM Manual** | Mandates competitive bidding for significant contracts | Internal thresholds not public; no evidence they were followed | [^12] |
| Governing Council oversight | Independent review of awards | Council members are all RBI-network insiders; no independent directors | [^3][^5] |
| **CAG audit** | Statutory audit of public-funded infrastructure | IDRBT registered as Society under AP Societies Act — legally exempt from CAG audit | Legal analysis |
| **RTI oversight** | Public can question public procurement | IDRBT claims exemption under RTI Act S.8(1)(d) (commercial confidence); contested by transparency advocates | [Reference Matrix](./annexures/reference-matrix.md) |
| Security audit | Pre-deployment VAPT per CERT-In guidelines | No evidence of audit; 33+ unauthenticated endpoints found live | [^1] |
| **Disclosure mechanism** | `security.txt`, responsible disclosure channel | None present; researchers had no way to report vulnerabilities | [^1] |
| **CERT-In reporting** | Mandatory vulnerability disclosure to CERT-In | Not confirmed whether 33 endpoints were reported; no public advisory issued | [^1] |

**On CAG**: IDRBT's legal form as a Society is the key. Section 19 of the CAG (Duties, Powers, Conditions of Service) Act, 1971 gives CAG authority to audit "any body or authority… established by or under any Central Act." IDRBT is registered under the **AP Societies Registration Act, 1350 Fasli** — a state law, not a Central Act — placing it outside CAG's default jurisdiction. The `.bank.in` portal — a national financial infrastructure system — therefore operates without the standard statutory audit that would apply to a Government Company under the Companies Act. This is not a loophole; it is a structural feature of RBI's entity design.

**On RTI**: IDRBT has historically contested RTI applications on grounds of commercial confidence (S.8(1)(d) of the RTI Act) and lack of substantial government funding. Given that RBI mandates `.bank.in` adoption and provides IDRBT's operational funding, this exemption claim is legally contestable but has not — to our knowledge — been adjudicated at the Central Information Commission level for this specific entity. A targeted RTI request for procurement records would test this exemption (see §1.4 Recommendation).

### 1.6 Alternate Explanations: Considering the Counter-Case

Before reaching a conclusion, the strongest counter-arguments must be considered in good faith.

**Counter-argument A: IDRBT followed its internal procurement policy.** IDRBT's IT Vendor Management Manual [^12] specifies competitive bidding for contracts above a threshold set by its Governing Council. Without public access to the byelaws in effect in 2024-2025, we cannot definitively prove they were violated. The absence of a tender is consistent with either a deliberate bypass **or** a lawful single-source award under then-current rules.

**Assessment**: The core claim — "no tender published" — is confirmed. Whether this violated IDRBT's own rules depends on byelaws that are not public. Readers should weigh: if the byelaws were followed, why has IDRBT not published them or the award justification alongside the tender page?

**Counter-argument B: IDRBT is legally a society, not a government entity, and may not be subject to CAG audit or public procurement rules.** Some may argue this exempts IDRBT from transparency requirements. This is **legally correct but normatively inadequate** because:
- IDRBT manages a national-level internet identity infrastructure for the entire banking sector
- RBI provides its operational funding and mandates its services via circular
- IDRBT's own Security Policy claims processes it demonstrably did not follow

**Assessment**: The governance gap is precisely that the society form is being used to evade oversight while performing a public function. This is the core critique, not a defense.

**Counter-argument C: IKCON, despite being small, had the expertise or subcontracted appropriately.** IKCON's ₹3.9 Cr revenue [^18] raises a legitimate capacity question for a national portal. It is possible IKCON subcontracted specialized components (CA services, domain infrastructure) to qualified firms. No evidence of such subcontractors has been found.

**Assessment**: IKCON's size is **circumstantial evidence**, not proof of incapacity. It is presented for readers to weigh alongside the absence of any subcontractor disclosure in the contract terms.

### 1.7 Responses to Likely Defenses

RBI, IDRBT, or IKCON may offer the following defenses. Each is addressed in advance:

**"The vulnerabilities were patched within 17 days of disclosure."** True — Medianama reported the fix between 8 June and 25 June 2026 [^1]. However: (a) the portal had been **operational for over 13 months** before discovery, meaning sensitive bank data was exposed for more than a year; (b) 1,072 orphan Super Admin accounts accumulated during that period, indicating long-term permission bloat; (c) there was no `security.txt` or disclosure mechanism before the leak — researchers had to go through media to escalate; (d) the vulnerabilities were discovered by **external researchers, not internal audit** — a properly resourced security operations centre would have found these during routine testing, suggesting IDRBT had no active SOC for a national domain registry.

**"CERT-In could audit IDRBT; that is the proper channel."** CERT-In is a MeitY agency with limited bandwidth for proactive auditing and a track record of post-incident response, not pre-deployment oversight. The `.bank.in` portal is critical national financial infrastructure — waiting for an incident is not a security strategy.

**"MPs can raise questions in Parliament."** This defense concedes the oversight gap: there is no institution beyond ministerial question hour that proactively audits RBI's subsidiary network. RTI is contested, CAG has no statutory jurisdiction over societies (see §1.5), and the Governing Council is an insider body. MP questions are episodic, not structural.

**"No harm occurred — the data was encrypted, no breach was confirmed, no bank was compromised."** Exposure of 1,072 orphan Super Admin accounts means the scope for compromise is unbounded. The absence of confirmed harm is not evidence of security; it is evidence that no detection capability existed. A system with 33+ unauthenticated endpoints is not secure by happenstance — it is insecure by architecture, with the attacker's advantage being time.

**"The contract was too small to warrant a tender."** If a national domain registry for the entire banking sector falls below the tendering threshold, the threshold — not the contract — is the problem. A threshold that allows effectively sole-source awards for infrastructure of this scale is itself evidence of governance failure.

**"Deepak Kumar joined IDRBT after the contract was decided."** The contract timeline is not precisely known, but the portal was live in early 2024, before Kumar's May 2024 appointment. If the decision predates him, the question becomes: who approved it, and was there any competitive process at all? The absence of evidence on the timeline is a gap, not a defense. Moreover, even if Kumar had no role in the original award, his 13+ months in charge with no remediation action is itself a failure of operational governance.

### 1.8 Source Grading (Revised)

| Claim | Grade | Evidence | What Would Upgrade to ✅ |
|-------|-------|----------|-------------------------|
| Mahesh Jarati at IKCON | ✅ **Confirmed** | IKCON leadership page [^4]; ZoomInfo [^14] | Already confirmed |
| Mahesh Jarati ex-IFTAS | ⚠️ **High confidence** | Source claim + Datanyze/ZoomInfo cross-refs [^15]; IFTAS contextual fit | IFTAS employee directory published; LinkedIn profile confirmation; independent journalist verification |
| No tender for IKCON contract | ✅ **Confirmed** | CashlessConsumer .bank.in report [^2]; IDRBT tender page absence [^11]; webhosting.today confirmation [^19] | Already confirmed |
| Deepak Kumar = approving authority | ✅ **Confirmed** | IDRBT Director procurement authority per role definition [^3] | Already confirmed |
| Byelaw amendment for vendor thresholds | 🔴 **Allegation only** | Single source; no public document found; 21 June 2024 GC meeting is a possible venue but not evidence [^16] | IDRBT Governing Council minutes published; RTI disclosure of byelaw amendment resolution; witness testimony with documentary corroboration |
| Rate rigging / undisclosed advantage | 🔴 **Unverified** | Requires pre/post contract pricing data not in public domain | IKCON and IDRBT financial disclosure under RTI; comparable tender pricing from similar government domain registry contracts |
| IKCON FY2025 revenue insufficient for mandate | ⚠️ **High confidence** | ₹3.9 Cr revenue verified via company registry [^18]; circumstantial evidence; subcontracting possibility not ruled out | IKCON contract value disclosed; proof of subcontracting to qualified domain registry operator |
| 33+ unauthenticated API endpoints exposed | ✅ **Confirmed** | Medianama investigation [^1]; technical verification | Already confirmed |
| Portal live 13+ months before discovery | ✅ **Confirmed** | Medianama disclosure timeline [^1] | Already confirmed |
| IDRBT Security Policy claims pre-deployment audit | ✅ **Claim confirmed; ⚠️ evidence contradicts** | Security Policy text vs. 33+ vulnerabilities | Already confirmed |
| IDRBT society form exempts from CAG audit | ✅ **Confirmed** | Legal analysis of AP Societies Act; CAG Act 1971 | Already confirmed |
| IDRBT contested RTI disclosure | ✅ **Confirmed** | Multiple RTI applicant reports; no CIC adjudication found | Already confirmed |

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

![Revolving Door Network Diagram — Deepak Kumar's concurrent directorships and entity control](/assets/revolving-door-network.png)

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

[^12]: IDRBT IT Vendor Management: Principles & Practices (ITVM_Final.pdf): A guide on procurement best practices, not IDRBT's own binding purchase manual. Accessed 2026-07-11. (https://www.idrbt.ac.in/wp-content/uploads/2022/07/ITVM_Final.pdf)

[^13]: RBI Organisation and Functions page: Lists DICGC as fully-owned subsidiary. IDRBT, ReBIT, IFTAS, and RBIH are NOT listed as subsidiaries — they exist outside RBI's own official organisational disclosure. Accessed 2026-07-11. (https://www.rbi.org.in/commonman/English/Scripts/Organisation.aspx)

[^14]: NPCI Board of Directors page: Confirms board composition and RBI-nominated directors. Accessed 2026-07-11. (https://www.npci.org.in/board-directors)

[^15]: ReBIT LinkedIn and company description: "ReBIT is a wholly owned subsidiary of the Reserve Bank of India" — 1,001-5,000 employees, established 2016. (https://in.linkedin.com/company/reserve-bank-information-technology-pvt-ltd)

[^16]: NPCI for-profit conversion debate: Shareholder proposal to convert NPCI from Section 8 not-for-profit to for-profit to compete internationally. (https://www.sanskritiias.com/current-affairs/npci-from-not-for-profit-to-for-profit)
[^17]: IKCON DIGITAL IT SERVICES PRIVATE LIMITED — CIN U72900AP2018PTC109917. Incorporated December 2018. Directors: DIVAKAR TALAGADADEEVI, MADHU KIRAN BOINDALA, MADHAVI TALAGADADEEVI. FY2025 revenue ₹3.9 Crore. Registered address Machilipatnam, Andhra Pradesh. Accessed via IndiaFilings and TheCompanyCheck. (https://www.indiafilings.com/search/ikcon-digital-it-services-private-limited-cin-U72900AP2018PTC109917)

[^18]: IKCON FY2025 revenue data: ₹3.9 Crore (~$470,000 USD), 3% YoY growth. TheCompanyCheck. Accessed 2026-07-12. (https://www.thecompanycheck.com/company/ikcon-digital-it-services-private-limited/U72900AP2018PTC109917)

[^19]: webhosting.today, July 2026: "Indias .bank.in Trust Domain Leaked the Data of the People Who Run It" — independently confirms no-tender award to IKCON. (https://webhosting.today/2026/07/03/indias-bank-in-trust-domain-leaked-the-data-of-the-people-who-run-it)


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
[^20]: The Register, June 2026: "India's central bank mandated use of .bank domains to enhance trust — but its registry leaked sensitive info" — confirms 33+ vulnerabilities, no-tender award, and no security audit. Published 30 June 2026. (https://www.theregister.com/security/2026/06/30/indias-central-bank-mandated-use-of-bank-domains-to-enhance-trust-but-its-registry-leaked-sensitive-info/5264152)
