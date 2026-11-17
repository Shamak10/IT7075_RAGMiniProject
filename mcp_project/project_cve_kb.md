# vsftpd 2.3.4
The vsftpd 2.3.4 FTP server (commonly seen on port 21) shipped with a malicious backdoor introduced into the source distribution. Connecting with a username ending in ":)" opens a command shell on TCP port 6200, granting remote command execution as root. Tracked as CVE-2011-2523. Severity: critical. Remediation: upgrade to a clean, vendor-verified vsftpd build and verify package checksums; never run software from unverified mirrors.

# OpenSSH 7.2p2
OpenSSH versions before 7.7 (including the 7.2 series often seen on port 22) are affected by a username enumeration weakness, CVE-2018-15473. By measuring response timing differences to malformed authentication requests, an attacker can determine which usernames exist on the system, aiding password-guessing and spear-phishing. Severity: medium. Remediation: upgrade OpenSSH to 7.7 or later, enforce key-based authentication, and rate-limit authentication attempts with fail2ban.

# Apache httpd 2.4.49
Apache HTTP Server 2.4.49 (port 80/443) contains a path-traversal flaw, CVE-2021-41773. A crafted URL using encoded "../" sequences can read files outside the document root, and when mod_cgi is enabled it escalates to remote code execution. Severity: critical. Remediation: upgrade to Apache 2.4.51 or later, disable directory aliasing you do not need, and ensure "require all denied" is set on the filesystem root.

# Apache Log4j 2.14
Applications using Apache Log4j 2 versions 2.0-beta9 through 2.14.1 are vulnerable to Log4Shell, CVE-2021-44228. If attacker-controlled text is logged, a JNDI lookup string such as "${jndi:ldap://...}" causes the server to fetch and execute remote code. This often surfaces through web services on ports 80/443/8080. Severity: critical. Remediation: upgrade Log4j to 2.17.1 or later, set log4j2.formatMsgNoLookups=true as a stopgap, and block outbound LDAP/RMI from servers.

# Samba 3.5.0
Samba file-sharing services (ports 139/445) from 3.5.0 up to 4.6.4 are vulnerable to CVE-2017-7494, nicknamed SambaCry. An authenticated client that can write to a share can upload and trigger a shared library, achieving remote code execution on the server. Severity: critical. Remediation: patch Samba to a fixed release, add "nt pipe support = no" to smb.conf as mitigation, and restrict share write access.

# Microsoft SMBv1
Windows hosts exposing SMBv1 (port 445) are vulnerable to EternalBlue, CVE-2017-0144, addressed by bulletin MS17-010. A malformed SMBv1 packet causes a buffer overflow leading to remote code execution; this was the propagation vector for the WannaCry and NotPetya worms. Severity: critical. Remediation: apply MS17-010, disable SMBv1 entirely, and block port 445 at the network perimeter.

# ProFTPD 1.3.5
ProFTPD 1.3.5 (port 21) with the mod_copy module enabled is vulnerable to CVE-2015-3306. The SITE CPFR and SITE CPTO commands can be used without authentication to copy files anywhere the daemon can write, enabling attackers to plant a web shell or read sensitive files. Severity: high. Remediation: upgrade ProFTPD, disable mod_copy unless required, and run the FTP daemon under a restricted account.

# OpenSSL 1.0.1
Services using OpenSSL 1.0.1 through 1.0.1f for TLS (ports 443, 993, 995, and others) are vulnerable to Heartbleed, CVE-2014-0160. A malformed TLS heartbeat request makes the server return up to 64 KB of process memory per request, which can leak private keys, session cookies, and credentials. Severity: critical. Remediation: upgrade OpenSSL to 1.0.1g or later, revoke and reissue affected certificates and keys, and force user password resets.

# MySQL 5.5
MySQL and MariaDB database servers (port 3306) in several 5.5/5.6 builds are affected by CVE-2012-2122, an authentication-bypass flaw. On vulnerable systems a timing issue lets a repeated login with an incorrect password occasionally succeed, granting access without valid credentials. Severity: high. Remediation: patch the database, never expose 3306 to untrusted networks, and require TLS plus strong, unique account passwords.

