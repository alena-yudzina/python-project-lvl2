ADD = '  + '
DEL = '  - '
SAME = '    '


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


def get_diff(dicts):
    dicts = convert_to_output_format(dicts)
    keys = sorted(list({**dicts[0], **dicts[1]}.keys()))
    diff = []
    for key in keys:
        if all(map(lambda lst: isinstance(lst.get(key), dict), dicts)):
            node = {
                'diff': SAME,
                'name': key,
                'value': 'dict',
                'children': get_diff([dicts[0].get(key), dicts[1].get(key)]),
            }
            diff.append(node)
        else:
            if dicts[0].get(key) == dicts[1].get(key):
                node = {
                    'diff': SAME,
                    'name': key,
                    'value': dicts[0].get(key),
                }
                diff.append(node)
            else:
                if dicts[0].get(key) is not None:
                    if isinstance(dicts[0].get(key), dict):
                        node = {
                            'diff': DEL,
                            'name': key,
                            'value': 'dict',
                            'children': get_diff([dicts[0].get(key),
                                                 dicts[0].get(key)]),
                        }
                    else:
                        node = {
                            'diff': DEL,
                            'name': key,
                            'value': dicts[0].get(key),
                        }
                    diff.append(node)
                if dicts[1].get(key) is not None:
                    if isinstance(dicts[1].get(key), dict):
                        node = {
                            'diff': ADD,
                            'name': key,
                            'value': 'dict',
                            'children': get_diff([dicts[1].get(key),
                                                 dicts[1].get(key)]),
                        }
                    else:
                        node = {
                            'diff': ADD,
                            'name': key,
                            'value': dicts[1].get(key),
                        }
                    diff.append(node)
    return diff
