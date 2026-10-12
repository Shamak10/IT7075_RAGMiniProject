# NIST SP 800-63B-4: Rate Limiting (Section 3.2.2) and Authentication Assurance Levels

## Rate Limiting (Throttling)

When required by the authenticator type descriptions in Sec. 3.1, the verifier SHALL implement controls to protect against online guessing attacks. Unless otherwise specified in the description of a given authenticator, the verifier SHALL limit consecutive failed authentication attempts using a specific authenticator on a single subscriber account to no more than 100 by disabling that authenticator.

The limit of 100 attempts is an upper bound, and agencies MAY impose lower limits. The limit of 100 was chosen to balance the likelihood of a correct guess (e.g., 100 attempts against a six-digit decimal OTP authenticator output) versus the potential need for account recovery when the limit is exceeded.

Additional techniques MAY be used to reduce the likelihood that an attacker will lock the legitimate claimant out due to rate limiting. These include:

- Requiring the claimant to complete a bot detection and mitigation challenge before attempting authentication
- Requiring the claimant to wait after a failed attempt for a period of time that increases as the subscriber account approaches its maximum allowance for consecutive failed attempts (e.g., 30 seconds up to an hour)

## Authentication Assurance Levels

Authentication Assurance Level 1: AAL1 provides basic confidence that the claimant controls an authenticator bound to the subscriber account being authenticated. AAL1 requires only single-factor authentication using a wide range of available authentication technologies.

Authentication Assurance Level 2: AAL2 provides high confidence that the claimant controls one or more authenticators bound to the subscriber account being authenticated. Proof of the possession and control of two distinct authentication factors is required. Applications assessed at AAL2 must offer a phishing-resistant authentication option.

Authentication Assurance Level 3: AAL3 provides very high confidence that the claimant controls one or more authenticators bound to the subscriber account being authenticated. Authentication at AAL3 is based on the proof of possession of a key through the use of a public-key cryptographic protocol. AAL3 authentication requires a phishing-resistant authenticator with a non-exportable authentication key.
