def convert_to_output_format(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def get_diff(python_dicts):
    dicts = []
    for dct in python_dicts:
        dct = {k: convert_to_output_format(v) for k, v in dct.items()}
        dicts.append(dct)
    merge_dict = {**dicts[0], **dicts[1]}
    keys = sorted(list(merge_dict.keys()))
    result = '{\n'
    for key in keys:
        is_in_first = key in dicts[0].keys()
        is_in_second = key in dicts[1].keys()
        if is_in_first and is_in_second:
            if dicts[0][key] == dicts[1][key]:
                result += f'    {key}: {dicts[0][key]}\n'
            else:
                result += f'  - {key}: {dicts[0][key]}\n'
                result += f'  + {key}: {dicts[1][key]}\n'
        elif is_in_first:
            result += f'  - {key}: {dicts[0][key]}\n'
        else:
            result += f'  + {key}: {dicts[1][key]}\n'
    result += '}'
    return result
