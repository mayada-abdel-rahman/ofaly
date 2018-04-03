import os

from flask import Flask, request, render_template
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

        id_str = user_info.get('id_str')
        user = cls.query.filter_by(provider_user_id=id_str).first()

        # user doesn't exist.
        if not user:
            user = cls(
                provider_user_id=id_str,
                name=user_info.get('name')
            )

            db.session.add(user)
            db.session.commit()

        return user


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_tweet_id = db.Column(db.String(60), index=True)
    content = db.Column(db.Text)
    retweet = db.Column(db.Integer, default=0)
    favorite = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @classmethod
    def tweet_not_exist(cls, id_str):
        return not cls.query.filter_by(provider_tweet_id=id_str).first()

    @classmethod
    def create_from_list(cls, tweets_list, user_id):
        """
       Creates and saves list of tweets for a specific user.
       """

        # create list of tweets that don't exist in db.
        new_tweets = [
            cls(
                provider_tweet_id=tweet.get('id_str'),
                content=tweet.get('text'),
                retweet=tweet.get('retweet_count'),
                favorite=tweet.get('favorite_count'),
                user_id=user_id,
            )
            for tweet in tweets_list if cls.tweet_not_exist(tweet.get('id_str'))
        ]

        # new tweets exist.
        if new_tweets:
            for tweet in new_tweets:
                db.session.add(tweet)
            db.session.commit()

        return new_tweets


# ------------------- Views -------------------
@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/<user_id>')
def get_user(user_id):
    local = request.args.get('local', False)

    # create new user first.
    if not local:
        user_info = twitter.user_info(user_id)
        User.create_from_dict(user_info)

    user = User.query.filter_by(user_id=user_id).first()

    return render_template('user.html', user=user)


@app.route('/users/<user_id>/posts')
def get_posts(user_id):
    local = request.args.get('local', False)

    # create new tweets first if any exist.
    if not local:
        tweets = twitter.tweets(user_id)
        Tweet.create_from_list(tweets, user_id)

    tweets = Tweet.query.filter_by(user_id=user_id).first()

    return render_template('user.html', tweets=tweets)


if __name__ == '__main__':
    app.run()