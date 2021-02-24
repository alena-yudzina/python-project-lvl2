import argparse
import inspect
from .parser import get_diff
from pathlib import Path
import json
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
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
    return (args.first_file.name, args.second_file.name)


def generate_diff(*paths):
    paths = [*paths]
    for i, path in enumerate(paths):
        paths[i] = Path(path)
        if not paths[i].exists():
            frm = inspect.stack()[1]
            mod = inspect.getmodule(frm[0])
            paths[i] = Path(mod.__file__).parent / paths[i].name

    python_dicts = read_files(paths)
    return get_diff(python_dicts)


def main():
    args = parse_cli_args()
    diff = generate_diff(*args)
    print(diff)


if __name__ == "__main__":
    main()
