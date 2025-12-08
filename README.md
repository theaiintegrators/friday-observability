# 📊 Friday Observability

*Monitoring, metrics & dashboards for AI agents*

<p align="left">
  <a href="https://github.com/theaiintegrators"><img src="https://img.shields.io/badge/Friday--Ecosystem-4B8BF5" /></a>
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/python-3.10_3.11-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</p>

------------------------------------------------------------------------

## 🌟 Overview

**Friday Observability** provides metrics, dashboards and Prometheus
integration for:

-   AI agents
-   orchestration systems
-   LLM tools
-   multi-agent workflows

------------------------------------------------------------------------

## 📘 Friday Observability

![Friday Observability](./docs/02-public-friday-observability.png)

------------------------------------------------------------------------

## ✨ Features

-   Real-time Prometheus metrics
-   Auto-provisioned Grafana dashboards
-   Dockerized stack
-   Latency, throughput & error analytics
-   Extensible metrics emitter

------------------------------------------------------------------------

## 🏛 Architecture

    Agents → Metrics Emitter → Prometheus → Grafana Dashboards

------------------------------------------------------------------------

## 📚 Repository Structure

    friday-observability/
      ├── docker-compose.yml
      ├── prometheus.yml
      ├── grafana/
      ├── emit_metrics.py
      ├── LICENSE
      └── README.md

------------------------------------------------------------------------

## 🚀 Quick Start

``` bash
git clone https://github.com/theaiintegrators/friday-observability
cd friday-observability

docker compose up -d
```

Grafana → http://localhost:3000
user: admin / pass: admin

------------------------------------------------------------------------

## 🧭 Roadmap

-   MCP tool integration
-   Parallel execution patterns
-   Workflow visualizer
-   LangFuse auto-enrichment
-   Built‑in safety evaluators
-   Friday CLI
-   Deployment templates

------------------------------------------------------------------------

## 🔭 Vision

Friday aims to make AI systems:

-   **Predictable**
-   **Testable**
-   **Observable**
-   **Enterprise-ready**

With a code-first, extensible design that scales from prototypes to full
production platforms.

------------------------------------------------------------------------

## 📄 License

MIT License
Copyright © 2025
The AI Integrators

------------------------------------------------------------------------

## 💬 Contact & Contributions

-   Open an Issue or Discussion
-   PRs welcome
-   https://github.com/theaiintegrators