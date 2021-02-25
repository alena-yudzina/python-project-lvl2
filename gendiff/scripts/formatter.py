def convert_to_output_format(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def stylish(diff, lvl=0):
    view = '{\n'
    for diff_item in diff:
        if diff_item.get('children') is not None:
            view += (f'{"    " * lvl}{diff_item["diff"]}{diff_item["name"]}: '
                     f'{stylish(diff_item["children"], lvl + 1)}')
        else:
            view += (f'{"    " * lvl}{diff_item["diff"]}{diff_item["name"]}: '
                     f'{convert_to_output_format(diff_item["value"])}\n')
    view += "    " * lvl + '}'
    if lvl > 0:
        view += '\n'
    return view


def make_str(diff, format='default'):
    if format == 'default':
        return stylish(diff)
