import time
from src.shared.event_bus import global_event_bus

class SmartMeterService:
    """Ingests high-frequency IoT meter data and broadcasts energy updates."""
    
    def ingest_reading(self, meter_id: str, generation_kwh: float, consumption_kwh: float):
        net_balance = generation_kwh - consumption_kwh
        reading = {
            "meter_id": meter_id,
            "net_balance_kwh": net_balance,
            "timestamp": time.time()
        }
        print(f"[IoT INGESTION] Ingested reading from Meter '{meter_id}': Net Balance = {net_balance:.2f} kWh")
        
        # Publish event asynchronously across boundary
        global_event_bus.publish("EnergyBalanceUpdated", reading)
        return reading