import json
import argparse


def load_data(filepath):
    with open(filepath,encoding='utf8') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    """
    We use json.dumps for 'pretty print' output
    data - input json
    ensure_ascii - these characters will be output as-is and not be converted to unicode characters.
    sort_keys - for sorting by key
    indent - for indent each level
    """
    return json.dumps(data,ensure_ascii=False,sort_keys=True,indent=4)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='''Display a json.''')
    parser.add_argument('json_file', type=str, help='filepath')

    user_input = parser.parse_args()

    print(pretty_print_json(load_data(user_input.json_file)))
