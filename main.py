import os
import argparse
import importlib
import util
import traceback

parser = argparse.ArgumentParser()
parser.add_argument("task", choices=("run", "init"))
parser.add_argument("day", type=int)
parser.add_argument("part", type=int)
parser.add_argument("-t", "--test", action="store_true")

args = parser.parse_args()

try:
    if args.task == "init":
        code_path = f"code/day_{args.day}.py"
        if os.path.exists(code_path):
            print(f"Python file already exists for day {args.day}. Skipping...")
        else:
            # Create new .py file
            print(f"Generating placeholder file at {code_path}...")
            with open(code_path, "w", encoding="utf-8") as fp:
                fp.write("def part_1(input_text):\n")
                fp.write("    print(input_text)\n\n")
                fp.write("def part_2(input_text):\n")
                fp.write("    print(input_text)\n")

        input_path = f"inputs/day{args.day}.txt"
        if os.path.exists(input_path):
            print(f"Input file already exists for day {args.day}. Skipping...")
        else:
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
    print()
    traceback.print_exc()
