import pathlib
import http.server
from datetime import datetime

from braincomputer.website import Website

_INDEX_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface</title>
    </head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
'''
_USER_LINE_HTML = '''
<li><a href="/users/{user_id}">user {user_id}</a></li>
'''
_USERS_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <table>
            {thoughts}
        </table>
    </body>
</html>
'''
_THOUGHT_LINE_HTML = '''
<tr>
    <td>{timestamp}</td>
    <td>{thought}</td>
</tr>
'''

root_path = pathlib.Path(__file__).absolute().parent.parent
directory_path = ""
website = Website()



@website.route("/")
def index():
    if directory_path == "":
        return 404, ''
    users_lines_html = []
    for user in directory_path.iterdir():
        id = user.name
        users_lines_html.append(_USER_LINE_HTML.format(user_id=id))  # add all the sub htmls - users htmls
    users_list = '\n'.join(users_lines_html)
    index_html_page = _INDEX_HTML.format(users=users_list)  # create the index html
    return 200, index_html_page

@website.route("/users/([0-9]+)")
def user(user_id):
    if directory_path == "":
        return 404, ''
    current_user_directory_path = directory_path / user_id
    thoughts_lines_html = []
    for thought in current_user_directory_path.iterdir():
        thought_timestamp = datetime.strptime(thought.stem, '%Y-%m-%d_%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S')
        thought_content = thought.read_text()
        thoughts_lines_html.append(_THOUGHT_LINE_HTML.format(timestamp=thought_timestamp, thought=thought_content))
    thought_list = '\n'.join(thoughts_lines_html)
    users_html_page = _USERS_HTML.format(user_id=user_id, thoughts=thought_list)
    return 200, users_html_page


def run_webserver(address, data_dir):
    global directory_path
    directory_path = pathlib.Path(data_dir)
    website.run(address)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(f'USAGE: {sys.argv[0]} <address> <data_dir>')
        sys.exit()
    try:
        address_array = sys.argv[1].split(':')
        address = (address_array[0], int(address_array[1]))
        data_dir = sys.argv[2]
        run_webserver(address, data_dir)
    except Exception as error:
        print(f'ERROR: {error}')
    sys.exit()


