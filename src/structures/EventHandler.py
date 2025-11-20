from __future__ import annotations

# fmt: off

from .EventSubscriber import EventSubscriber
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable

class EventHandler[T, **P]:
    def __init__(self) -> None:
        self.subscribers: list[EventSubscriber[T, P]] = []
    
    def Subscribe(self, a_subscriber: Callable[P, T]) -> EventSubscriber[T, P]:
        subscriber: EventSubscriber[T, P] = EventSubscriber[T, P](a_subscriber, a_onInvalidate=lambda a_eventSubscriber: self.Remove(a_eventSubscriber))
        self.subscribers.append(subscriber)
        return subscriber

    def Unsubscribe(self, a_subscriber: EventSubscriber[T, P]) -> None:
        """Unsubscribe a subscriber from the Event Handler.
        
        Args:
            a_subscriber (EventSubscriber[T, P]): The subscriber to unsubscribe.
        
        Raises:
            ValueError: The subscriber passed in was not subscribed to the handler.
        """
        try:
            self.subscribers.pop(self.subscribers.index(a_subscriber)).Release()
        except ValueError as e:
            e.add_note(f"The event subscriber {a_subscriber} was not subscribed to the event handler {self}.")
            raise e

    def Remove(self, a_subscriber: EventSubscriber[T, P]) -> None:
        """Remove a subscriber from the Event Handler without releasing.
        
        Args:
            a_subscriber (EventSubscriber[T, P]): The subscriber to unsubscribe.
        
        Raises:
            ValueError: The subscriber passed in was not subscribed to the handler.
        """
        try:
            self.subscribers.pop(self.subscribers.index(a_subscriber))
        except ValueError as e:
            e.add_note(f"The event subscriber {a_subscriber} was not subscribed to the event handler {self}.")
            raise e

    def Call(self, *args: P.args, **kwargs: P.kwargs) -> None:
        [subscriber.callback(*args, **kwargs) for subscriber in self.subscribers]