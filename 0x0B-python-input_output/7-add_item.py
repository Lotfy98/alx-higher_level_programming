#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
    and then saves them to a file"""

import sys


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    args = load_from_json_file(filename)
except FileNotFoundError:
    args = []


args.extend(sys.arga[1:])

save_to_json_file(args, filename)
