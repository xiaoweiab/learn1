#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-01 15:28
import abc

def main():
    mydict = {}
    print(isinstance(mydict, abc.ABCMeta))


def is_hash():
    tt = (1, 2, (30, 40))
    print(hash(tt))



if __name__ == "__main__":
    # main()
    is_hash()








