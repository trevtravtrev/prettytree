import argparse
import os.path
import prettytree


# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("root", type=str, help="full path to your root project directory")
parser.add_argument("-t", "--text", action='store_true', help="output text")
parser.add_argument("-i", "--image", action='store_true', help="output image")
parser.add_argument("-b", "--blacklist", nargs='*', help='ignore these words, separated by "|"')

# Read arguments from the command line
args = parser.parse_args()

if args.root:
    if os.path.isdir(args.root):
        pass
    else:
        parser.print_help()
        print("Invalid directory. Please input the full path to your root project directory.")
if not args.text and not args.image:
    prettytree.main(args.root, "both")
if args.text:
    prettytree.main(args.root, "text", args.blacklist)
if args.image:
    prettytree.main(args.root, "image")
