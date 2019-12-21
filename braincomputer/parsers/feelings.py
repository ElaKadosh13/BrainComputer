import json


def parse_feelings(context, snapshot):
    context.save("feelings.json", json.dumps(dict(
        hunger=snapshot.user_feelings[0],
        thirst=snapshot.user_feelings[1],
        exhustion=snapshot.user_feelings[2],
        happiness=snapshot.user_feelings[3]
    )))


parse_feelings.field = 'feelings'
