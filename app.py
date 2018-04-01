from flask import Flask

app = Flask(__name__)


@app.route('/users')
def get_users():
    return "All users"


@app.route('/users/<user_id>')
def get_user(user_id):
    return "user with id: {}".format(user_id)


@app.route('/users/<user_id>/posts')
def get_posts(user_id):
    return "posts of user with id: {}".format(user_id)


if __name__ == '__main__':
    app.run()
