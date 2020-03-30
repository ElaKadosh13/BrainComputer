
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
<li><a href="/users/{user_id}">User: {user_id}</a></li>
'''
_USERS_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Name: {user_name}</p>
         <p>Gender: {user_gender}</p> 
         <p>Birthday: {user_birthday}</p>
         <p>Snapshots timestamps: </p>
        <ul>
            {thoughts}
        </ul>
    </body>
</html>
'''
_THOUGHT_LINE_HTML = '''
<li><a href="/users/{user_id}/{ts}">Timestamp: {timestamp}</a></li>
'''

_SNAPSHOT_HTML = '''
<html>
    <head>
        <title>brain computer interface: user {user_id} timestamp: {timestamp}</title>
    </head>
    <body>
        <p>user {user_id} timestamp: {timestamp}</p>
        <p>pose:</br>translation: {translation}</br>rotation: {rotation}</p>
        <p>feelings:{feelings}</p>
        <p>color_image: </br> <img alt="color image missing" src={color_image_path} width={color_image_width}, height={color_image_height}></p>
        <p>depth_image: </br> <img alt="depth image missing" src={depth_image_path} width={depth_image_width}, height={depth_image_height}></p>
   </body>
</html>
'''
