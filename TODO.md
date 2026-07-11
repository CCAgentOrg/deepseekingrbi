# DeepSeeking RBI — Project TODO

> **Status**: Core report (~970 lines, 97+ footnotes) drafted. Remaining work organized below.

---

## Phase 1: Strengthen References (Active)

- [ ] **RTI filing**: File RTI with RBI asking for IDRBT procurement records, byelaw amendment details, IKCON contract value. Route through RTI Online / RBI CPIO.
- [ ] **MCA/ROC**: Pull ReBIT, IFTAS, RBIH annual filings from MCA portal. Extract board composition, auditor reports, related-party transactions.
- [ ] **IKCON forensic**: Full GSTIN-based contract trail — search other IDRBT/IFTAS contracts held by IKCON. Cross-reference directors with other RBI entity vendors.
- [ ] **ZoomInfo/LinkedIn**: Full career timeline for Mahesh Jarati (IFTAS → IKCON gap), Deepak Kumar's board appointment dates across all entities.
- [ ] **Governing Council minutes**: Track down any published GC minutes for IDRBT (annual reports, parliament questions). Verify byelaw amendment timeline.
- [ ] **IDRBT procurement manual**: Download and diff the Purchase Manual versions (pre/post 2022) to identify threshold changes.

## Phase 2: Investigative Deep-Dives

- [ ] **NPCI for-profit conversion**: Governance implications of Section 8 → for-profit with same board structure. Track shareholder proposal progress.
- [ ] **ReBIT governance**: No published board minutes, auditor independence check. ROC filing analysis.
- [ ] **IFTAS clawback completeness**: What else was transferred from IDRBT to IFTAS beyond INFINET/SFMS/Cloud? Were these valued at market price?
- [ ] **RBI Fintech Dept vs RBIH**: Map exact overlap of mandates, personnel, budgets between the internal department and external Section 8 entity.
- [ ] **Global comparison**: How do other central banks (BoE, Fed, ECB) structure their technology subsidiaries? What governance safeguards exist abroad that are missing here?

## Phase 3: Publication

- [ ] **Final report PDF**: Typeset the full report using book-typesetting skill (pandoc + Eisvogel) for professional PDF distribution.
- [ ] **Interactive website**: Build on zo.space or as a Zo Site. Map visualisation of entity network, searchable reference database, downloadable sources.
- [ ] **GitHub repository**: Publish the full report + annexures + data as an open repository. Add README with executive summary.
- [ ] **Media outreach**: Pitch as follow-up to Medianama's .bank.in coverage. Emphasise governance angle, not just security.
- [ ] **RTI campaign**: Coordinate with transparency orgs (Transparency International India, SHRIR, NCPRI) to file multi-pronged RTI on all entities.

## Phase 4: Website Build

- [ ] Choose platform: zo.space (quick) vs Zo Site (custom deps, domain). Decision criteria: do we need server-side data processing?
- [ ] Entity network diagram (interactive D3.js): Show connections between entities, shared directors, overlapping mandates.
- [ ] Reference database: DuckDB-backed API endpoint on zo.space serving the reference matrix + footnotes.
- [ ] Full-text search across all chapters.
- [ ] Download links: PDF report + source data (CSV/JSON).

## Phase 5: Long-Term Monitoring

- [ ] **IDRBT monitor skill**: Set up scheduled agent to scrape IDRBT website, track procurement postings, new governing council members, annual report releases.
- [ ] **ReBIT security disclosures**: Track cybersecurity incidents/breaches at RBI entities.
- [ ] **NPCI conversion**: Monitor for board resolutions, government approvals, shareholder meetings.
- [ ] **Periodic update**: Update the report quarterly with new findings.

---

## Current File Inventory

| File | Lines | Description |
|------|-------|-------------|
| `chapters/rbi_governance.md` | 376 | Main report — 3 chapters + refs + appendix |
| `chapters/rbi-subsidiaries-survey.md` | 294 | Historical survey of all RBI entities |
| `chapters/DeepakKumar.md` | 189 | Raw procurement investigation notes |
| `annexures/reference-matrix.md` | 117 | Cross-verified source grading for each claim |
| `AGENTS.md` | 55 | Project index and agent instructions |
| `TODO.md` | — | This file |

---

*Generated: 2026-07-11. Check off items as completed. Re-prioritise as needed.*
