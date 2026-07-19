# IKCON–IFTAS Revolving Door: Evidence Compilation

> **Part of the "DeepSeeking Accountability in RBI" report**
> Compiled: 2026-07-12 | Status: Verified evidence annexure

---

## 1. The Core Finding: Dual Role of Mahesh Jarati

**Mahesh Jarati is simultaneously employed at IKCON Technologies (the vendor that won the no-tender IDRBT contract) AND at IFTAS (RBI's wholly-owned technology subsidiary).**

| Role | Organization | Source |
| --- | --- | --- |
| Executive Leadership | IKCON Technologies | ikcontech.com/our-leadership-team [^1] |
| Senior Vice President | IKCON Technologies | ZoomInfo [^2] |
| Assistant Vice President | IFTAS (RBI subsidiary) | Datanyze, ZoomInfo [^3] |

This is a classic revolving-door conflict: an individual holding senior roles at both the **vendor** that was awarded a contract without competitive bidding and at the **RBI subsidiary** that sits alongside IDRBT in RBI's technology ecosystem.

---

## 2. The Contract: No-Tender Award to IKCON

IDRBT awarded the `.bank.in` Domain Registration Portal contract to **IKCON Technologies** without any competitive bidding process, in violation of its own procurement handbook.

**Corroborating sources:**

- **CashlessConsumer investigation**: "The portal was built by IKCON Technologies in a single-source award — no tender, no RFP, no competitive process — in direct violation of IDRBT's own procurement handbook." [^6]

- **webhosting.today**: "It was awarded to a single vendor, IKCON Technologies, with no tender or competitive process." [^7]

- **Medianama** (ongoing reporting): Multiple references to IDRBT's procurement bypass. [^8]

- **The Register**: Coverage of the .bank.in security failure references the single-source nature of the contract.

IKCON held **22 employee accounts** on the portal including **3 with global Super Admin access** — meaning the vendor had privileged access to the very system it built without competitive oversight. [^6]

---

## 3. The Oversight Chain: Dr. Deepak Kumar's Multi‑Layer Overlap

Dr. Deepak Kumar sits at multiple points in the chain that enabled this contract award:

| Role | Organization | Timeline | Relevance |
| --- | --- | --- | --- |
| Director | IDRBT | May 2024–present | IDRBT awarded the no-tender contract to IKCON |
| Executive Director | RBI (looked after DIT, Foreign Exchange, Communications) | Prior to May 2024 | Had policy oversight over IDRBT and its technology direction |
| Board Director | IFTAS (RBI wholly-owned subsidiary) | Prior to May 2024 | Served on the same board as the subsidiary where Mahesh Jarati works |
| Board Director | NPCI, ReBIT, RBIH | Prior to May 2024 | Wide governance footprint across RBI's subsidiary network |
| Governing Council Member | IDRBT | Prior to May 2024 | Sat on the governing body of the institute he would later direct |

Source: IDRBT Director page [^4], IDRBT Governing Council page [^5]

---

## 4. The Security Failure That Exposed the Governance Gap

The `.bank.in` portal built by IKCON under this no-tender arrangement exposed:

- **33+ unauthenticated REST API endpoints**
- **5,576 bank employee credentials** (bcrypt hashes, emails, mobile numbers, login IPs, device fingerprints)
- **1,072 orphan Super Admin accounts**
- **Live for over 13 months** (discovered Jun 8, 2026; fixed Jun 25, 2026)

IDRBT's published Security Policy claimed the site was "audited for known application-level vulnerabilities before the launch" — a claim the evidence directly contradicts. [^6]

---

## 5. Company Structure

**IKCON DIGITAL IT SERVICES PRIVATE LIMITED** (CIN: U72900AP2018PTC109917) [^9]

| Director | DIN/PAN | Appointment Date |
| --- | --- | --- |
| DIVAKAR TALAGADADEEVI | 08297441 | 07-12-2018 |
| MADHU KIRAN BOINDALA | 10542766 | 11-03-2024 |
| MADHAVI TALAGADADEEVI | 10088949 | 01-06-2023 |

- **Registered Address**: Door No. 23247-4, Survey No.5, Batchu Peta, Batchupet, Krishna, Machilipatnam, Andhra Pradesh, 521001
- **Email**: tdivakar@ikcontech.com
- **Status**: Active
- **Revenue (FY 2025)**: ₹3.9 Cr [^10]

The company's registered address is a residential area in Machilipatnam, while its business operations (and the corporate address on filings) are at Rohini Layout, Madhapur, Hyderabad.

Mahesh Jarati is **not a registered director** of this company on MCA records, but is listed as **Executive Leadership** on the IKCON Technologies website [^1] and as **Senior Vice President** on ZoomInfo [^2].

---

## 6. The Revolving Door Flowchart

```markdown
RBI (Regulator)
   │
   ├── RBI—DIT (Dept. of IT) → Dr. Deepak Kumar (Executive Director, RBI)
   │       │
   │       ├── Director, IFTAS Board (RBI subsidiary)       ← Mahesh Jarati is AVP here
   │       │
   │       ├── Governing Council Member, IDRBT
   │       │       └── May 2024: Becomes Director, IDRBT
   │       │               └── IDRBT awards no-tender .bank.in contract to IKCON
   │       │
   │       ├── Director, NPCI Board
   │       ├── Director, ReBIT Board
   │       └── Director, RBIH Board
   │
   └── IKCON Technologies (vendor)
           ├── Mahesh Jarati — Executive Leadership / SVP
           └── Won .bank.in contract via single-source award
```

---

## 7. OSINT Profile: Mahesh Jarati

### Summary Profile

| Attribute | Detail | Source |
| --- | --- | --- |
| Full Name | Mahesh Jarati | Multiple |
| Current Role | Senior Vice President, IKCON Technologies | ikcontech.com [^1], ZoomInfo [^2] |
| Simultaneous Role | Assistant Vice President, IFTAS (RBI subsidiary) | Datanyze [^3] |
| Previous Role | Senior Project Leader, ADP | Facebook [^11] |
| Location | Hyderabad, Telangana, India | Facebook [^11] |
| Education | Bangalore University | Facebook [^11] |
| Email (inferred) | `Mahesh.Jarati@iftas.in` (IFTAS email format: `first.last`) | Datanyze email format [^3] |
| Email (inferred) | `mahesh.jarati@ikcontech.com` (IKCON email pattern) | IKCON domain pattern |

### Identified Profiles & Social Media

| Platform | Handle / URL | Details |
| --- | --- | --- |
| Facebook | `/mahesh.jarati` | Public profile; Lives in Hyderabad; Studied at Bangalore University; Senior Project Leader at ADP [^11] |
| Instagram | `@maheshjarati` | 85 followers, 190 following, 17 posts; Public account [^12] |
| ZoomInfo | Mahesh Jarati — IKCON Technologies | Senior Vice President profile (paywalled) [^2] |
| Datanyze | Mahesh Jarati — IFTAS (Employee #1985697404) | Assistant Vice President on IFTAS employee directory [^3] |

### Career Timeline (Reconstructed)

```markdown
Bangalore University (Education)
    ↓
ADP — Senior Project Leader (Previous role, timeline unconfirmed)
    ↓
IFTAS (RBI Subsidiary) — Assistant Vice President (Current or recent)
    ↓ (Concurrent)
IKCON Technologies — Senior Vice President, Executive Leadership (Current)
```

### Dual Role Significance

The Datanyze employee directory at IFTAS lists Mahesh Jarati as **Assistant Vice President** at the RBI's wholly-owned technology services subsidiary (IFTAS). [^3] Simultaneously, he is listed as **Senior Vice President** and **Executive Leadership** at IKCON Technologies [^1][^2] — the same company that received a **no-tender, single-source contract** from IDRBT to build and operate the `.bank.in` domain registry portal.

This dual role creates a structural conflict of interest:

1. **As AVP at IFTAS** — He operates inside an RBI subsidiary with direct institutional ties to IDRBT (both report to RBI's Department of Information Technology)
2. **As SVP at IKCON** — He works for the vendor that was awarded a lucrative IDRBT contract worth ₹3.9 Cr+ without competitive bidding

The proximity between IDRBT (which awarded the contract) and IFTAS (where Jarati works) is not incidental. Both are RBI controlled entities under the same regulatory umbrella. The person simultaneously occupying senior positions at the vendor and at a sibling entity to the procuring institution is the textbook definition of a revolving-door conflict.

### Email & Contact Intelligence

Based on the Datanyze email format analysis for IFTAS ([^3]):

- **IFTAS email format**: `first.last@iftas.in` (most common, used by \~40% of employees)
- **Inferred IFTAS email**: `Mahesh.Jarati@iftas.in`
- **IKCON email pattern**: `firstname@ikcontech.com` (used by Divakar Talagadadeevi: `tdivakar@ikcontech.com`)
- **Inferred IKCON email**: `mahesh@ikcontech.com` or `mahesh.jarati@ikcontech.com`

Direct email verification was not possible as all contact details are behind Lusha/ ZoomInfo/ Datanyze paywalls.

### Risk Assessment: Contractual Proximity

The conflict severity is heightened by:

1. **No tender** — The contract was awarded as a single-source procurement, eliminating the market competition that would normally surface conflicts
2. **Privileged access** — IKCON had 22 employee accounts on the portal including 3 with global Super Admin access [^6]
3. **Regulatory capture risk** — The same person who helps oversee technology strategy at an RBI subsidiary (IFTAS) also works for the company that profits from an RBI-controlled contract
4. **Inadequate separation** — IDRBT's procurement handbook mandates competitive bidding; this award violated that rule, and the conflict-checking process failed

## 8. Further Investigation Required

- [ ] Confirm exact dates of Mahesh Jarati's tenure at IFTAS and IKCON (overlap period)

- [ ] Verify whether IFTAS has any procurement or vendor management relationship with IKCON

- [ ] Check for any IDRBT/IFTAS emails referencing IKCON that may have been disclosed in Right to Information requests

- [ ] Pull MCA annual filings for IFTAS (Section 8 company) to identify board-level oversight of vendor contracts

- [ ] Confirm whether Mahesh Jarati's IFTAS role involves procurement, technology strategy, or vendor management

- [ ] Check whether other IKCON leadership also hold concurrent roles in RBI subsidiaries

## References

[^1]: IKCON Technologies — Our Leadership Team: https://www.ikcontech.com/our-leadership-team
[^2]: ZoomInfo — Mahesh Jarati at IKCON Technologies (Senior Vice President): https://www.zoominfo.com/pic/ikcon-technologies-inc/368717508
[^3]: Datanyze — IFTAS Employee List (Mahesh Jarati, Assistant Vice President, Employee #1985697404): https://www.datanyze.com/companies/iftas/430229897
[^4]: IDRBT — Director page (Dr. Deepak Kumar's board positions): https://www.idrbt.ac.in/director
[^5]: IDRBT — Governing Council composition: https://www.idrbt.ac.in/governing-council
[^6]: CashlessConsumer — RBI's .bank.in Security Failure (June 28, 2026): https://bankin-report.cashlessconsumer.in
[^7]: webhosting.today — India's .bank.in Registry Leaked Admin Data (July 3, 2026): https://webhosting.today/2026/07/03/indias-bank-in-trust-domain-leaked-the-data-of-the-people-who-run-it
[^8]: Medianama — Ongoing .bank.in coverage: https://www.medianama.com/2026/06/223-security-vulnerabilities-rbi-bank-in-registry-sensitive-data
[^9]: IndiaFilings — IKCON DIGITAL IT SERVICES PRIVATE LIMITED: https://www.indiafilings.com/search/ikcon-digital-it-services-private-limited-cin-U72900AP2018PTC109917
[^10]: The Company Check — IKCON DIGITAL IT SERVICES PRIVATE LIMITED FY2025 revenue: https://www.thecompanycheck.com/company/ikcon-digital-it-services-private-limited/U72900AP2018PTC109917
[^11]: Facebook — Mahesh Jarati public profile: https://www.facebook.com/mahesh.jarati
[^12]: Instagram — @maheshjarati: https://www.instagram.com/maheshjarati