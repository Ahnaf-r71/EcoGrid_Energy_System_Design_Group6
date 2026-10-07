from src.shared.event_bus import global_event_bus

class MarketplaceService:
    """Matches excess energy sellers with local neighborhood buyers."""
    
    def __init__(self):
        # Subscribe to Event Bus (Decoupled from IoT Domain)
        global_event_bus.subscribe("EnergyBalanceUpdated", self.handle_energy_update)

    def handle_energy_update(self, event_data: dict):
        meter_id = event_data["meter_id"]
        net_balance = event_data["net_balance_kwh"]
        
        if net_balance > 0:
            print(f"[MARKETPLACE] Seller detected ({meter_id}) with {net_balance:.2f} kWh excess!")
            self.execute_trade(seller_id=meter_id, kwh=net_balance, price_per_kwh=0.15)

    def execute_trade(self, seller_id: str, kwh: float, price_per_kwh: float):
        trade_details = {
            "trade_id": "TRD-1001",
            "seller_id": seller_id,
            "buyer_id": "METER-NEIGHBOR-02",
            "amount_kwh": kwh,
            "total_price": round(kwh * price_per_kwh, 2)
        }
        print(f"[MARKETPLACE] Trade Matched! {trade_details}")
        global_event_bus.publish("TradeExecuted", trade_details)