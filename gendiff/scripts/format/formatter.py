from .stylish import stylish
from .plain import plain
import json


def make_str(diff, format):
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff).rstrip('\n')
    if format == 'json':
        return json.dumps(diff, indent=4, sort_keys=True)
