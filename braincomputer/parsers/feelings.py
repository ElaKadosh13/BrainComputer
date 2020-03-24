import json


def parse_feelings(snapshot):
    data = json.loads(snapshot)
    return json.dumps({'user': data['user'],
                       'ts': data['timestamp'],
                       'feelings': data['feelings']})


parse_feelings.field = 'feelings'
