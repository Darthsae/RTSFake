from dataclasses import dataclass

@dataclass
class UIInputHolder:
    leftMouseDown:   bool = True
    leftMouseHeld:   bool = True
    leftMouseUp:     bool = True
    middleMouseDown: bool = True
    middleMouseHeld: bool = True
    middleMouseUp:   bool = True
    rightMouseDown:  bool = True
    rightMouseHeld:  bool = True
    rightMouseUp:    bool = True
    mouseEnter:      bool = True
    mouseHover:      bool = True
    mouseExit:       bool = True