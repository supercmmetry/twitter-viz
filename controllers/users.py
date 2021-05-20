from typing import List, Dict, Set

from deps import api
from models import UserModel, TweetModel


class UserController:
    def __init__(self):
        self.tweets: List[TweetModel] = []
        self.user_names: List[str] = []
        self.user_dict: Dict[str, UserModel] = {}
        self.hash_to_user: Dict[str, Set[UserModel]] = {}

    def load_from_tweets(self, tweets: List[TweetModel]):
        self.tweets = tweets
        self.user_names = list(set([tweet.user_name for tweet in tweets]))

    def get_by_username(self, user_name: str) -> UserModel:
        if user_name in self.user_dict:
            return self.user_dict[user_name]

        tweepy_user = api.get_user(user_name)
        user = UserModel.from_tweepy_object(tweepy_user)
        self.user_dict[user.user_name] = user

        return user

    def load_hash_to_user_dict(self):
        self.hash_to_user = {}

        for tweet in self.tweets:
            for hash_tag in tweet.hash_tags:
                if hash_tag not in self.hash_to_user:
                    self.hash_to_user[hash_tag] = set()

                self.hash_to_user[hash_tag].add(self.get_by_username(tweet.user_name))
