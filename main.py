import os
import argparse
import importlib
import util

parser = argparse.ArgumentParser()
parser.add_argument("task", choices=("run", "init"))
parser.add_argument("day", type=int)
parser.add_argument("part", type=int)
parser.add_argument("-t", "--test", action="store_true")

args = parser.parse_args()

try:
    if args.task == "init":
        path = f"code/day_{args.day}.py"
        if os.path.exists(path):
            print(f"Error: Python file already exists for day {args.day}. Exiting...")
            exit(0)

        # Create new .py file
        print(f"Generating placeholder file at {path}...")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write("def part_1(input_text):\n")
            fp.write("    print(input_text)\n\n")
            fp.write("def part_2(input_text):\n")
            fp.write("    print(input_text)\n")

        # Download input text from adventofcode
        print("Downloading input text from adventofcode.com...")
        util.download_input(args.day)

    else:
        module = importlib.import_module(f"code.day_{args.day}")
        input_text = util.read_input(args.day, args.test)
        getattr(module, f"part_{args.part}")(input_text)

except ModuleNotFoundError:
    print(f"Error: Can't find code for day {args.day}. Exiting...")

except Exception as exc:
    print(f"Error: {' - '.join(exc.args)}. Exiting...")
