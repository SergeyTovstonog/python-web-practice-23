from bottle import Bottle, request, template

# Create a Bottle app instance
app = Bottle()

# Temporary data structure to store blog posts
posts = []

# Route for the home page
@app.get('/')
def index():
    return template('index', posts=posts)

# Route for displaying a specific blog post
@app.get('/post/<post_id:int>')
def show_post(post_id):
    if post_id < len(posts):
        post = posts[post_id]
        return template('post', post=post)
    else:
        return "Post not found!"

# Route for adding a new blog post
@app.post('/add_post')
def add_post():
    title = request.forms.get('title')
    content = request.forms.get('content')
    author = request.forms.get('author')
    if title and content and author:
        posts.append({'title': title, 'content': content, 'author': author})
        return "Post added successfully!"
    else:
        return "Missing title, content, or author!"

if __name__ == '__main__':
    # Run the Bottle app
    app.run(host='localhost', port=8080)
