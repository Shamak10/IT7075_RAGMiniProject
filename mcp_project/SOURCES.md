# Sources

The four knowledge-base sections I added to `project_cve_kb.md` are written in my own words, from the pages below. Every CVE named in them is real. The host `10.0.0.33` and its banners are invented. Its banners use real product versions, but no real system was scanned.

## Knowledge-base sections I added

| Section | Covers | Sources |
|---|---|---|
| `nginx 1.18.0` | CVE-2021-23017, a 1-byte memory overwrite in the nginx DNS resolver; 0.6.18 through 1.20.0; fixed in 1.20.1 and 1.21.0; CVSS 3.1 7.7 (High) | NVD: https://nvd.nist.gov/vuln/detail/CVE-2021-23017 · nginx security advisory: https://mailman.nginx.org/pipermail/nginx/2021-May/060720.html · nginx security advisories list: https://nginx.org/en/security_advisories.html |
| `PostgreSQL 9.6` | End of life on 11 November 2021, with 9.6.24 as the final release; CVE-2022-1552 as an example of a later fix that 9.6 never received | PostgreSQL release announcement (14.1 … 9.6.24, 9.6 EOL): https://www.postgresql.org/about/news/postgresql-141-135-129-1114-1019-and-9624-released-2349/ · PostgreSQL versioning policy: https://www.postgresql.org/support/versioning/ · CVE-2022-1552: https://www.postgresql.org/support/security/CVE-2022-1552/ and https://nvd.nist.gov/vuln/detail/CVE-2022-1552 · CWE-1104, Use of Unmaintained Third Party Components: https://cwe.mitre.org/data/definitions/1104.html |
| `OpenSSH 8.9p1` | CVE-2024-6387 (regreSSHion), a signal-handler race in sshd; 8.5p1 through 9.7p1; fixed in 9.8p1; CVSS 3.1 8.1 (High); Ubuntu 22.04 fix 1:8.9p1-3ubuntu0.10 (USN-6859-1); LoginGraceTime 0 mitigation | NVD: https://nvd.nist.gov/vuln/detail/CVE-2024-6387 · OpenSSH 9.8 release notes: https://www.openssh.com/txt/release-9.8 · Qualys advisory: https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt · Ubuntu: https://ubuntu.com/security/CVE-2024-6387 and https://ubuntu.com/security/notices/USN-6859-1 |
| `Apache httpd 2.4.50` | CVE-2021-42013, the incomplete fix for CVE-2021-41773; path traversal and RCE with mod_cgi; 2.4.49 and 2.4.50 only; fixed in 2.4.51; CVSS 3.1 9.8 (Critical); in CISA KEV | Apache httpd 2.4 vulnerabilities: https://httpd.apache.org/security/vulnerabilities_24.html · NVD: https://nvd.nist.gov/vuln/detail/CVE-2021-42013 · CISA Known Exploited Vulnerabilities: https://www.cisa.gov/known-exploited-vulnerabilities-catalog |

## My host, 10.0.0.33

| Banner | Why it is realistic |
|---|---|
| `OpenSSH 8.9p1 Ubuntu 3ubuntu0.6` | The OpenSSH package in Ubuntu 22.04 LTS, at a patch level from before the July 2024 regreSSHion fix (fixed in `3ubuntu0.10`): https://launchpad.net/ubuntu/+source/openssh |
| `Apache httpd 2.4.50 ((Unix))` | What a source-built Apache 2.4.50 reports, for example the official `httpd:2.4.50` container image: https://hub.docker.com/_/httpd |
| `Redis key-value store 4.0.14` | A real Redis 4.0 release (March 2019). It is covered by the course's `Redis 4.0` section, an unauthenticated instance reachable over the network: https://redis.io/docs/latest/operate/oss_and_stack/management/security/ |

## A note on the course ground truth

`expected_cves.json` credits the `MySQL 5.5` section (CVE-2012-2122) as the right answer for `MySQL 5.5.40`. NVD describes CVE-2012-2122 as affecting "5.5.x before 5.5.24", so 5.5.40 is not affected. I left the course row unchanged so my numbers stay comparable with the starter's. The report discusses it. NVD: https://nvd.nist.gov/vuln/detail/CVE-2012-2122

## Course material

The MCP lecture notebooks (`mcp_build_server.ipynb`, `mcp_client_agent.ipynb`), the starter notebook, server, knowledge base and `expected_cves.json`, from https://github.com/li2cc/IT7075-Applied-AI-for-Cybersecurity (module `07_MCP`).

## Use of AI tools

I used Claude (Anthropic) to help write code, check CVE details against the sources above, and organize the results, as the assignment allows. I checked each section against its sources myself.
