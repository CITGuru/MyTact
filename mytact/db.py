import json
import os
from mytact.utils import getConfigDir

DB_FILE = os.path.join(getConfigDir(), "data.json")

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_FILE) 

def load():
    with open(PATH, 'r') as _fp:
        data = json.load(_fp)
    return data

def insert(data):
    with open(PATH, 'w') as _fp:
        json.dump(data, _fp)