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
    tweets = db.relationship('Tweet', backref='user', lazy=True)

    @classmethod
    def create_from_dict(cls, user_info):
        """
        Creates user object and save it from user_info  retrieved from twitter client.
        """
        pass


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_tweet_id = db.Column(db.String(60), index=True)
    content = db.Column(db.Text)
    retweet = db.Column(db.Integer, default=0)
    favorite = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @classmethod
    def create_from_list(cls, tweets_list, user_id):
        """
        Creates and saves list of tweets for a specific user.
        """
        pass


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
        User.create_from_dict(user_info)
        return "user with id: {}".format(user_id)


@app.route('/users/<user_id>/posts')
def get_posts(user_id):
    local = request.args.get('local', False)

    if local:
        return "posts of user with id: {} from db".format(user_id)
    else:
        tweets = twitter.tweets(user_id)
        Tweet.create_from_list(tweets, user_id)
        return "posts of user with id: {}".format(user_id)


if __name__ == '__main__':
    app.run()
