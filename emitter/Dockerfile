FROM python:3.10-slim
WORKDIR /app
COPY emit_metrics.py .
RUN pip install prometheus_client
CMD ["python", "emit_metrics.py"]
