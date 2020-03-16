import json


def parse_translation(snapshot):
    data = json.loads(snapshot)
    return json.dumps(data['translation'])


parse_translation.field = 'translation'
