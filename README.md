# EcoGrid Energy

This project demonstrates an event-driven energy trading architecture
## Structure

- `src/shared` contains the shared event bus and message schema components.
- `src/ingestion` handles meter ingestion.
- `src/marketplace` handles trading and matching.
- `src/settlement` handles financial settlement.

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main entry point:
   ```bash
   python main.py
   ```
4. Run the architecture checks:
   ```bash
   pytest -q tests/test_architecture.py
   ```
