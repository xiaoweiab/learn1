#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 16:10

import argparse

def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int, help='the base ')
    parser.add_argument('y', type=int, help='the exponent')
    parser.add_argument('-v', '--verbosity', action='count', default=0)
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print("{}^{} == ".format(args.x, args.y), end="")
    print(answer)









