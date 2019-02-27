#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-25 15:25
import contextlib
import sys

@contextlib.contextmanager
def looking_glass():

    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
    print('exit')

def main():
    with looking_glass() as what:
        print("samma")
        print(what)
    print('ok')


if __name__ == "__main__":
    main()









