# Cloud Database Python Toolkit

A practical collection of multi-cloud database automation scripts, operational utilities, and core Python data-structure patterns built for **Cloud Database Engineer** workflows across **AWS (Aurora / RDS)** and **GCP (Cloud SQL / AlloyDB)**.

Built on **14+ years of production Linux and MySQL/Aurora database engineering**, focusing on reliability, automated maintenance, observability, and zero-downtime operations.

---

## Repository Structure

```text
cloud-db-python-toolkit/
├── README.md            # Project overview and setup instructions
├── pyproject.toml       # Python dependencies managed via uv / pip
├── .gitignore           # Excludes virtual environments, secrets, and cache artifacts
├── aws/                 # AWS Aurora MySQL/PostgreSQL automation, RDS snapshot retention, Secrets Manager
├── gcp/                 # GCP Cloud SQL & AlloyDB operational scripts, IAM auth, Query Insights parsers
├── common/              # Cloud-agnostic DBA tools (slow query log aggregator, Slack alerts, config diff)
└── dsa-patterns/        # Core Python data structure & algorithm patterns (hashing, sliding window, intervals)
```

---

## Focus Areas

- **Cloud Database Automation (`aws/` & `gcp/`):** Programmatic snapshot lifecycle management, secret rotation checks, failover verification, and security group audits using `boto3` and Google Cloud SDKs.
- **Database Reliability & Telemetry (`common/`):** Slow query log fingerprinting, replication lag alerting via Slack webhooks, connection spike detection, and `.cnf` / parameter-group diff utilities.
- **Core Python & Problem Solving (`dsa-patterns/`):** Clean, readable implementations of essential algorithmic patterns applied to log parsing, time-series metrics, and maintenance window scheduling.

---

## Local Setup (macOS / Linux)

This repository uses [`uv`](https://astral.sh) for fast, isolated Python dependency management.

```bash
# 1. Clone the repository
git clone git@github.com:Sibashish/cloud-db-python-toolkit.git
cd cloud-db-python-toolkit

# 2. Create virtual environment and install dependencies
uv sync

# 3. Run a script inside the managed environment
uv run python common/slow_query_parser.py
```

*(Alternative using standard `venv` and `pip`)*:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

