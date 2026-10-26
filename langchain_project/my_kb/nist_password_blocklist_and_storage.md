# NIST SP 800-63B-4: Password Blocklists, Password Managers, and Storage (Section 3.1.1.2, continued)

## Blocklists

When processing a request to establish or change a password, verifiers SHALL compare the prospective secret against a blocklist that contains known commonly used, expected, or compromised passwords. The entire password SHALL be subject to comparison, not substrings or words that might be contained therein. For example, the list may include:

- Passwords obtained from previous breach corpuses
- Dictionary words
- Context-specific words, such as the name of the service, the username, and derivatives thereof

If the chosen password is found on the blocklist, the CSP SHALL require the subscriber to select a different secret and SHALL provide the reason for rejection. Since the blocklist is used to defend against brute-force attacks and unsuccessful attempts are rate-limited, the blocklist SHOULD be of sufficient size to prevent subscribers from choosing passwords that attackers are likely to guess before reaching the attempt limit.

## Password managers

Verifiers SHALL allow the use of password managers and autofill functionality. Verifiers SHOULD permit claimants to use the “paste” function when entering a password to facilitate password manager use when password autofill APIs are unavailable. Password managers have been shown to increase the likelihood that subscribers will choose stronger passwords, particularly if the password managers include password generators.

## Storing passwords

Verifiers SHALL store passwords in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using a suitable password hashing scheme. Password hashing schemes take a password, a salt, and a cost factor as inputs and generate a password hash. Their purpose is to make each password guess more expensive for an attacker who has obtained a hashed password file, thereby making the cost of a guessing attack high or prohibitive.

The salt SHALL be at least 32 bits in length and chosen to minimize salt value collisions among stored hashes (i.e., to prevent multiple subscriber accounts from having the same hashed password). Both the salt value and the resulting hash SHALL be stored for each password.
