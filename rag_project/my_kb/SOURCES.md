# Sources for my_kb/

All five documents are excerpts of publications by US federal agencies (NIST and CISA). Works of the US
government are not subject to copyright in the United States; NIST states this on the publication itself and asks
for attribution, which this file provides.

**What I changed:** the wording is NIST's and CISA's own. To keep the knowledge base near the 10,000-character
target I cut sentences, paragraphs and whole sections; I added the Markdown headings; and I put each paragraph and
list item on one line so a line break cannot split an evidence phrase. Other edits are listed per file below.
Nothing was reworded to make a question easier to answer.

| File | Source | Sections used |
|---|---|---|
| `nist_password_rules.md` | NIST SP 800-63B-4 | 3.1.1, 3.1.1.1, start of 3.1.1.2 |
| `nist_password_blocklist_and_storage.md` | NIST SP 800-63B-4 | rest of 3.1.1.2 |
| `nist_rate_limiting_and_aal.md` | NIST SP 800-63B-4 | 3.2.2, and the AAL summary in the Introduction |
| `cisa_phishing_resistant_mfa.md` | CISA fact sheet *Implementing Phishing-Resistant MFA* | Overview, Cyber Threats to MFA, Table 1, FIDO/WebAuthn |
| `cisa_number_matching.md` | CISA fact sheet *Implementing Number Matching in MFA Applications* | Overview, The Problem, Mitigation, Best Practices |

## NIST SP 800-63B-4

Temoshok, D., et al. *Digital Identity Guidelines: Authentication and Authenticator Management*. NIST Special
Publication 800-63B-4, National Institute of Standards and Technology, July 2025.
<https://doi.org/10.6028/NIST.SP.800-63B-4> (PDF:
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf>)

- `nist_password_rules.md`: the definition of a password in 3.1.1 (the paragraph on activation secrets is left
  out, so its last sentence now closes the first paragraph), 3.1.1.1 without its pointer to Appendix A, and the
  numbered verifier requirements of 3.1.1.2.
  Requirements 3 and 4 (accepted characters) are left out; the remaining items keep NIST's numbers 1, 2 and 5-9.
- `nist_password_blocklist_and_storage.md`: the blocklist paragraphs, the password-manager paragraph and the first
  storage paragraphs of 3.1.1.2. Left out: the boxed note on blocklist size; the paragraphs on guiding users,
  on rate limiting, on showing the password and on mistyping; the sentences on the cost factor, SP 800-132,
  output length and recording the hashing scheme; and the paragraph on keyed hashing with a secret key. The
  citation marker `[Managers]` is removed.
- `nist_rate_limiting_and_aal.md`: 3.2.2 without the sentences on disabling several authenticators and rebinding,
  the risk-based-authentication bullet, and the closing paragraph on resetting the retry count. The three AAL
  paragraphs are from the high-level summary in the Introduction, with cross-references such as "(see Sec. 3.2.5)"
  removed, and without the AAL1 recommendation to offer MFA and the closing sentences of AAL1 and AAL3.

**Deliberately left out:** reauthentication and session timeouts (Sections 2.1.3, 2.2.3, 2.3.3 and 5.2). Question
Q8 in `goldset.json` asks about them, to test whether the system refuses a question that sounds covered but is not.

## CISA fact sheets

Cybersecurity and Infrastructure Security Agency. *Implementing Phishing-Resistant MFA*. Fact sheet, October 2022.
<https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf>

- `cisa_phishing_resistant_mfa.md`: selected sentences of the Overview; the four threats, with their introductory
  definitions shortened (two sentences re-capitalised where their opening clause was cut); Table 1 flattened into
  a numbered list giving each row's MFA forms, the main points of its "Threat" column and, for SMS or voice, the
  table's "last resort" sentence; and the FIDO/WebAuthn paragraph without the sentences on its history and browser
  support, with the two kinds of authenticator joined into one sentence. Left out: the PKI section, the implementation-planning
  sections and the resources list.

Cybersecurity and Infrastructure Security Agency. *Implementing Number Matching in MFA Applications*. Fact sheet,
October 2022.
<https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf>

- `cisa_number_matching.md`: selected sentences of the Overview, The Problem (without its footnote and one
  sentence), Mitigation (without the screenshots and the list of vendor product names), and one of the two best
  practices ("Investigate denied push notifications").
