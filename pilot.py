from io import IO
from uss import Uss
from request import Request

if __name__ == '__main__':
    req = Request()

    uss = {}
    uss_list = {'left': Uss.LEFT, 'right': Uss.RIGHT}
    for key, val in uss_list.items():
        uss[key] = Uss(val)

    io = {}
    io_list = {'front': IO.FRONT, 'left': IO.LEFT, 'right': IO.RIGHT}
    for key, val in io_list.items():
        io[key] = Uss(val)

    print('press enter to start\n')
    input('>>>  ')

    while True:
        req.set([Request.STR, 50, 100])
        break

    print('End')
