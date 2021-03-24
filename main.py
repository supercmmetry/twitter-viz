import tweepy
import config


if __name__ == '__main__':
    auth = tweepy.AppAuthHandler(config.consumer_key, config.consumer_secret)
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.search, q='hacking').items(10):
        print(tweet.author)
