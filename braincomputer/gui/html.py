
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
<li><a href="/users/{user_id}">User: {user_id}, Name: {user_name}</a></li>
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
         <li><a href="/users/{user_id}/feelings_overtime">check out how feelings look over time</a></li>
         <li><a href="/users/{user_id}/pose_overtime">check out how poses look over time</a></li>
         <li><a href="/users/{user_id}/color_image_overtime">check out how color images look over time</a></li>
         <li><a href="/users/{user_id}/depth_image_overtime">check out how depth images look over time</a></li>
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
_IMAGE_HTML = '''
<html>
    <body>
        <p>image: </br> <img alt="image missing" src={image_path} width={image_width}, height={image_height}></p>
   </body>
</html>
'''
_FEELINGS_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the feelings data:</p>
        <ul>
            {feelings_data_overtime}
        </ul>
    </body>
</html>
'''
_FEELINGS_LINE_HTML = '''
<li><p>{feelings_data}</p></li>
'''
_POSE_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the pose data:</p>
        <ul>
            {pose_data_overtime}
        </ul>
    </body>
</html>
'''
_POSE_LINE_HTML = '''
<li><p>Rotation: {rotation_data}</br>Translation: {translation_data}</p></li>
'''
_IMAGE_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the images:</p>
        <ul>
            {image_data_overtime}
        </ul>
    </body>
</html>
'''
_IMAGE_LINE_HTML = '''
<li>       
    <p>image: </br> <img alt="image missing" src={path} width={width}, height={height}></p>
</li>
'''
_FEELINGS_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the feelings data:</p>
        <ul>
            {feelings_data_overtime}
        </ul>
    </body>
</html>
'''
_FEELINGS_LINE_HTML = '''
<li><p>{feelings_data}</p></li>
'''
_POSE_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the pose data:</p>
        <ul>
            {pose_data_overtime}
        </ul>
    </body>
</html>
'''
_POSE_LINE_HTML = '''
<li><p>Rotation: {rotation_data}</br>Translation: {translation_data}</p></li>
'''
_IMAGE_OVERTIME_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Id: {user_id}, Name: {user_name}</p>              
         <p>check out all the images:</p>
        <ul>
            {image_data_overtime}
        </ul>
    </body>
</html>
'''
_IMAGE_LINE_HTML = '''
<li>       
    <p>image: </br> <img alt="image missing" src={path} width={width}, height={height}></p>
</li>
'''