from json import dumps, loads
from uuid import uuid4

def to_file(dict_to_save):
    file_name = uuid4()
    file_path = f'/var/tmp/{file_name}.txt' 
    with open(file_path, 'w') as f:
        f.write(dumps(dict_to_save))
    return file_path

def to_dict(file_path):
    text = ''
    with open(file_path, 'r') as f:
        text = f.readlines()
    return loads(''.join(text))