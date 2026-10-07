# Bounded Context Isolation Fitness Function

This test module implements an architectural **fitness function** using `pytest`. It enforces domain boundaries by ensuring that the **Marketplace** module does not directly import or depend on the **IoT Ingestion** module.

---

## Overview

In modular architectures and Domain-Driven Design (DDD), bounded contexts must remain isolated to prevent tight coupling.

This test checks `src/marketplace/matching_engine.py` to confirm that it has no direct imports from `src.ingestion`. If a direct dependency is detected, the test fails with an architectural violation error.

---

## Enforced Rules

| Pattern | Status | Description |
| --- | --- | --- |
| `from src.ingestion ...` | ❌ **Forbidden** | Direct import from Ingestion context |
| `import src.ingestion` | ❌ **Forbidden** | Direct package reference to Ingestion |

---

## Prerequisites

Ensure `pytest` is installed:

```bash
pip install pytest

```

---

## How to Run

Execute the test using `pytest`:

```bash
pytest test_bounded_context_isolation.py

```

---

## Resolving Test Failures

If this test fails, refactor the code to eliminate the direct import:

1. **Event-Driven Decoupling:** Publish domain events (e.g., via an event bus or broker) from IoT Ingestion and subscribe to them in Marketplace.
2. **Shared Abstractions / Anti-Corruption Layer:** Intersect communication using shared interfaces or data transfer objects (DTOs) outside of the restricted modules.
