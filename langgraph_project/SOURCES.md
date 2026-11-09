# Sources

The 12 alerts in `my_alerts.json` are written in my own words. None of them is copied from a real
console or an employer's system. Host names, user names and change tickets are invented. The pages
below are what I read to make each alert type realistic.

| Alert | Alert type | Background reading |
|---|---|---|
| M01 | EDR ransomware behaviour (mass file renames) | MITRE ATT&CK T1486, Data Encrypted for Impact: https://attack.mitre.org/techniques/T1486/ |
| M02 | Windows Security event 1102, audit log cleared | Microsoft, "1102(S): The audit log was cleared": https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-1102 · ATT&CK T1070.001, Clear Windows Event Logs: https://attack.mitre.org/techniques/T1070/001/ |
| M03 | AWS CloudTrail, IAM `AttachUserPolicy` with `AdministratorAccess` | AWS IAM API reference, AttachUserPolicy: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachUserPolicy.html · ATT&CK T1098, Account Manipulation: https://attack.mitre.org/techniques/T1098/ |
| M04 | EDR process tree, Office spawning encoded PowerShell | ATT&CK T1566.001, Spearphishing Attachment: https://attack.mitre.org/techniques/T1566/001/ · ATT&CK T1059.001, PowerShell: https://attack.mitre.org/techniques/T1059/001/ |
| M05 | Entra ID sign-in risk, impossible / atypical travel | Microsoft Entra ID Protection, risk detections: https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks · ATT&CK T1078, Valid Accounts: https://attack.mitre.org/techniques/T1078/ |
| M06 | Zeek DNS log, DNS tunnelling | ATT&CK T1071.004, Application Layer Protocol: DNS: https://attack.mitre.org/techniques/T1071/004/ · Zeek documentation: https://docs.zeek.org/ |
| M07 | Nessus scheduled vulnerability scan | Tenable Nessus documentation: https://docs.tenable.com/nessus/ |
| M08 | Windows Security event 4732, member added to a local group | Microsoft, "4732(S): A member was added to a security-enabled local group": https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4732 |
| M09 | Defender detection of the EICAR test file | EICAR anti-malware test file: https://www.eicar.org/download-anti-malware-testfile/ |
| M10 | Windows Security event 4740, account locked out | Microsoft, "4740(S): A user account was locked out": https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4740 |
| M11 | AWS GuardDuty `Recon:EC2/PortProbeUnprotectedPort` | AWS GuardDuty EC2 finding types: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html |
| M12 | DLP / egress-volume rule on a backup server | ATT&CK T1048, Exfiltration Over Alternative Protocol (what the rule is meant to catch): https://attack.mitre.org/techniques/T1048/ |

Course material used: the IT7075 LangGraph lecture notebooks (`langgraph_state_nodes.ipynb`,
`langgraph_branch_tools.ipynb`) and the Mini-Project starter notebook, from
https://github.com/li2cc/IT7075-Applied-AI-for-Cybersecurity (module `06_LangGraph`).

Use of AI tools: I used Claude (Anthropic) to help write code, draft alert wording and organize
results, as the assignment allows. I checked every alert's label myself.
