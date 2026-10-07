import os
import pytest

def test_bounded_context_isolation():
    """Fitness Function: Ensures Marketplace code does not import IoT Ingestion directly."""
    marketplace_file = os.path.join("src", "marketplace", "matching_engine.py")
    
    with open(marketplace_file, "r") as f:
        content = f.read()
        
    assert "from src.ingestion" not in content, "VIOLATION: Marketplace cannot directly import IoT Ingestion!"
    assert "import src.ingestion" not in content, "VIOLATION: Marketplace cannot directly import IoT Ingestion!"