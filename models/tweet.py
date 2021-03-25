import twint


class TweetModel:
    @staticmethod
    def __twint_to_pandas():
        return twint.run.output.panda.Tweets_df[twint.run.output.panda.Tweets_df.columns]

    def __init__(self):
        self.text = ''
        self.name = ''
        self.user_name = ''
        self.hash_tags = []

    @staticmethod
    def from_tweepy_object(obj):
        tweet = TweetModel()
        tweet.text = obj.text
        tweet.name = obj.author.name
        tweet.user_name = obj.author.screen_name
        tweet.hash_tags = obj.entities['hashtags']
        return tweet

    @staticmethod
    def from_twint_list():
        tweets = []
        df = TweetModel.__twint_to_pandas()

        for _, row in df.iterrows():
            tweet = TweetModel()
            tweet.text = row['tweet']
            tweet.name = row['name']
            tweet.user_name = row['username']
            tweet.hash_tags = row['hashtags']
            tweets.append(tweet)

        return tweets
