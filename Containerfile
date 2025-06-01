FROM python:3.10-slim AS builder
WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir --target=/python-deps \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /python-deps /usr/local/lib/python3.10/site-packages
COPY ./app ./app

ENV TORCH_HOME=/app/.torch
RUN mkdir -p /app/.torch

USER root
RUN chgrp -R 0 /app/.torch && \
    chmod -R g=u /app/.torch
USER 1001

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]