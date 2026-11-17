"""Mini-Project 5 — your MCP server (SIMULATED, safe, offline).

A real Model Context Protocol server built with FastMCP, exposing:

    Tools:
      port_scan(target)        simulated nmap-style scan of a lab host
      lookup_cve(service)      the LECTURE version -- naive token matching
      lookup_cve_v2(service)   YOUR version (TODO 1) -- product + version aware
      list_targets()           the hosts this server knows about
      assess_finding(service)  MY tool (Part 8) -- CVE, severity and fix per advisory,
                               with an explicit "unassessed" answer for knowledge gaps
    Resource:
      kb://cve                 the CVE knowledge base as text (TODO 2)

SAFETY / ETHICS
---------------
`port_scan` does NOT touch the network. It returns canned output for fictional lab
hosts so the project is reproducible and safe. Real scanning is shown in a comment
only, and you must run it ONLY against systems you are explicitly authorized to test.

The client launches this file over stdio, so it starts a FRESH process every time --
edit this file, re-run the client cell, and your change is live. No restart needed.
"""
import os
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("cyber-recon-project", log_level="WARNING")

# --- the knowledge base: YOUR editable copy (Part 8 asks you to extend it) ----
def _kb_path():
    # Part 8 (mine): the notebook can point the server at another copy of the
    # knowledge base (the course original, or one with a deliberately vague entry)
    # by setting CVE_KB_FILE in the server's environment. Unset = the normal file.
    override = os.environ.get("CVE_KB_FILE")
    if override:
        return Path(override)
    here = Path(__file__).parent
    for candidate in (here / "project_cve_kb.md", here / ".." / "project_cve_kb.md"):
        if candidate.exists():
            return candidate
    return here / "project_cve_kb.md"


def _load_kb_sections():
    """GIVEN: parse the knowledge base into {section title: full section text}."""
    path = _kb_path()
    if not path.exists():
        return {}
    sections = {}
    for chunk in path.read_text(encoding="utf8").split("#"):
        chunk = chunk.strip()
        if chunk:
            sections[chunk.splitlines()[0].strip()] = chunk
    return sections


# --- the simulated lab ------------------------------------------------------
_SIMULATED_HOSTS = {
    "10.0.0.5": [
        "21/tcp   open  ftp      vsftpd 2.3.4",
        "22/tcp   open  ssh      OpenSSH 7.2p2 Ubuntu",
        "80/tcp   open  http     Apache httpd 2.4.49",
    ],
    "10.0.0.8": [
        "139/tcp  open  netbios-ssn Samba smbd 3.5.0",
        "3306/tcp open  mysql    MySQL 5.5.40",
    ],
    "10.0.0.12": [
        "23/tcp   open  telnet   Linux telnetd",
        "443/tcp  open  ssl/http Apache httpd 2.2.8 (OpenSSL 1.0.1)",
        "6379/tcp open  redis    Redis key-value store 4.0.9",
    ],
    "10.0.0.20": [
        "21/tcp   open  ftp      ProFTPD 1.3.5",
        "80/tcp   open  http     nginx 1.18.0",
        "5432/tcp open  postgres PostgreSQL 9.6.24",
    ],
    # Part 8 (mine): an invented internal app server. Ubuntu 22.04's stock OpenSSH,
    # an Apache built from source and never upgraded, and a Redis left on the LAN.
    # Redis is covered by the course knowledge base; the other two were not until I
    # added entries for them (CVE-2024-6387 and CVE-2021-42013).
    "10.0.0.33": [
        "22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.6",
        "80/tcp   open  http     Apache httpd 2.4.50 ((Unix))",
        "6379/tcp open  redis    Redis key-value store 4.0.14",
    ],
}


@mcp.tool()
def port_scan(target: str) -> str:
    """Run a (simulated) network port scan of a target host and return open ports
    with detected service names and versions, in nmap style.

    SIMULATED: returns canned data for known lab hosts; no packets are sent.
    """
    if target in _SIMULATED_HOSTS:
        header = f"Nmap scan report for {target}\nPORT     STATE SERVICE  VERSION"
        return header + "\n" + "\n".join(_SIMULATED_HOSTS[target])
    return f"Nmap scan report for {target}\n(no open ports in the simulated environment)"

    # --- Real scan (authorized targets ONLY) ---
    # import subprocess
    # return subprocess.run(["nmap", "-sV", target],
    #                       capture_output=True, text=True, timeout=120).stdout


