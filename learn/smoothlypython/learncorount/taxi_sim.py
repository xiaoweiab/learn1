#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 13:36
import collections

Event = collections.namedtuple('Event', 'time poc action')


def taxi_process(ident, trip, start_time=0):
    """每次改变状态，把控制台让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trip):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')


def main():
    time = 7
    taxi = taxi_process(ident=13, trip=2, start_time=0)
    print(next(taxi))
    print(taxi.send(time))
    print(taxi.send(time))
    print(taxi.send(time+1))
    print(taxi.send(time+1))
    print(taxi.send(time+1))


if __name__ == "__main__":
    main()









