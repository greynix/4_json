import json
from pprint import pprint
from sys import argv


def load_data(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    """
    We use pprint for 'pretty print' output
    """
    return pprint(data)


if __name__ == '__main__':
    pretty_print_json(load_data(argv[1]))