@mcp.tool()
def list_targets() -> str:
    """List the demo hosts this server can scan (simulated lab environment)."""
    return "Known simulated targets: " + ", ".join(_SIMULATED_HOSTS)


@mcp.tool()
def lookup_cve(service: str) -> str:
    """Look up known vulnerabilities for a service or product name (e.g.
    'vsftpd 2.3.4', 'Apache 2.4.49') in the local knowledge base.

    THE LECTURE VERSION -- left here unchanged so you can measure against it.
    It matches when two or more words of the query appear anywhere in a section,
    which is why it both misses services it knows and answers with the wrong
    version. Part 7 shows you exactly where.
    """
    sections = _load_kb_sections()
    query = service.lower()
    tokens = [t for t in query.replace("/", " ").split() if t]
    hits = [body for title, body in sections.items()
            if title.lower() in query or sum(tok in (title + " " + body).lower()
                                             for tok in tokens) >= 2]
    return "\n\n".join(hits) if hits else f"No known CVEs for '{service}' in the knowledge base."


@mcp.tool()
def lookup_cve_v2(service: str) -> str:
    """Look up known vulnerabilities for a service, matching on PRODUCT and
    VERSION so a 2.2.8 server is never answered with a 2.4.49 advisory.

    Give this docstring some thought: for an MCP client, the docstring IS the
    contract. It is all an LLM sees when it decides whether to call your tool.
    """
    sections = _load_kb_sections()
    text = service.lower()
    hits = []
    for title, body in sections.items():
        product = title.lower().split()[0]              # "apache", "redis", "telnet"
        version = re.search(r"\d[\d.p]*", title)         # "2.4.49", "4.0", or None

        ###################  TODO 1 — a version-aware match  ###################
        # WHAT: decide whether this KB section really describes `service`.
        #
        # Two conditions, both on the LOWERCASED service text:
        #   1. the product name appears in it   ->  product in text
        #   2. the version matches: either the title has NO version at all
        #      (version is None), or the title's version string appears in the
        #      service text  ->  version.group() in text
        #
        # Set `match` to True only when BOTH hold, then append `body` to `hits`.
        #
        # WHY this fixes real bugs, all three visible in Part 7:
        #   * "Linux telnetd"  vs section "Telnet service" -> product "telnet" IS
        #     in "linux telnetd", and the section has no version, so it matches.
        #     The lecture version missed it even though the entry exists.
        #   * "Redis key-value store 4.0.9" vs "Redis 4.0" -> "4.0" appears in
        #     "4.0.9", so it matches.
        #   * "Apache httpd 2.2.8 (OpenSSL 1.0.1)" vs "Apache httpd 2.4.49" ->
        #     "2.4.49" does NOT appear, so it is correctly rejected; and the
        #     OpenSSL 1.0.1 section matches instead, which is the right answer.
        ################

        match = product in text and (version is None or version.group() in text)
        if match:
            hits.append(body)

    return "\n\n".join(hits) if hits else f"No known CVEs for '{service}' in the knowledge base."


# --- Part 8: my own tool -----------------------------------------------------
_SEVERITY_RANK = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def _version_in(version, text):
    """True when `version` appears in `text` as a whole version number: '4.0'
    matches '4.0.14' and '1.0.1' matches '1.0.1f', but '4.0' does not match
    '7.4.0', and the '4' that the title regex reads out of 'Apache Log4j 2.14'
    does not match 'Apache httpd 2.4.49'. lookup_cve_v2's plain substring test
    gets both of those wrong."""
    return re.search(r"(?<![\d.])" + re.escape(version) + r"(?!\d)", text) is not None


