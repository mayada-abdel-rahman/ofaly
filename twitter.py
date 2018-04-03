"""
Twitter API client.

waiting for twitter app approval.
"""


def user_info(user_id):
    """Returns dictionary of user info

    https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show
    """

    # fake data for testing.
    return {
        "name": "Twitter Dev",
        "id_str": "2244994945"
    }


def tweets(user_id, limit=25):
    """Returns list of tweets from user timeline, with limit of 25 by default

    https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.htmlhttps://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html
    """

    # fake data for testing.
    tweets_lst = [
        {
            "id_str": str(848929357519241216 + i),
            "text": "content{}".format(i),
            "retweet_count": i + 1,
            "favorite_count": i + 1,
        }
        for i in range(100)
    ]

    return tweets_lst[:limit]
