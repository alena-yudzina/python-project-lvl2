def stylish(diff, lvl=0):
    view = '{\n'
    for diff_item in diff:
        diff = diff_item['diff']
        if diff == 'add':
            diff = '  + '
        elif diff == 'del':
            diff = '  - '
        else:
            diff = '    '
        children = diff_item.get('children')
        if children:
            children = stylish(diff_item["children"], lvl + 1)
        else:
            children = str(diff_item["value"]) + '\n'
        str_ = '{lvl}{diff}{name}: {children}'.format(
            lvl="    " * lvl,
            diff=diff,
            name=diff_item["name"],
            children=children,
        )
        view += str_
    view += "    " * lvl + '}'
    if lvl > 0:
        view += '\n'
    return view


def make_str(diff, format):
    if format == 'stylish':
        return stylish(diff)
