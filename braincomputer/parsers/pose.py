import json


def parse_pose(snapshot):
    data = json.loads(snapshot)
    return json.dumps({
        'user': data['user'],
        'rotation': data['rotation'],
        'translation': data['translation']
    })


parse_pose.field = 'pose'