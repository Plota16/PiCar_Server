from Enums import *


class Car:
    def __init__(self):
        self.movement = Movment.stop
        self.turning = Turning.straight
        self.lights = Lights.off

    def turn_right(self):
        self.turning = Turning.right

    def turn_left(self):
        self.turning = Turning.left

    def go_straight(self):
        self.turning = Turning.straight

    def go_forward(self):
        self.movement = Movment.forward

    def go_backward(self):
        self.movement = Movment.backward

    def stop(self):
        self.movement = Movment.stop

    def lights_on(self):
        self.lights = Lights.on

    def lights_off(self):
        self.lights = Lights.off

