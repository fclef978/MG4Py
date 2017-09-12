from RPi import GPIO
import time


class IO:
    FRONT = 18
    LEFT = 25
    RIGHT = 26

    IN = GPIO.IN
    OUT = GPIO.OUT

    def __init__(self, port, io):
        self.port = port
        self.io = io
        GPIO.setmode(GPIO.BCM)
        if self.io == IO.IN:
            GPIO.setup(self.port, self.io, pull_up_down=GPIO.PUD_UP)
        elif self.io == IO.OUT:
            GPIO.setup(self.port, self.io)

    def __del__(self):
        GPIO.cleanup(self.port)

    def read(self):
        return GPIO.input(self.port)

    def write(self, state):
        if self.io == IO.OUT:
            GPIO.output(self.port, state)
            return True
        else:
            print("Port {0} is not OUTPUT".format(self.port))
            return False

    def toggle_write(self):
        self.write(not self.read())
