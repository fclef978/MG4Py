from arduino import Arduino


class Request:

    STP = 'a'
    STR = 'b'
    ROT = 'c'
    GET_MODE = 'e'
    GET_DIST = 'f'
    GET_BATT = 'g'

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
        return cmd_data[1], cmd_data[2]  # Left, Rightの順番

    def get_batt(self):
        cmd_data = self.get(Request.GET_BATT)
        if cmd_data is False:
            return False
        return cmd_data[1] / 100.0
