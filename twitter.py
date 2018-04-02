"""
Twitter API client.

waiting for twitter app approval.
"""


def user_info(user_id):
    """Returns dictionary of user info"""

    # fake data for testing.
    return {
        'name': 'UserName',
        'email': 'random@email.com'
    }


def tweets(user_id, limit=25):
    """Returns list of tweets from user timeline, with limit of 25 by default"""

    # fake data for testing.
    tweets_lst = [
        {
            'content': 'content{}'.format(i),
            'retweet': i + 1,
            'favorite': i + 1,
        }
        for i in range(100)
    ]

    return tweets_lst[:limit]
