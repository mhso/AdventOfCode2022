import argparse
import importlib
import util

parser = argparse.ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("part", type=int)

args = parser.parse_args()

try:
    module = importlib.import_module(f"code.day{args.day}")
    input_text = util.read_input(args.day)
    getattr(module, f"part{args.part}")(input_text)

except Exception as e:
    print(e.args)
    print("Error: Invalid day. Exiting...")
