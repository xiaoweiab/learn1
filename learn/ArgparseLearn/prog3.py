#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 16:26
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int, help='the base')
    parser.add_argument('y', type=int, help='the exponent')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    answer = args.x ** args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print("{}^{} == {}".format(args.x, args.y, answer))


if __name__ == "__main__":
    main()









