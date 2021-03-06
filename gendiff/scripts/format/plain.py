def output_view(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def value_view(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value in (True, False, None):
        return output_view(value)
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def add_string(full_path, value1, status, value2=None):
    value1 = value_view(value1)
    value2 = value_view(value2)
    if status == 'added':
        return f"Property '{full_path}' was added with value: {value1}\n"
    if status == 'deleted':
        return f"Property '{full_path}' was removed\n"
    if status == 'modified':
        return (f"Property '{full_path}' was updated. "
                f"From {value1} to {value2}\n")
    return ''


def plain(diff, full_path=''):
    keys = sorted(list(diff.keys()))
    view = ''
    for key in keys:
        if diff[key][0] == 'nested':
            view += plain(diff[key][1], full_path + key + '.')
        elif diff[key][0] == 'modified':
            view += add_string(f'{full_path}{key}', diff[key][1],
                               'modified', diff[key][2])
        else:
            view += add_string(f'{full_path}{key}', diff[key][1], diff[key][0])
    return view
