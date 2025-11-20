from __future__ import annotations

# fmt: off

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Self
    from collections.abc import Callable

class EventSubscriber[T, **P]:
    """Summary

    Attributes:
        valid (bool): Whether or not the subscriber is still valid.
        callback (Callable[P, T]): The callback of the subscriber.
        onInvalidate (Callable[[Self], None] | None): Called when the subscriber is invalidated by the subscriber.
        onRelease (Callable[[Self], None] | None): Called when the subscriber is released by the Event Handler.
    """
    def __init__(self, a_callback: Callable[P, T], /, a_onInvalidate: Callable[[Self], None]|None = None, a_onRelease: Callable[[Self], None]|None = None) -> None:
        """Creates a new Event Subscriber.

        Args:
            a_callback (Callable[P, T]): The callback of the subscriber.
            a_onInvalidate (Callable[[Self], None] | None): Called when the subscriber is invalidated by the subscriber.
            a_onRelease (Callable[[Self], None] | None): Called when the subscriber is released by the Event Handler.
        """
        self.valid: bool = True
        """Whether or not the subscriber is still valid."""
        self.callback: Callable[P, T] = a_callback
        """The callback of the subscriber."""
        self.onInvalidate: Callable[[Self], None]|None = a_onInvalidate
        """Called when the subscriber is invalidated by the subscriber."""
        self.onRelease: Callable[[Self], None]|None = a_onRelease
        """Called when the subscriber is released by the Event Handler."""
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.valid == other.valid and self.callback == other.callback and self.onInvalidate == other.onInvalidate and self.onRelease == other.onRelease

    def Invalidate(self) -> None:
        """Use to invalidate the subscriber without being the Event Handler.
        """
        self.valid = False
        if self.onInvalidate is not None:
            self.onInvalidate(self)
    
    def Release(self) -> None:
        """Used by the Event Handler to release the subscriber.
        """
        self.valid = False
        if self.onRelease is not None:
            self.onRelease(self)