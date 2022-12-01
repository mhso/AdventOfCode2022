import argparse
import importlib
import util

parser = argparse.ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("part", type=int)
parser.add_argument("-t", "--test", action="store_true")

args = parser.parse_args()

try:
    module = importlib.import_module(f"code.day{args.day}")
    input_text = util.read_input(args.day, args.test)
    getattr(module, f"part_{args.part}")(input_text)

except ModuleNotFoundError:
    print(f"Error: Can't find code for day {args.day}. Exiting...")

except Exception as exc:
    print(f"Error: {' - '.join(exc.args)}. Exiting...")
