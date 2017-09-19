# Arduino通信クラス
# TL 鈴木宏和
# 2017-08-26
# 2017-08-26

import serial
from time import sleep


class ArduinoOpenError(Exception):
    
    def __str__(self):
        return ('Arduino Open Failed')

class Arduino:
    """
	Arduinoとの通信をやってくれるクラスです。
	シリアル通信のクラスであるserial(モジュールはpySerial)はbyte型や
	byteArray型でしかやり取りできないので、このクラス内のread()やwrite()で
	エンコード・デコードしてます。
	"""

    def __init__(self):
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200)
            self.port = '/dev/ttyACM0'
        except:
            self.ser = serial.Serial('/dev/ttyACM1', 115200)
            self.port = '/dev/ttyACM1'
        finally:
            pass
        self.flush()
        print("Arduino Opened {0}".format(self.port))

    def __del__(self):
        # cmd = [99, 0, 0]
        # self.send(cmd)
        self.ser.close()

    def flush(self):
        self.ser.reset_input_buffer()

    def send(self, cmd_data):
        print("Send {0}".format(cmd_data))
        ser_data = self.encode(cmd_data)
        for i in range(12):
            self.write(ser_data[i])

    def receive(self):
        cnt = 0
        ser_data = []
        # 50ループ(だいたい50ミリ秒)でタイムアウト
        for i in range(50):
            if self.ser.in_waiting >= 12:
                ser_data.append(self.read())
                if ser_data[0] == ':':
                    for i in range(1, 12):
                        ser_data.append(self.read())
                    ser_data = ''.join(ser_data)
                    cmd_data = self.decode(ser_data)
                    print("Receive {0}".format(cmd_data))
                    return cmd_data
            sleep(0.001)

        return False

    def write(self, byte_data):
        tmp = byte_data.encode('ASCII')
        print(tmp)
        self.ser.write(tmp)
        return
        
    def read(self):
        tmp = self.ser.read().decode('utf-8')
        return tmp 

    @staticmethod
    def encode(cmd):
        return ':{cmd[0]}{cmd[1]:05d}{cmd[2]:05d}'.format(cmd = cmd)

    @staticmethod
    def decode(ser):
        a = ser[1]
        b = ser[2:7]
        c = ser[7:12]
        return [a, int(b), int(c)]
