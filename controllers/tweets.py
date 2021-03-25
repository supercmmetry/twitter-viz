from typing import List

import tweepy
import twint
from deps import api
from models import TweetModel


class TweetController:
    def __init__(self):
        self.tweets: List[TweetModel] = []
        self.hash_tags: List[str] = []

    def tweepy_query(self, query, limit=5):
        tweets = []
        for tweet in tweepy.Cursor(api.search, q=query).items(limit):
            tweets.append(TweetModel.from_tweepy_object(tweet))

        self.tweets = tweets
        return tweets

    def twint_query(self, query, limit=5):
        config = twint.Config()
        config.Search = query
        config.Limit = limit
        config.Hide_output = True
        config.Pandas = True

        twint.run.Search(config)
        self.tweets = TweetModel.from_twint_list()[:limit]
        return self.tweets

    def load_hash_tags(self):
        hash_tags = set()
        for tweet in self.tweets:
            for hash_tag in tweet.hash_tags:
                hash_tags.add(hash_tag)

        self.hash_tags = list(hash_tags)
