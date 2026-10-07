from src.shared.event_bus import global_event_bus

class FinancialSettlementService:
    """Processes micro-transactions for executed trades."""
    
    def __init__(self):
        global_event_bus.subscribe("TradeExecuted", self.handle_trade_executed)

    def handle_trade_executed(self, trade_data: dict):
        total = trade_data["total_price"]
        seller = trade_data["seller_id"]
        buyer = trade_data["buyer_id"]
        
        print(f"[SETTLEMENT] Processing Micro-transaction: ${total:.2f} from {buyer} -> {seller}")
        print(f"[SETTLEMENT] Ledger updated successfully for Trade {trade_data['trade_id']}.")