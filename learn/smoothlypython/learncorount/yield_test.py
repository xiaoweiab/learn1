#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 13:58


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    i * 2


def main():
    # 使用for循环
    for i in yield_test(5):
        print(i, ",")
    # yield_test(5)


if __name__ == "__main__":
    main()









