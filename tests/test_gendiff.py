# import pytest
import json
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from pathlib import Path
from gendiff.scripts.gendiff import get_diff
from gendiff.scripts.formatter import make_str


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent
    return current_dir/'fixtures'/file_name


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_jsons = read(get_fixture_path('plain_json.txt')).split('\n\n')
plain_yamls = read(get_fixture_path('plain_yaml.txt')).split('\n\n')
jsons = read(get_fixture_path('json.txt')).split('\n\n')
yamls = read(get_fixture_path('yaml.txt')).split('\n\n')
results = read(get_fixture_path('results.txt')).split('\n\n')


def test_get_diff():
    assert make_str(get_diff([json.loads(plain_jsons[0]),
                    json.loads(plain_jsons[1])])) == results[0]

    assert make_str(get_diff([json.loads(plain_jsons[1]),
                    json.loads(plain_jsons[2])])) == results[1]

    assert make_str(get_diff([yaml.load(plain_yamls[1], Loader=Loader),
                    yaml.load(plain_yamls[2], Loader=Loader)])) == results[1]

    assert make_str(get_diff([json.loads(jsons[0]),
                    json.loads(jsons[1])])) == results[2]

    assert make_str(get_diff([yaml.load(yamls[0], Loader=Loader),
                    yaml.load(yamls[1], Loader=Loader)])) == results[2]
