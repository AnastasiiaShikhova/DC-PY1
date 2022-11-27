import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as file:
        data_list = [line.replace(new_line, '').split(delimiter) for line in file]

    head_line = data_list[0]
    list_w_dicts = []
    for value in range(1, len(data_list)):
        result = dict(zip(head_line, data_list[value]))
        list_w_dicts.append(result)
        
    return list_w_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
