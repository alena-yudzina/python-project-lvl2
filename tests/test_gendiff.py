# import pytest
import json
from pathlib import Path
from gendiff.scripts.gendiff import make_diff


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent
    return current_dir/'fixtures'/file_name


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_jsons = read(get_fixture_path('plain_json.txt')).rstrip().split('\n\n')
results = read(get_fixture_path('results.txt')).rstrip().split('\n\n')


def test_make_diff():
    assert make_diff(json.loads(plain_jsons[0]),
                     json.loads(plain_jsons[1])) == results[0]
    assert make_diff(json.loads(plain_jsons[1]),
                     json.loads(plain_jsons[2])) == results[1]
