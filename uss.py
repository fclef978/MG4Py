import smbus2
from time import sleep


class Uss:

    LEFT = 0x70
    RIGHT = 0x71

    INTERVAL = 0.05
    MIN_DIST = 16
    MAX_DIST = 600
    CENTER_DIST = 10

    def __init__(self, addr):
        self.addr = addr
        self.i2c = smbus2.SMBus(1)
        # ソフトウェアリビジョンの確認
        if not self.i2c.read_byte_data(self.addr, 0) == 0x06:
            print("failed to open USS in %{0}".format(self.addr))
        else:
            print("USS opened in %{0}".format(self.addr))

    def get(self):
        self.i2c.write_byte_data(self.addr, 0x00, 0x51)
        sleep(Uss.INTERVAL)

        data = self.i2c.read_i2c_block_data(self.addr, 0x02, 2)
        if data < Uss.MIN_DIST or data > Uss.MAX_DIST:
            return False
        else:
            return data + Uss.CENTER_DIST
