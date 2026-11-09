# An alert-triage agent with LangGraph

A small LangGraph agent decides whether each security alert should be escalated to an analyst or
closed. I measure the two ways it can be wrong: a **missed** incident and an **over-escalated**
routine alert. I build the Lecture 3 graph (state, a keyword `classify` node, a conditional edge, a
tool node, memory by `thread_id`) and run it on 12 labelled alerts I wrote myself. Then I change the
word list one step at a time, and then the graph itself. I add a `context` node that calls two tools
I wrote, an asset inventory and a change calendar, plus a router with new branches. Widening the word
list alone catches all six incidents but over-escalates five of six routine alerts. With the context
node, the same list catches all six and over-escalates one. A third change lets the router read the
case's memory, so a quiet follow-up alert on an open case is escalated. The same alert on a fresh
thread is closed. Everything runs offline in plain Python: no API key, no model, no GPU, so every
number here is exact and reproducible.

Shamak Patel · IT7075 Applied AI for Cybersecurity · University of Cincinnati · Fall 2026

## What is here

| Path | What it is |
|---|---|
| `agent_notebook.ipynb` | The notebook, saved with all outputs. Parts 1-8 are the course starter with the five TODOs completed; Part 9 onward is my own work |
| `my_alerts.json` | My 12 labelled alerts (6 escalate, 6 close), each with the reason an analyst would make that call; 7 are hard cases |
| `SOURCES.md` | Background reading for each alert type (Microsoft event docs, MITRE ATT&CK, AWS docs) |
| `results_mine.csv` | My results: 10 settings, one change at a time, with caught / missed / over-escalated and the IDs of the alerts that were wrong |
| `alerts.json`, `results.csv` | The course's 12 alerts and the Part 7 keyword sweep on them |
| `requirements.txt` | `langgraph` (plus `grandalf` to draw the graph) |

## The graph

```
classify --> context --(router)--> investigate         (escalate; calls lookup_cve)
             |                 \-> quick_close         (close: no keyword)
             |                 \-> close_with_context  (close: lab/honeypot host, or approved change on this host)
             |                 \-> add_to_case         (escalate: no keyword, but this thread has an open escalation)
             calls lookup_asset(host) and check_change(ticket, host)
```

## Results on my 12 alerts

| Row | Keyword list | Graph | Caught | Missed | Over-escalated |
|---|---|---|---|---|---|
| 2 | lecture (5 words) | Lecture 3 graph | 2/6 | 4/6 | 3/6 |
| 3 | wider (8) | Lecture 3 graph | 4/6 | 2/6 | 3/6 |
| 4 | widest (13) | Lecture 3 graph | 6/6 | 0/6 | 5/6 |
| 5 | widest (13) | + context node, `lookup_asset` (first host named) | 6/6 | 0/6 | 5/6 |
| 6 | widest (13) | + `lookup_asset` on the host the alert is on | 6/6 | 0/6 | 4/6 |
| **7** | **widest (13)** | **+ `check_change` (both tools)** | **6/6** | **0/6** | **1/6** |
| 8 | wider (8) | as row 7 | 4/6 | 2/6 | 0/6 |

All 10 rows are in `results_mine.csv`. The Lecture 3 agent reproduces the starter's expected numbers
on the course alerts (caught 3/6, missed 3/6, over-escalated 2/6).

## Run it

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace agent_notebook.ipynb
```

Or open the notebook in VS Code or Colab and Run All. It takes a few seconds.
