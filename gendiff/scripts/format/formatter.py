def dict_view(dct, lvl):
    keys = sorted(list(dct.keys()))
    res_str = '{\n'

    for key in keys:
        res_str += '{}{}: '.format((lvl + 1) * 4 * ' ', key)
        if isinstance(dct[key], dict):
            res_str += dict_view(dct[key], lvl + 1) + '\n'
        else:
            res_str += f'{dct[key]}\n'

    return res_str + lvl * 4 * ' ' + '}'


def add_string(status, key, value, lvl):
    if isinstance(value, dict):
        value = dict_view(value, lvl + 1)

    str_ = '{status}{key}: {value}\n'.format(
        status=lvl * '    ' + status,
        key=key,
        value=value,
    )

    return str_


def stylish(diff, lvl=0):
    keys = sorted(list(diff.keys()))
    view = '{\n'
    ind = '    '

    for key in keys:
        if diff[key][0] == 'nested':
            up_lvl = lvl + 1
            view += up_lvl * ind + f'{key}: ' + stylish(diff[key][1], up_lvl)
        elif diff[key][0] == 'added':
            view += add_string('  + ', key, diff[key][1], lvl)
        elif diff[key][0] == 'deleted':
            view += add_string('  - ', key, diff[key][1], lvl)
        elif diff[key][0] == 'same':
            view += add_string('    ', key, diff[key][1], lvl)
        elif diff[key][0] == 'modified':
            view += add_string('  - ', key, diff[key][1], lvl)
            view += add_string('  + ', key, diff[key][2], lvl)
    view += lvl * ind + '}'

    if lvl > 0:
        view += '\n'
    return view


def make_str(diff, format='stylish'):
    if format == 'stylish':
        return stylish(diff)
