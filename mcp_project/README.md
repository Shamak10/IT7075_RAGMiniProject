# Auditing an MCP server for CVE lookups

This project tests a small Model Context Protocol (MCP) server that scans simulated lab hosts and looks up CVEs in a local knowledge base. The question is what the server tells a client when its answer is quietly wrong. I finished the course server and client (five TODOs). Then I added a host of my own (`10.0.0.33`), a tool of my own (`assess_finding`, which reports the CVE, severity and fix and states when a service is unassessed), and four knowledge-base sections for real products with real CVEs. I swept 14 services with three lookup tools against three versions of the knowledge base, and sorted every answer into four buckets: grounded, blind spot, wrong version, or true gap. Better matching removed the blind spots. New knowledge removed the true gaps. A vague entry with no version brought a wrong-version answer back. Everything runs offline: no network traffic, no model, no API key, so every number is exact and reproducible.

Shamak Patel · IT7075 Applied AI for Cybersecurity · University of Cincinnati · Fall 2026

## What is here

| Path | What it is |
|---|---|
| `mcp_notebook.ipynb` | The notebook, saved with all outputs. Parts 1-7 are the course starter with TODOs 3-5 completed. Part 8 onward is my own client and measurement |
| `project_mcp_server.py` | The MCP server (FastMCP, stdio). TODOs 1-2 completed, plus my host `10.0.0.33`, my tool `assess_finding`, and a `CVE_KB_FILE` override so the notebook can serve other copies of the knowledge base |
| `project_cve_kb.md` | The knowledge base. The course's 12 sections, plus my four at the end |
| `expected_cves.json` | Ground truth: the section each of the 14 services should get. My edits are listed in its `changes_by_me` field |
| `SOURCES.md` | Citations for the four sections I wrote and for my host's banners |
| `results_mine.csv` | My results: 14 services × 3 knowledge-base states, with each tool's bucket (42 rows) |
| `results.csv` | Part 5's course table (the four course hosts, two tools) |
| `requirements.txt` | `mcp<2` (the starter uses the 1.x API) and `ipykernel` |

## Tools the server advertises

| Tool | What it does |
|---|---|
| `port_scan(target)` | Simulated nmap-style scan. It sends no packets |
| `list_targets()` | The five simulated hosts |
| `lookup_cve(service)` | The lecture version: two or more words in common. Kept as the baseline |
| `lookup_cve_v2(service)` | TODO 1: the product name and the title's version must both appear in the banner |
| `assess_finding(service)` | Mine: whole-version matching, the CVE, severity and fix for each match, `UNCONFIRMED` when the entry has no version, and `UNASSESSED` instead of a silent "no CVEs" |

It also exposes one resource, `kb://cve` (TODO 2).

## Results (whole lab, 14 services: grounded / blind spot / wrong version / true gap)

| Knowledge base | `lookup_cve` | `lookup_cve_v2` | `assess_finding` |
|---|---|---|---|
| course, as shipped | 6 / 3 / 2 / 3 | 9 / 0 / 2 / 3 | 10 / 0 / 0 / 4 |
| + my four sections | 8 / 3 / 3 / 0 | 12 / 0 / 2 / 0 | 14 / 0 / 0 / 0 |
| + `# OpenSSH 8.9p1` made vague | 8 / 3 / 3 / 0 | 11 / 0 / 3 / 0 | 13 / 0 / 1 / 0 |

On the four course hosts and the course knowledge base, Part 5's scorer reproduces the starter's expected output exactly (6 / 2 / 1 / 2 and 9 / 0 / 0 / 2). My stricter scorer finds one more wrong answer from `lookup_cve_v2`: it returns the Log4Shell advisory for `Apache httpd 2.4.49`, because the version regex reads the "4" in "Log4j".

## Run it

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace mcp_notebook.ipynb
```

Or open the notebook in VS Code and Run All. It takes about ten seconds. The client starts the server itself, so nothing needs to be running first. To start the server by hand: `python project_mcp_server.py` (it waits on stdin for an MCP client).

Safety: every tool is simulated or read only. `port_scan` returns canned output for invented hosts, and the real `nmap` call stays commented out.
