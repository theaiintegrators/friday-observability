<p align="left">
  <a href="https://github.com/theaiintegrators">
    <img src="https://img.shields.io/badge/Friday-Ecosystem-4B8BF5" />
  </a>
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img/shields.io/badge/python-3.9%20|%203.10%20|%203.11-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/docs-in%20progress-lightgrey" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</p>

# 🔍 friday-observability  
_Tracing, analytics, and introspection for enterprise multi-agent workflows_

Friday Observability provides structured tracing and workflow analytics for Friday Core.  
It is inspired by modern observability systems used in:

- **LangFuse-style workflow tracing**  
- **LangSmith / DeepEval evaluation pipelines**  
- **Microsoft Agent Framework debugging**  
- **OpenTelemetry-style instrumentation**  
- **MCP tool interaction tracing**  

It enhances Friday Core with deep insights into agent behaviour, routing decisions, timing, and evaluation results.

---

# 🌟 Why Enterprise Observability Matters

Multi-agent workflows are complex networks of decisions.  
Without observability, teams cannot:

- understand why agents chose certain actions  
- reconstruct workflow timelines  
- debug failures or incorrect transitions  
- measure latency or bottlenecks  
- inspect LLM inputs and outputs  
- track evaluation score history  

Friday Observability adds **full execution transparency**, allowing teams to monitor, debug, and optimise workflows.

---

# ✨ Features

- **Structured workflow traces**  
- **LangFuse-compatible events & metadata**  
- **Agent-level logs & routing logs**  
- **LLM input/output recording**  
- **Execution timing metrics**  
- **Workflow-wide trace graphs**  
- **Attachable observability hooks**  
- **Low overhead & production-ready design**  

---

# 🏛 Architecture Overview

Friday Observability integrates deeply with Friday Core:

```
Event → Agent → Observability → Evaluation → Router → Next Agent
```

### **Core Components**

#### **TraceRecorder**
Captures structured multi-agent execution traces.

#### **LangfuseClientWrapper**
Sends workflow metadata, timing, and evaluation results to LangFuse.

#### **MetricsCollector**
Captures step latency, workflow duration, and agent performance metrics.

#### **WorkflowLogger**
Lightweight logger for debugging or on-prem deployments.

---

# 📁 Repository Structure

```
friday-observability/
  ├── friday_observability/
  │     ├── base.py
  │     ├── trace_recorder.py
  │     ├── langfuse_client.py
  │     ├── metrics.py
  │     ├── logger.py
  │     └── types.py
  ├── examples/
  ├── tests/
  └── README.md
```

---

# 🚀 Example: Logging Agent Transitions

```python
from friday import Orchestrator
from friday_observability import TraceRecorder

recorder = TraceRecorder()

orchestrator = Orchestrator(agents=agents)
orchestrator.with_observability(recorder)

result = orchestrator.run("start")
recorder.dump()  # print structured workflow trace
```

---

# 🤝 Example: LangFuse Integration

```python
from friday import Orchestrator
from friday_observability import LangfuseClient

langfuse = LangfuseClient(
    public_key="LF_PUBLIC",
    secret_key="LF_SECRET",
    host="https://cloud.langfuse.com"
)

orchestrator = Orchestrator(agents=agents)
orchestrator.with_observability(langfuse)

orchestrator.run("start")
```

This records:

- agent start/end events  
- inputs & outputs  
- evaluation scores  
- timing & latency  
- error metadata  
- workflow graphs  

---

# 🔗 Works Seamlessly with Friday Core & Friday Evaluation

Friday Observability completes the **Orchestration + Evaluation + Observability triad**:

```
        ┌──────────────────┐
        │   Observability  │
        └──────▲───────────┘
               │
 Orchestration │ Evaluation
        ┌──────┴──────┐
        │   Friday    │
        └─────────────┘
```

---

# 🧪 Roadmap

- JSON trace export  
- LangFuse auto-enrichment  
- Visual workflow timeline UI  
- OpenTelemetry integration  
- Real-time workflow dashboards  
- Error fingerprinting & classification  

---

# 🔭 Vision

Friday Observability aims to make large multi-agent workflows:

- transparent  
- debuggable  
- evaluable  
- auditable  
- safe for enterprise deployment  

---

# 📄 License  
MIT License
