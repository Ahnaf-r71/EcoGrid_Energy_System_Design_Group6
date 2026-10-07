from typing import Callable, Dict, List, Any

class EventBus:
    """Simple In-Memory Event Bus for Asynchronous Domain Event Messaging."""
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, data: Any):
        print(f"\n[EVENT BUS] Published '{event_type}': {data}")
        if event_type in self._subscribers:
            for handler in self._subscribers[event_type]:
                handler(data)

# Global singleton event bus instance
global_event_bus = EventBus()