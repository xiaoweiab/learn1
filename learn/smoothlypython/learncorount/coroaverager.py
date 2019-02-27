#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-25 16:39


def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        total += term
        count += 1
        average = total / count
        print(average)

def main():
    avg_coro = averager()
    next(avg_coro)
    avg_coro.send(10)
    avg_coro.send(12)
    avg_coro.send(14)
    avg_coro.send(10)
    avg_coro.send(10)
    avg_coro.send(10)
    avg_coro.send(12)
    avg_coro.send(14)
    avg_coro.send(12)
    avg_coro.send(14)
    avg_coro.send(12)
    avg_coro.send(14)


if __name__ == "__main__":
    main()









