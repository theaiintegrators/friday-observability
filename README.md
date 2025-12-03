# 📦 friday-observability
### _Tracing, Metrics & Debugging for Multi-Agent Workflows_

Friday Observability provides **tracing, logging, and monitoring capabilities** for multi-agent workflows running on Friday Core.

It enables developers and enterprises to:

- Understand agent behaviour  
- Inspect event transitions  
- Trace workflow failures  
- Measure execution timing  
- Capture LLM input/output  
- Send structured traces to observability tools (e.g., Langfuse)  

---

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/Status-Under%20Development-orange.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

---

## 🌟 Why Observability Matters

Multi-agent systems are **complex**. Without observability:

- You cannot debug routing decisions  
- You cannot know why an agent failed  
- You cannot detect loops or stuck workflows  
- You cannot measure performance  
- You cannot inspect LLM inputs and outputs  
- You cannot iterate or improve reliability  

Friday Observability solves this by offering structured tracing that integrates directly into the Friday Core orchestration loop.

---

## ✨ Features

- **Structured event traces** (input → agent → output)  
- **Langfuse integration**  
- **Execution timing metrics**  
- **Agent-level logs**  
- **Workflow-level logs**  
- **Attachable hooks for custom logging systems**  
- **Minimal overhead & plug-and-play design**  

---

## 🧩 Architecture Overview

Friday Observability hooks into the Friday Core event loop:

```
Event → Agent → Observability → Evaluation → Router → Next Agent
```

### **Core Components**

#### **TraceRecorder**
Captures structured traces of agent execution.

#### **LangfuseClientWrapper**
Sends traces, scores, and metadata to Langfuse.

#### **MetricsCollector**
Captures timing and execution statistics.

#### **WorkflowLogger**
Lightweight console/file logger for debugging.

---

## 📁 Repository Structure

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

## 🚀 Example: Logging Agent Transitions

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

## 🤝 Example: Integrating Langfuse

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

This automatically records:

- Agent start/end  
- Input/output payloads  
- Execution time  
- Errors (with stack traces)  
- Scores (if using friday-evaluation)  

---

## 🔗 Works Seamlessly with Friday Core & Friday Evaluation

Friday Observability works in combination with:

### ✔ **Friday Core**  
Adds tracing around each agent execution.

### ✔ **Friday Evaluation**  
Captures evaluation scores and logs them to Langfuse/trace recorder.

This makes Friday a full **orchestration + evaluation + observability triangle**.

```
        ┌──────────────┐
        │ Observability│
        └──────▲───────┘
               │
 Orchestration │ Evaluation
        ┌──────┴──────┐
        │   Friday    │
        └─────────────┘
```

---

## 🧪 Roadmap

- [ ] Export traces as JSON  
- [ ] Visual workflow timeline UI  
- [ ] Langfuse auto-enrichment with workflow metadata  
- [ ] OpenTelemetry integration  
- [ ] Agent performance metrics dashboard  
- [ ] Error classification & fingerprints  

---

## 🔭 Vision

Friday Observability aims to make multi-agent workflows **transparent**, **explainable**, and **debuggable**, unlocking reliable enterprise AI systems.

---

## 📄 License  
MIT License
