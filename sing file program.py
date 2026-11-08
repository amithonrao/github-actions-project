from distutils.dir_util import copy_tree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str)
args = parser.parse_args()

if args.name is None:
    raise "Need a name argument"

copy_tree("template", f"{args.name}")
print(f"Created a new project: {args.name}")