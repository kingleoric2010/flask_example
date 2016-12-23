from flask import Flask, url_for, redirect, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    #return 'Hello World'
    return redirect(url_for('show_user_profile', username='laimingxing'))

@app.route('/about/')
def about():
    return redirect(url_for('static', filename='style.css'))

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    # show the user profile for that user
    age = request.args.get('age', -1)
    return 'HTTP method : {0} User {1} age {2}'.format(request.method, username, age)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
