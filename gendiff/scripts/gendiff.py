import argparse
import inspect
import json
import yaml

from .parser import get_diff
from .format.formatter import make_str
from pathlib import Path
from yaml import Loader


def read_files(paths):
    if paths[0].suffix == '.json':
        python_dicts = list(map(lambda path: json.load(open(path)), paths))
    else:
        python_dicts = list(map(lambda path: yaml.load(open(path),
                                Loader=Loader), paths))
    return python_dicts


def parse_cli_args():
    ''' parse arguments from cli

    '''
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    if not args.format:
        args.format = 'stylish'
    return (args.first_file.name, args.second_file.name, args.format)


def generate_diff(*args):
    first_file, second_file, format = args
    paths = [first_file, second_file]
    for i, path in enumerate(paths):

        paths[i] = Path(path)
        if not paths[i].exists():
            frm = inspect.stack()[1]
            mod = inspect.getmodule(frm[0])
            paths[i] = Path(mod.__file__).parent / paths[i].name

    try:
        python_dicts = read_files(paths)
    except FileNotFoundError:
        return print('Wrong file path')
    return make_str(get_diff(python_dicts), format)


def main():
    args = parse_cli_args()
    diff = generate_diff(*args)
    print(diff)


if __name__ == "__main__":
    main()
