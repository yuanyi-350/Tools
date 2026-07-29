import argparse
from main_clean import main_clean
from style import style
from left import left

start, end = None, None

def main():
    global start, end
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--left', nargs='+', type=int, help = "remove `\\left` and `\\right` between `start` and `end`")
    parser.add_argument('--style', nargs='+', type=int, help =
        "remove `\\boldsymbol`, `\\mathrm`, `\\mathbf` between `start` and `end`")
    args = parser.parse_args()
    if args.left:
        if len(args.left) == 1:
            start, end = args.left[0], args.left[0]
        else:
            start, end = args.left
        return "left"
    elif args.style:
        if len(args.style) == 1:
            start, end = args.style[0], args.style[0]
        else:
            start, end = args.style
        return "style"
    else:
        return "main_clean"

command = main()
filename = input()
if filename[0] == '"':
    filename = filename[1:-1]

if command == "main_clean":
    main_clean(filename)
elif command == "style":
    style(filename, start, end)
else:
    left(filename, start, end)