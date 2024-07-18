# Project Name: Instrumenting Django with OpenTelemetry (OTel)

## Overview
This project demonstrates how to instrument a django application that uses celery to perform asynchronous tasks

The application logs are collected by the prometheus application and spans and traces are collected by jaeger application.

## Prerequisites

- Python (3.10+)
- Django framework
- Docker (optional, for local development)

## Setup Instructions

### Run application suite using docker compose

You can run the application using docker compose

```bash
docker compose up --build
```

  