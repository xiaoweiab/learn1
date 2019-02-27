

# -------------列表推导---------------------

list = [i for i in range(10) if i % 2 == 0]
print(list)


seq = ['one', 'two', 'three']


def _treatment(pos, element):
    return '%d: %s' % (pos, element)


list2 = [_treatment(i, el) for i, el in enumerate(seq)]
print(list2)

# ------------生成器-------------------------


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fi = fibonacci()
list3 = [fi.__next__() for i in range(10)]
print(list3)

# -------------协同程序-----------------------


def corontime_1():
    for i in range(3):
        print("'C1")
        yield i


def corontime_2():
    for i in range(3):
        print("'C2")
        yield i
# ---------------生成器表达式-------------------


iter_1 = (x**2 for x in range(10) if x % 2 == 0)
for e1 in iter_1:
    print(e1)
