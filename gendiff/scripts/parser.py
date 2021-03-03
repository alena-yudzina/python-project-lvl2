def change_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def convert_to_output_format(dicts):
    res = []
    for dct in dicts:
        dct = {k: change_value(v) for k, v in dct.items()}
        res.append(dct)
    return res


def create_node(diff, name, value, children=None):
    node = {
        'diff': diff,
        'name': name,
        'value': value,
    }
    if children:
        node['children'] = children
    return node


def get_diff(dicts):
    dicts = convert_to_output_format(dicts)
    keys = set({**dicts[0], **dicts[1]}.keys())
    diff = {}
    for key in keys:
        if all(map(lambda lst: isinstance(lst.get(key), dict), dicts)):
            diff[key] = ['nested', get_diff([dicts[0][key], dicts[1][key]])]
        elif dicts[0].get(key) == dicts[1].get(key):
            diff[key] = ['same', dicts[0].get(key)]
        elif dicts[0].get(key) is None:
            diff[key] = ['added', dicts[1].get(key)]
        elif dicts[1].get(key) is None:
            diff[key] = ['deleted', dicts[0].get(key)]
        else:
            diff[key] = ['modified', dicts[0].get(key), dicts[1].get(key)]
    return diff
