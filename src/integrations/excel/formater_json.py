import json


def pretty_json(result: dict):
    print(json.dumps(result, indent=4, default=str))
