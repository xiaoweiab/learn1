#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-25 15:06
import sys

class LookingGlass:

    def __enter__(self):
        print('enter')
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self,text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        print('eixt')
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

def main():
    with LookingGlass() as what:
        print("samma")
        print(what)


if __name__ == "__main__":
    main()









