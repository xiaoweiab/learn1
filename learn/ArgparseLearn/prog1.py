#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-26 15:32

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", action='store_true')
parser.add_argument("--ve", help="increase output verbosity", action='store_true')
args = parser.parse_args()
print(args)
if args.verbose:
    print("verbosity turned on ")









