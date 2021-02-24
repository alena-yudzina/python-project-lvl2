import argparse
import inspect
from pathlib import Path
import json


def convert_to_json_format(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def parse_cli_args():
    ''' parse arguments from cli

    '''
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    return (args.first_file.name, args.second_file.name)


def get_diff(json_dicts):
    first_json = {k: convert_to_json_format(v) for k,
                  v in json_dicts[0].items()}
    second_json = {k: convert_to_json_format(v) for k,
                   v in json_dicts[1].items()}
    merge_dict = {**first_json, **second_json}
    keys = sorted(list(merge_dict.keys()))
    result = '{\n'
    for key in keys:
        is_in_first = key in first_json.keys()
        is_in_second = key in second_json.keys()
        if is_in_first and is_in_second:
            if first_json[key] == second_json[key]:
                result += f'    {key}: {first_json[key]}\n'
            else:
                result += f'  - {key}: {first_json[key]}\n'
                result += f'  + {key}: {second_json[key]}\n'
        elif is_in_first:
            result += f'  - {key}: {first_json[key]}\n'
        else:
            result += f'  + {key}: {second_json[key]}\n'
    result += '}'
    return result


def generate_diff(*paths):
    paths = [*paths]
    for i, path in enumerate(paths):
        paths[i] = Path(path)
        if not paths[i].exists():
            frm = inspect.stack()[1]
            mod = inspect.getmodule(frm[0])
            paths[i] = Path(mod.__file__).parent / paths[i].name

    json_dicts = list(map(lambda path: json.load(open(path)), paths))
    diff = get_diff(json_dicts)
    print(diff)


def main():
    args = parse_cli_args()
    generate_diff(*args)


if __name__ == "__main__":
    main()
