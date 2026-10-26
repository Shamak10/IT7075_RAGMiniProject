# NIST SP 800-63B-4: Passwords (Section 3.1.1)

A password (sometimes referred to as a passphrase or, if numeric, a personal identification number [PIN]) is a secret value intended to be chosen and either memorized or recorded by the subscriber. Passwords must be of sufficient effective strength and secrecy that it would be impractical for an attacker to guess or otherwise discover the correct secret value. A password is “something you know.” Passwords are not phishing-resistant.

## Password Authenticators (3.1.1.1)

Passwords SHALL either be chosen by the subscriber or assigned randomly by the CSP. If the CSP disallows a chosen password because it is on a blocklist of commonly used, expected, or compromised values (see Sec. 3.1.1.2), the subscriber SHALL be required to choose a different password. Other composition requirements for passwords SHALL NOT be imposed.

## Password Verifiers (3.1.1.2)

The following requirements apply to passwords.

1. Verifiers and CSPs SHALL require passwords that are used as a single-factor authentication mechanism to be a minimum of 15 characters in length. Verifiers and CSPs MAY allow passwords that are only used as part of multi-factor authentication processes to be shorter but SHALL require them to be a minimum of eight characters in length.
2. Verifiers and CSPs SHOULD permit a maximum password length of at least 64 characters.
5. Verifiers and CSPs SHALL NOT impose other composition rules (e.g., requiring mixtures of different character types) for passwords.
6. Verifiers and CSPs SHALL NOT require subscribers to change passwords periodically. However, verifiers SHALL force a change if there is evidence that the authenticator has been compromised.
7. Verifiers and CSPs SHALL NOT permit the subscriber to store a hint (e.g., a reminder of how the password was created) that is accessible to an unauthenticated claimant.
8. Verifiers and CSPs SHALL NOT prompt subscribers to use knowledge-based authentication (KBA) (e.g., “What was the name of your first pet?”) or security questions when choosing passwords.
9. Verifiers SHALL request the password to be provided in full (not a subset of it) and SHALL verify the entire submitted password (e.g., not truncate it).
