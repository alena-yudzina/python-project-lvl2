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
    keys = set({**dicts[0], **dicts[1]}.keys())
    diff = {}
    for key in keys:
        if all(map(lambda lst: isinstance(lst.get(key), dict), dicts)):
            diff[key] = ['nested', get_diff([dicts[0][key], dicts[1][key]])]
        elif dicts[0].get(key) == dicts[1].get(key):
            diff[key] = ['same', dicts[0].get(key)]
        elif key not in dicts[0]:
            diff[key] = ['added', dicts[1].get(key)]
        elif key not in dicts[1]:
            diff[key] = ['deleted', dicts[0].get(key)]
        else:
            diff[key] = ['modified', dicts[0].get(key), dicts[1].get(key)]
    return diff
