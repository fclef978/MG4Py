# Arduino通信クラス
# TL 鈴木宏和
# 2017-08-26
# 2017-08-26

import serial
import time


class Aruduino:

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.flush()

    def __del__(self):
        self.ser.close()

    def flush(self):
        self.ser.reset_input_buffer()

    def send(self, cmd_data):
        ser_data = self.encode(cmd_data)
        for i in range(7):
            self.ser.write(ser_data[i])

    def receive(self):
        ser_data = [0] * 7
        if self.ser.in_waiting > 7:
            for i in range(7):
                ser_data[i] = self.ser.read()

        cmd_data = self.decode(ser_data)
        return cmd_data

    def encode(self, cmd_data):
        mid_data = [0] * 6
        ser_data = [0] * 7
        for i in range(3):
            mid_data[2 * i] = (cmd_data[i] >> 8) & 0xff
            mid_data[2 * i + 1] = cmd_data[i] & 0xff

        for i in range(7):
            upper_bit = 0x40
            lower_bit = 0x7f
            data1 = 0xff
            data2 = 0x00
            for j in range(i):
                if not j == 0:
                    upper_bit >>= 1
                    upper_bit |= 0x80
                lower_bit >>= 1
                lower_bit &= 0x7f
            if i == 0:
                upper_bit = 0x08
            else:
                data1 = mid_data[i - 1] << (7 - i)
            if not i == 6:
                data2 = mid_data[i] >> (i + 1)
            ser_data[i] = (data1 & upper_bit) | (data2 & lower_bit)

        return ser_data

    def decode(self, ser_data):
        mid_data = [0] * 6
        cmd_data = [0] * 3

        for i in range(6):
            upper_bit = 0xfe
            lower_bit = 0x01
            data1 = ser_data[i] << (i + 1)
            data2 = ser_data[i + 1] >> (6 - i)
            for j in range(i):
                upper_bit <<= 1
                upper_bit &= 0xf7
                lower_bit <<= 1
                lower_bit |= 0x01
            mid_data[i] = (data1 & upper_bit) | (data2 & lower_bit)

        for i in range(3):
            cmd_data[i] = (mid_data[2 * i] << 8) | mid_data[2 * i + 1]

        return cmd_data
