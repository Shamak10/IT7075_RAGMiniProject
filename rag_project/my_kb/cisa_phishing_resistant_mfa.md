# CISA Fact Sheet: Implementing Phishing-Resistant MFA (October 2022)

## Overview

MFA is a security control that requires a user to present a combination of two or more different authenticators (something you know, something you have, or something you are) to verify their identity for login. With MFA enabled, if one factor, such as a password, becomes compromised, unauthorized users will be unable to access the account if they cannot also provide the second factor. However, not all forms of MFA are equally secure. Some forms are vulnerable to phishing, “push bombing” attacks, exploitation of Signaling System 7 (SS7) protocol vulnerabilities, and/or SIM Swap attacks. While any form of MFA is better than no MFA and will reduce an organization’s attack surface, phishing-resistant MFA is the gold standard and organizations should make migrating to it a high priority effort.

## Cyber threats to MFA

- Phishing. A threat actor sends an email to a target that convinces the user to visit a threat actor-controlled website that mimics a company’s legitimate login portal. The user submits their username, password, as well as the 6-digit code from their mobile phone’s authenticator app.
- Push bombing (also known as push fatigue). Cyber threat actors bombard a user with push notifications until they press the “Accept” button, thereby granting threat actor access to the network.
- Exploitation of SS7 protocol vulnerabilities. Cyber threat actors exploit SS7 protocol vulnerabilities in communications infrastructure to obtain MFA codes sent via text message (SMS) or voice to a phone.
- SIM Swap. Cyber threat actors convince cellular carriers to transfer control of the user’s phone number to a threat actor-controlled SIM card, which allows the threat actor to gain control over the user’s phone.

## MFA forms, strongest to weakest (Table 1)

1. Phishing-resistant MFA (FIDO/WebAuthn authentication, PKI-based). Resistant to phishing. Push bombing, SS7, and SIM swap attacks are not applicable.
2. App-based authentication (one-time password, mobile push notification with number matching) and token-based OTP. Vulnerable to phishing attacks. Resistant to push bombing.
3. Mobile application push notification without number matching. Vulnerable to push bombing attacks as well as user error.
4. SMS or Voice. Vulnerable to phishing, SS7, and SIM swap attacks. This form of MFA should only be used as a last resort MFA option.

## FIDO/WebAuthn authentication

The only widely available phishing-resistant authentication is FIDO/WebAuthn authentication. WebAuthn authenticators can either be separate physical tokens (called “roaming” authenticators) connected to a device via USB or near-field comms (NFC), or embedded into laptops or mobile devices as “platform” authenticators.
