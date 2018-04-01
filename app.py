import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import twitter

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


# ------------------- Models ------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_user_id = db.Column(db.String(60), index=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tweets = db.relationship('Tweet', backref='user', lazy=True)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)
    retweet = db.Column(db.Integer, default=0)
    favorite = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# ------------------- Views -------------------
@app.route('/users')
def get_users():
    return "All users"


@app.route('/users/<user_id>')
def get_user(user_id):
    local = request.args.get('local', False)

    if local:
        return "user with id: {} from db".format(user_id)
    else:
        user_info = twitter.user_info(user_id)
        # save to db
        return "user with id: {}".format(user_id)


@app.route('/users/<user_id>/posts')
def get_posts(user_id):
    local = request.args.get('local', False)

    if local:
        return "posts of user with id: {} from db".format(user_id)
    else:
        tweets = twitter.tweets(user_id)
        # save to db
        return "posts of user with id: {}".format(user_id)


if __name__ == '__main__':
    app.run()
