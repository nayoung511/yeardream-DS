import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--left', type=int)
parser.add_argument('-r', '--right', type=int, default=20)
parser.add_argument('--operation', dest='op', default="sum", help="연산자")

args = parser.parse_args()
print(args)


if args.op =='sum':
    out = args.left + args.right
elif args.op == 'sub':
    out = args.left - args.right

print(out)