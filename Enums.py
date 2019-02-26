from enum import Enum


class Movment(Enum):
    forward = "Going forward"
    stop = "Stopping"
    backward = "Going backward"


class Turning(Enum):
    left = "Turning left"
    right = "Turning right"
    straight = "Going straight"


class Lights(Enum):
    on = "Lights on"
    off = "Lights off"