def _parse_section(title, body):
    """Pull the CVE, severity and fix out of one knowledge-base section."""
    cves = re.findall(r"CVE-\d{4}-\d{4,}", body)
    if "no single cve" in body.lower() or not cves:
        cve = "none (a configuration or lifecycle weakness, not a single CVE)"
    else:
        cve = cves[0]
    sev = re.search(r"Severity:\s*([A-Za-z]+)", body)
    fix = re.search(r"Remediation:\s*(.+)", body)
    return {"title": title, "cve": cve,
            "severity": sev.group(1).lower() if sev else "unknown",
            "fix": fix.group(1).strip() if fix else "(no remediation in the entry)"}


@mcp.tool()
def assess_finding(service: str) -> str:
    """Assess one service banner against the local CVE knowledge base and report
    each matching advisory with its CVE, severity and fix, most severe first.

    Call it once per open port after port_scan, passing the product-and-version
    part of the scan line exactly as printed, for example
    'Apache httpd 2.4.50 ((Unix))' or 'OpenSSH 8.9p1 Ubuntu 3ubuntu0.6'.
    Read only: it reads the local knowledge base and nothing else. It sends no
    packets and writes no files.

    How to read the answer:
      - 'match: version-confirmed' means the entry's product name and its
        version number both appear in the banner.
      - 'match: UNCONFIRMED' means the entry names no version, so it matches
        every banner for that product. Check the running version by hand
        before acting on it.
      - An answer that starts with 'No known CVEs' means UNASSESSED: the
        knowledge base has no matching entry. It does NOT mean the service is
        safe, and it should be reported as a gap, not as a clean result.

    Limits: matching is on names and version strings, not version ranges, so a
    vulnerable version the knowledge base does not name is missed; distribution
    backports (for example an Ubuntu package that carries a fix) are not
    recognised; 'cve' is the first CVE the entry cites.
    """
    text = service.lower()
    found = []
    for title, body in _load_kb_sections().items():
        product = title.lower().split()[0]
        version = re.search(r"\d[\d.p]*", title)
        if not re.search(r"\b" + re.escape(product), text):
            continue
        if version is None:
            basis = ("UNCONFIRMED (the entry names no version, so it matches every "
                     "'%s' banner; check the version by hand)" % product)
        elif _version_in(version.group(), text):
            basis = "version-confirmed ('%s' and '%s' both in the banner)" % (product, version.group())
        else:
            continue
        item = _parse_section(title, body)
        item["basis"] = basis
        found.append(item)

    if not found:
        return (f"No known CVEs for '{service}' in the knowledge base. UNASSESSED: the "
                "knowledge base has no entry for this product and version. This is a "
                "gap in the data, not evidence that the service is safe.")

    found.sort(key=lambda f: -_SEVERITY_RANK.get(f["severity"], 0))
    lines = [f"Assessment of '{service}': {len(found)} advisory(ies), highest severity "
             f"{found[0]['severity'].upper()}"]
    for f in found:
        lines += [f"- section: {f['title']}",
                  f"  cve: {f['cve']}",
                  f"  severity: {f['severity']}",
                  f"  match: {f['basis']}",
                  f"  fix: {f['fix']}"]
    return "\n".join(lines)


###################  TODO 2 — expose the knowledge base as a RESOURCE  ###################
# WHAT: return the whole knowledge-base file as text.
#
# HOW (the Lecture 2 server shape): the decorator is already written for you --
# @mcp.resource("kb://cve") is what gives the resource its URI. You supply the body:
#
#       return _kb_path().read_text(encoding="utf8")
#
# WHY a resource and not a tool: a tool is something the agent *does*; a resource is
# something it *reads*. Same data, different primitive -- the client fetches this one
# with read_resource("kb://cve") instead of call_tool.
################

@mcp.resource("kb://cve")
def cve_kb() -> str:
    """The full CVE knowledge base as Markdown text (an MCP *resource*)."""
    return _kb_path().read_text(encoding="utf8")


if __name__ == "__main__":
    # stdio is the MCP default: the client launches this script as a subprocess and
    # talks to it over stdin/stdout. mcp.run(transport="streamable-http") would serve
    # over HTTP instead -- same tools, different transport (Lecture 2, section 4).
    mcp.run()
