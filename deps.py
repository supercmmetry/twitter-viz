import os

import dash
import tweepy

import config

dir_path = os.path.dirname(os.path.realpath(__file__))

external_stylesheets = []
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
auth = tweepy.AppAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)
