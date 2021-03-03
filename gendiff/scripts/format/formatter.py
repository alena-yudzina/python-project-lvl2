from .stylish import stylish
from .plain import plain


def make_str(diff, format='stylish'):
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff).rstrip('\n')
