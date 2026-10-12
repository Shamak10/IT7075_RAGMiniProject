# CISA Fact Sheet: Implementing Number Matching in MFA Applications (October 2022)

## Overview

Mobile push-notification-based MFA is a form of application-based MFA that authenticates via a mobile application notifying a user’s smart phone. After receiving the prompt (aka “push” notification), the user presses “approve” on the notification to grant themselves access to their account. MFA fatigue, also known as “push bombing,” occurs when a cyber threat actor bombards a user with mobile application push notifications until the user either approves the request by accident or out of annoyance with the nonstop notifications.

If an organization that uses mobile push-notification-based MFA is unable to implement phishing-resistant MFA, CISA recommends using number matching to mitigate MFA fatigue. Although number matching is not as strong as phishing-resistant MFA, it is one of the best interim mitigation for organizations who may not immediately be able to implement phishing-resistant MFA.

## The problem

Cyber threat actors who have obtained a user’s password know they can enter it into an identity platform that uses mobile push-notification-based MFA to generate hundreds of prompts on the user’s device over a short period of time. This activity understandably annoys the user, who may—accidentally or from MFA fatigue—press accept to stop the prompts. As a result of any of these possible scenarios, the user unknowingly grants the cyber threat actor access to their account.

## Mitigation

Number matching is a setting that forces the user to enter numbers from the identity platform into their app to approve the authentication request. The number matching requirement mitigates MFA fatigue by:

- Requiring access to the login screen to approve requests. Users cannot approve requests without entering the numbers on the login screen.
- Discouraging prompt spam. Each prompt generates a unique set of numbers for every login request. As the user cannot accept the prompts without knowing the numbers, generating multiple prompts is not effective.

## Best practices

Investigate denied push notifications. When a user denies an MFA requests, they should alert their IT security team, who should investigate the root cause. MFA checks are done after the first factor (e.g., the user’s password) is satisfied, so denied MFA requests could mean the user’s password is compromised.
