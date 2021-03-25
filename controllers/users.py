class UserController:
    def __init__(self, tweets):
        self.tweets = tweets
        self.users = [tweet.author for tweet in tweets]