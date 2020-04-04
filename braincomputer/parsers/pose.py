import json


def parse_pose(snapshot):
    print("in pose parser!!!!")
    data = json.loads(snapshot)
    return json.dumps({
        'user': data['user'],
        'ts': data['timestamp'],
        'rotation': data['rotation'],
        'translation': data['translation']
    })


parse_pose.field = 'pose'
