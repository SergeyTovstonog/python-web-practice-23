<!DOCTYPE html>
<html>
<head>
    <title>Simple Blog</title>
</head>
<body>
    <h1>Welcome to the Simple Blog</h1>
    <ul>
        % for post in posts:
            <li><a href="/post/{{post[0]}}">{{post[1]}}</a> by {{post[2]}}</li>
        % end
    </ul>
    <hr>
    <a href="/add">Add a New Post</a>
</body>
</html>
