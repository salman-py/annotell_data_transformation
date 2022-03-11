import json
from src.main import ReadFile

if __name__ == '__main__':
    path_to_annotell_annotation = 'annotell_1.json'
    with open(path_to_annotell_annotation, 'r') as content:
        json_body = json.load(content)
    result = ReadFile().convert(json_body)
    print(result)