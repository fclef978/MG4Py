#!/usr/bin/python3

from gpio import IO
from uss import Uss
from request import Request
from time import sleep

if __name__ == '__main__':
    req = Request()

    uss = {}
    uss_list = {'left': Uss.LEFT, 'right': Uss.RIGHT}
    for key, val in uss_list.items():
        uss[key] = Uss(val)

    io = {}
    io_list = {'front': IO.FRONT, 'left': IO.LEFT, 'right': IO.RIGHT}
    for key, val in io_list.items():
        io[key] = IO(val, IO.OUT)

    print('press enter to start\n')
    input('>>>  ')

    while True:
        # import pdb; pdb.set_trace()
        req.set(['b', 30, 100])
        sleep(3)
        break

    print('End')
