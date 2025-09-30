FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl git gcc build-essential && \
    pip install --no-cache-dir bandit semgrep gunicorn && \
    curl -sSL https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64.tar.gz \
    | tar -xz -C /usr/local/bin gitleaks

WORKDIR /app
