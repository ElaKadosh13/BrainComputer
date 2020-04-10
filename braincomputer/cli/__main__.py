import sys
import webbrowser

import click
import braincomputer
import requests
from braincomputer.utils.log import log


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("get-users", short_help="http get users")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
def get_users(host, port):
    request = requests.get(f"http://{host}:{port}/users")
    users = request.json()
    for user in users:
        print(f"user: {user['id']}, name: {user['name']}")


@main.command("get-user", short_help="http get users by id")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
@click.argument("user_id", type=int)
def get_user(host, port, user_id):
    request = requests.get(f"http://{host}:{port}/users/{user_id}")
    user = request.json()
    if str(user).startswith("Error:"):
        print(str(user))
    else:
        print(f"user: {user['id']}, name: {user['name']}, birthday: {user['birthday']}, gender: {user['gender']}")


@main.command("get-snapshots", short_help="http get user snapshots")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
@click.argument("user_id", type=int)
def get_snapshots(host, port, user_id):
    request = requests.get(f"http://{host}:{port}/users/{user_id}/snapshots")
    snapshots = request.json()
    if str(snapshots).startswith("Error:"):
        print(str(snapshots))
    else:
        for snapshot in snapshots:
            print(f"id: {snapshot['id']}, timestamp: {snapshot['ts']}")


@main.command("get-snapshot", short_help="http get user snapshot")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
@click.argument("user_id", type=int)
@click.argument("snapshot_id", type=str)
def get_snapshot(host, port, user_id, snapshot_id):
    request = requests.get(f"http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}")
    snapshot = request.json()
    if str(snapshot).startswith("Error:"):
        print(str(snapshot))
    else:
        print(f"snapshot: {snapshot_id}, datetime: {snapshot['ts']}")
        print("Available data:")
        if "translation" in snapshot and "rotation" in snapshot:
            print("pose")
        if "feelings" in snapshot:
            print("feelings")
        if "color_image" in snapshot:
            print("color-image")
        if "depth_image" in snapshot:
            print("depth-image")


@main.command("get-result", short_help="http get user snapshot result")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
@click.option('-s', '--save', default="")
@click.argument("user_id", type=int)
@click.argument("snapshot_id", type=str)
@click.argument("result_name", type=str)
def get_result(host, port, user_id, snapshot_id, result_name, save):
    request = requests.get(f"http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result_name}")
    snapshot = request.json()
    if str(snapshot).startswith("Error:"):
        print(str(snapshot))
    else:
        if result_name == "feelings":
            hunger, thirst, exhastion, happiness = snapshot
            print(f"Hunger: {hunger}\nThirst: {thirst}\nExhaustion: {exhastion}\nHappiness: {happiness}")
        if result_name == "pose":
            print(f"Rotation: {snapshot['rotation']}\nTranslation: {snapshot['translation']}")
        if result_name.endswith("image"):
            width, height, path = snapshot
            print(f"Width:{width}\nHeight:{height}\nPath:{path}")
            print("If you want to see the image you can navigate to the path above, "
                  "OR use the GET request:\n "
                  "python -m braincomputer.cli get-result-data <user id> <snapshot id> <result type>\n"
                  "[result type can be: color-image/depth-image]\n")
        if save:
            print(f"saving data to path {save}")
            with open(save, 'w') as f:
                f.write(str(snapshot))


@main.command("get-result-data", short_help="http get user image result")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8081)
@click.argument("user_id", type=int)
@click.argument("snapshot_id", type=str)
@click.argument("result_name", type=str)
def get_result_data(host, port, user_id, snapshot_id, result_name):
    request = requests.get(f"http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result_name}/data")
    image_path = request.json()
    if str(image_path).startswith("Error:"):
        print(str(image_path))
    else:
        ts = snapshot_id.split("_")[1]
        print(f"To see image in browser use this link - \n http://127.0.0.1:8080/users/{user_id}/{ts}/{result_name} \n(if you changed the default gui port replace 8080 with the port you chose)")


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
