<!DOCTYPE html>
<html>
<head>
    <title>Add a New Post</title>
</head>
<body>
    <h1>Add a New Post</h1>
    <form action="/add" method="post">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content"></textarea><br>
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author"><br>
        <input type="submit" value="Add Post">
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
