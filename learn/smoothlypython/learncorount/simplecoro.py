#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-25 16:24

from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> start: a= ', a)
    b = yield
    print('-> Received: b =', b)
    c = yield
    print(c)
    print('-> Received: c =', c)


def main():
    my_coro2 = simple_coro2(13)
    print(getgeneratorstate(my_coro2))
    next(my_coro2)
    print(getgeneratorstate(my_coro2))
    my_coro2.send(23)
    print(getgeneratorstate(my_coro2))
    my_coro2.send(33)
    print(getgeneratorstate(my_coro2))


if __name__ == "__main__":
    main()









