from prometheus_client import start_http_server, Counter, Gauge
import random
import time

REQUEST_COUNT = Counter("friday_agent_requests", "Number of agent requests", ["agent"])
LATENCY = Gauge("friday_agent_latency", "Agent response latency", ["agent"])

AGENTS = ["SearchAgent", "MathAgent", "RAGAgent"]

if __name__ == "__main__":
    start_http_server(8000)
    print("Emitter started on port 8000")

    while True:
        agent = random.choice(AGENTS)
        REQUEST_COUNT.labels(agent=agent).inc()
        LATENCY.labels(agent=agent).set(random.uniform(0.1, 1.0))
        time.sleep(1)
