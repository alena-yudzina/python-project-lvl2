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


def get_diff(dicts):  # noqa: C901
    dicts = convert_to_output_format(dicts)
    keys = sorted(list({**dicts[0], **dicts[1]}.keys()))
    diff = []
    for key in keys:
        if all(map(lambda lst: isinstance(lst.get(key), dict), dicts)):
            diff.append(create_node('same', key, 'dict',
                        get_diff([dicts[0].get(key), dicts[1].get(key)])))
        elif dicts[0].get(key) == dicts[1].get(key):
            diff.append(create_node('same', key, dicts[0].get(key)))
        else:
            if dicts[0].get(key) is not None:
                if isinstance(dicts[0].get(key), dict):
                    args = ('del', key, 'dict',
                            get_diff([dicts[0].get(key), dicts[0].get(key)]))
                else:
                    args = ('del', key, dicts[0].get(key))
                diff.append(create_node(*args))
            if dicts[1].get(key) is not None:
                if isinstance(dicts[1].get(key), dict):
                    args = ('add', key, 'dict',
                            get_diff([dicts[1].get(key), dicts[1].get(key)]))
                else:
                    args = ('add', key, dicts[1].get(key))
                diff.append(create_node(*args))
    return diff
