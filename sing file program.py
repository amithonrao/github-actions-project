import argparse
from pathlib import Path
from shutil import copytree

parser = argparse.ArgumentParser(description="Create a project from a template.")
parser.add_argument("--name", required=True, help="Name of the new project folder")
args = parser.parse_args()

template = Path("template")
destination = Path(args.name)

if not template.is_dir():
    parser.error("Could not find the 'template' folder in the current directory.")

try:
    copytree(template, destination)
except FileExistsError:
    parser.error(f"Destination already exists: {destination}")
except OSError as exc:
    parser.exit(1, f"Could not copy the template: {exc}\n")

print(f"Created a new project: {destination}")