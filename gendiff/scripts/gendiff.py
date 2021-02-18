import argparse
import inspect
from pathlib import Path
import os
import json


def make_diff_str(first_json, second_json):
    temp_dict = first_json.copy()
    temp_dict.update(second_json)
    keys = sorted(list(temp_dict.keys()))
    result = '{\n'
    for key in keys:
        if key in first_json.keys():
            if key in second_json.keys():
                if first_json[key] == second_json[key]:
                    result += f'    {key}: {first_json[key]}\n'
                else:
                    result += f'  - {key}: {first_json[key]}\n'
                    result += f'  + {key}: {second_json[key]}\n'
            else:
                result += f'  - {key}: {first_json[key]}\n'
        else:
            result += f'  + {key}: {second_json[key]}\n'
    end_symb = '}'
    return f'{result}{end_symb}'


def generate_diff(first_path, second_path):
    first_file = Path(first_path)
    if not first_file.exists():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        first_file = Path('{}/{}'.format(os.path.dirname(mod.__file__),
                          first_path))

    second_file = Path(second_path)
    if not second_file.exists():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        second_file = Path('{}/{}'.format(os.path.dirname(mod.__file__),
                           second_path))

    first_json = json.load(open(first_file))
    second_json = json.load(open(second_file))

    print(make_diff_str(first_json, second_json))


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    generate_diff(args.first_file.name, args.second_file.name)


if __name__ == "__main__":
    main()
