from arduino import Arduino


class Request:

    STP = 1
    STR = 2
    ROT = 3
    GET_MODE = 10
    GET_DIST = 11
    GET_BATT = 12

    def __init__(self):
        self.arduino = Arduino()

    def set(self, cmd_data):
        self.arduino.send(cmd_data)

    def get(self, mode):
        cmd_data = [mode, 0, 0]
        self.set(cmd_data)
        return self.arduino.receive()

    def get_dist(self):
        cmd_data = self.get(Request.GET_DIST)
        if cmd_data is False:
            return False
        return cmd_data[0], cmd_data[1]  # Left, Rightの順番

    def get_batt(self):
        cmd_data = self.get(Request.GET_BATT)
        if cmd_data is False:
            return False
        return cmd_data[0] / 100.0
