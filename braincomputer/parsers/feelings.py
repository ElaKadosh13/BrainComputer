import json


def parse_feelings(snapshot):
    data = json.loads(snapshot)
    return json.dumps(data['feelings'])


parse_feelings.field = 'feelings'