# Redis 4.0
Redis instances (port 6379) left without authentication and reachable over the network can be abused for remote code execution. An attacker writes a malicious module or crafted RDB/SSH key file via unauthenticated commands and loads it. There is no single CVE; this is a configuration weakness widely exploited in the wild. Severity: critical. Remediation: require a strong "requirepass", bind Redis to localhost or a private interface, enable protected-mode, and disable the MODULE and CONFIG commands.

# PHP-CGI
Web servers running php-cgi (ports 80/443) are vulnerable to CVE-2012-1823, an argument-injection flaw. Query strings beginning with "?-" are passed to the PHP binary as command-line switches, allowing source disclosure or remote code execution. Severity: critical. Remediation: upgrade PHP, use PHP-FPM instead of php-cgi, and add a web-server rule that rejects request strings starting with a dash.

# Telnet service
A telnet service (port 23) transmits all data, including usernames and passwords, in cleartext with no encryption. Anyone able to observe the traffic can capture credentials, and telnet is frequently left enabled with default credentials on routers, switches, and IoT devices. Severity: high. Remediation: disable telnet entirely and replace it with SSH; if a serial-console fallback is required, isolate it on a dedicated management network.

# nginx 1.18.0
nginx 1.18.0 (web server and reverse proxy, ports 80/443) is affected by CVE-2021-23017, an off-by-one error in the DNS resolver code (ngx_resolver_copy). When the "resolver" directive is configured, a crafted DNS response can overwrite one byte of memory, which crashes a worker process and may allow remote code execution. Every nginx release from 0.6.18 through 1.20.0 is affected. Severity: high (CVSS 3.1 7.7). Remediation: upgrade to nginx 1.20.1 or 1.21.0 or later; until then remove the "resolver" directive if it is not needed, or point it only at trusted internal DNS servers.

# PostgreSQL 9.6
PostgreSQL 9.6 (port 5432) reached end of life on 11 November 2021, and 9.6.24 is the last release of the branch. There is no single CVE: the finding is unsupported software (CWE-1104). Security fixes published after that date, for example CVE-2022-1552 (autovacuum, REINDEX and other maintenance commands running outside the security-restricted sandbox, fixed only in 10.21, 11.16, 12.11, 13.7 and 14.3), are neither built nor tested for 9.6, so this server's exposure to every later flaw is unknown and will never be patched. Severity: high. Remediation: upgrade to a supported major version with pg_upgrade or a dump and restore; until then accept connections on 5432 only from the application hosts that need it and require password authentication in pg_hba.conf instead of trust.

# OpenSSH 8.9p1
OpenSSH 8.9p1 (port 22, the version Ubuntu 22.04 ships) is affected by CVE-2024-6387, nicknamed regreSSHion: a race condition in the sshd SIGALRM handler, a regression of the 2006 bug CVE-2006-5051, lets an unauthenticated attacker who leaves connections open past LoginGraceTime run code as root on glibc-based Linux. OpenSSH portable 8.5p1 through 9.7p1 is affected; exploitation is a timing race that needs thousands of attempts. Severity: high (CVSS 3.1 8.1). Remediation: upgrade to OpenSSH 9.8p1, or to a distribution build that carries the fix (Ubuntu 22.04: 1:8.9p1-3ubuntu0.10 or later, USN-6859-1); as a stopgap set LoginGraceTime 0 in sshd_config, which trades the code-execution risk for a denial-of-service risk.

# Apache httpd 2.4.50
Apache HTTP Server 2.4.50 (ports 80/443) is affected by CVE-2021-42013. The 2.4.50 fix for the CVE-2021-41773 path traversal was incomplete: double URL-encoded "../" sequences can still map URLs to files outside the directories configured by Alias-like directives, and with mod_cgi enabled this becomes remote code execution. Only 2.4.49 and 2.4.50 are affected, and only where those files are not protected by "Require all denied". It is listed in CISA's Known Exploited Vulnerabilities catalog. Severity: critical (CVSS 3.1 9.8). Remediation: upgrade to Apache 2.4.51 or later, keep "Require all denied" on the filesystem root, and disable mod_cgi where it is not needed.
