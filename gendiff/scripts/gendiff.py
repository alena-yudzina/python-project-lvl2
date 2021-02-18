import argparse
import inspect
from pathlib import Path
import os

def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def generate_diff(first_path, second_path):
    first_file = Path(first_path)
    if not first_file.exists():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        first_file = Path('{}/{}'.format(os.path.dirname(mod.__file__), first_path))

    second_file = Path(second_path)
    if not second_file.exists():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        second_file = Path('{}/{}'.format(os.path.dirname(mod.__file__), second_path))
    


if __name__ == "__main__":
    main()
