
<p align="left">
  <a href="https://github.com/theaiintegrators">
    <img src="https://img.shields.io/badge/Friday-Ecosystem-4B8BF5" />
  </a>
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/python-3.10%20|%203.11-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</p>

# 🔍 Friday Observability  
### _Metrics, Insights, and Monitoring for Multi-Agent AI Systems_

Friday Observability is a lightweight, open-source observability layer designed for **AI agents**, **LLM toolchains**, and **multi-agent orchestration systems**.

This module provides **real-time metrics**, **agent analytics**, and **runtime introspection** through a clean, reproducible **Prometheus + Grafana** monitoring stack.

It is built as part of the **Friday Ecosystem**, but can be used independently for any agent-based or LLM-based system.

---

# 🌟 Why Observability for Agents?

Modern AI systems behave like distributed, dynamic graphs of decisions:

- Agents call tools  
- Tools call models  
- Models generate reasoning chains  
- Supervisors route tasks  
- Autonomous decisions emerge  

Without observability, teams cannot:

- See what agents are doing  
- Measure performance  
- Debug unexpected routing  
- Identify latency bottlenecks  
- Detect failing agents  
- Benchmark quality  

Friday Observability solves this with a **fully open-source**, **dockerized**, **plug-and-play** monitoring stack.

---

# ✨ Features

### ✅ Real-time Agent Metrics
Track per-agent:

- Request rate  
- Latency (p50 / p95 / p99)  
- Error rate  
- Throughput  
- Live activity timeline  

### ✅ Beautiful Grafana Dashboards
Out-of-the-box dashboards:

- **Friday Overview Dashboard**  
- **Agent Deep-Dive Dashboard**  

Both load automatically on Docker startup.

### ✅ Prometheus Integration
A tiny Python emitter exposes:

```
/metrics
```

…allowing Prometheus to scrape structured agent metrics.

### ✅ Fully Reproducible Environment
Anyone can simply run:

```
docker compose up -d
```

…and immediately get:

- Prometheus running  
- Grafana running  
- Datasource auto-provisioned  
- Dashboards auto-provisioned  
- Metrics flowing in real time  

### ✔ No manual setup  
### ✔ No UID mismatch  
### ✔ No hidden configuration  

---

# 🏛 Architecture Overview

```
┌──────────────┐      ┌────────────────┐      ┌───────────────┐
│ Agent System │ ───► │ Metrics Emitter│ ───► │  Prometheus   │
└──────────────┘      └────────────────┘      └───────┬───────┘
                                                      │
                                                      ▼
                                                ┌────────────┐
                                                │  Grafana   │
                                                │ Dashboards │
                                                └────────────┘
```

Friday Observability does **not** require any private Friday code.  
It simply listens to metrics and visualizes them.

---

# 📦 Repository Structure

```
friday-observability-public/
  ├── docker-compose.yml
  ├── prometheus.yml
  ├── emit_metrics.py
  ├── grafana/
  │     ├── provisioning/
  │     │      ├── dashboards.yml
  │     │      └── datasources.yml
  │     └── dashboards/
  │            ├── demo_dashboard.json
  │            └── agent_deep_dive.json
  ├── LICENSE
  └── README.md
```

---

# 🚀 Quick Start

### Clone the repo

```
git clone https://github.com/theaiintegrators/friday-observability
cd friday-observability
```

### Start the observability stack

```
docker compose up -d
```

### Open Grafana  
→ http://localhost:3000  
→ Username: **admin**  
→ Password: **admin**

You will see **two dashboards already working**, powered by live metrics.

---

# 📊 Dashboard Highlights

## 1️⃣ Friday Overview Dashboard  
Shows system-wide health:

- Total requests  
- Active agents  
- Error rate  
- Real-time throughput  
- Latency over time  
- CPU & Memory signals  

## 2️⃣ Agent Deep-Dive Dashboard  
Detailed visibility by agent:

- Requests per second  
- p50 / p95 / p99 latency  
- Error breakdown  
- Slowest agents  
- High-volume agents  
- Combined performance table  

These dashboards auto-load on container startup.

---

# 🧩 Metric Endpoints

The metrics emitter produces Prometheus metrics such as:

```
friday_agent_requests_total{agent="SearchAgent"} 42
friday_agent_latency{agent="MathAgent"} 0.12
friday_agent_errors_total{agent="RAGAgent"} 1
```

You can extend `emit_metrics.py` to track additional custom signals.

---

# 🛡️ Safety: What This Repo Does *Not* Include

This public version **does not include**:

- Private Friday Core logic  
- Proprietary agent orchestration code  
- MS Agent Framework integrations  
- Internal evaluation pipelines  
- Any non-public IP  

Only **the observability scaffolding** is provided.

This ensures the repo is:

- Safe  
- Open-source friendly  
- Fully reproducible  
- Technically impressive  

…but **without exposing private Friday implementation**.

---

# 🧪 Roadmap

- OTEL / Trace ingestion  
- Workflow timeline visualization  
- Log aggregation  
- RAG performance metrics  
- Anomaly detection  
- LLM token & cost analytics  

---

# 🤝 Contributing  
PRs are welcome!  
Friday Observability aims to set a standard for **AI agent observability**.

---

# 📄 License  
MIT License

