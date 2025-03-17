'''
Custom Python CLI for Ubuntu:
A custom Python-based CLI for Ubuntu that allows natural-language file and directory management commands.

Author: Yagnik Poshiya
License: MIT License
Copyright (c) 2025 Yagnik Poshiya
'''

import os
import json
import shutil

from typing import Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # get the absolute path to the directory of this script
JSON_FILE_PATH = os.path.join(BASE_DIR, 'data', 'dir_commands.json') # create a full path to dir_commands.json

try:
	with open(JSON_FILE_PATH) as d: # load JSON commands from file
    		COMMANDS = json.load(d)
except FileNotFoundError: # raise exception if file not found
	COMMANDS = {}

def execute_command(command,*args) -> Any:
    '''
    Executes a command dynamically based on JSON-defined commands.

    Args:
        command (str): The command name as defined in `commands.json` e.g. 'create dir'
        *args (tuple): Arguments to be inserted into the command e.g. 'dir_name'

    Raises:
        KeyError: If the command does not exist in `commands.json`.
        Exception: If an error occurs during execution.
    '''

    if command in COMMANDS:
        try:
            command_code = COMMANDS[command].format(*args) # replace placeholders `{}` in the command string with arguments
            result = eval(command_code) # executes the command dynamically
            print(result)
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('Command not found.')
