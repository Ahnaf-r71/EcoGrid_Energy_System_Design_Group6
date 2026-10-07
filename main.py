from src.ingestion.meter_service import SmartMeterService
from src.marketplace.matching_engine import MarketplaceService
from src.settlement.ledger_service import FinancialSettlementService

def main():
    print("==================================================")
    print("      EcoGrid Energy - System Design Simulation   ")
    print("==================================================")

    # Initialize Services
    ingestion_service = SmartMeterService()
    marketplace_service = MarketplaceService()
    settlement_service = FinancialSettlementService()

    # Simulate Smart Meter Readings (High-frequency IoT Stream)
    print("\n--- Simulating IoT Data Ingestion ---")
    ingestion_service.ingest_reading(meter_id="METER-HOUSE-A", generation_kwh=12.5, consumption_kwh=4.0)
    ingestion_service.ingest_reading(meter_id="METER-HOUSE-B", generation_kwh=2.0, consumption_kwh=8.0)

if __name__ == "__main__":
    main()