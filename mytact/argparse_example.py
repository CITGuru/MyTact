import argparse
parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument("echo")
args = parser.parse_args()
print args.echo


# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print args.square**2


# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#    print "verbosity turned on"
# ]

# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print "the square of {} equals {}".format(args.square, answer)
# else:
#     print answer