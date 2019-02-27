#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 15:32

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",type=int)
args = parser.parse_args()
print(args.square ** 2)









