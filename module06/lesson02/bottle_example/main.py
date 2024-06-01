from bottle import Bottle, request, template, redirect

from connection import get_db_connection

app = Bottle()


@app.route('/')
def index():
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('SELECT id, title, author FROM posts')
        posts = cur.fetchall()
        cur.close()
    return template('index', posts=posts)


@app.route('/post/<post_id:int>')
def show_post(post_id):
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('SELECT title, content, author FROM posts WHERE id = %s', (post_id,))
        post = cur.fetchone()
        cur.close()
    if post:
        return template('post', post=post)
    return "Post not found!"


@app.route('/add', method=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.forms.get('title')
        content = request.forms.get('content')
        author = request.forms.get('author')

        with get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO posts (title, content, author) VALUES (%s, %s, %s)', (title, content, author))
            conn.commit()
            cur.close()

        return redirect('/')
    return template('add_post')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
