<!DOCTYPE html>
<html>
<head>
    <title>Simple Blog</title>
</head>
<body>
    <h1>Welcome to the Simple Blog</h1>
    <ul>
        % for post_index, post in enumerate(posts):
            <li><a href="/post/{{post_index}}">{{post['title']}}</a> by {{post['author']}}</li>
        % end
    </ul>
    <hr>
    <!--
    <h2>Add a New Post</h2>
    <form action="/add_post" method="post">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content"></textarea><br>
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author"><br>
        <input type="submit" value="Add Post">
    </form>
    -->
</body>
</html>
