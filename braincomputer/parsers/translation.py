import json


def parse_translation(context, snapshot):
    context.save("translation.json", json.dumps(dict(
        x=snapshot.translation[0],
        y=snapshot.translation[1],
        z=snapshot.translation[2]
    )))


parse_translation.field = 'translation'
