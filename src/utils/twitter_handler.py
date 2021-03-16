import tweepy.error
import json
import emoji
import random


class TwitterHandler():
    def __init__(self, auth, api):
        self.auth = auth
        self.api = api

        with open("src/utils/tweets.json", "r") as data_file:
            self.tweets_reactions = json.load(data_file)

        try:
            self.api.verify_credentials()

            print("Autenticação OK!")
        except tweepy.error.TweepError as tweepError:
            print("Erro na autenticação!")
            raise tweepError

    def generate_tweet(self, dollar_info):
        if float(dollar_info['pctChange']) > 0:
            rised = "Subiu!"
            reaction = self.tweets_reactions["bad"]["quotes"][0]
            emoji_reaction = self.tweets_reactions["good"]["emojis"][random.randrange(
                0, len(self.tweets_reactions["bad"]["emojis"])-1)]
            sign = "+"
            chart = ":chart_increasing:"
        else:
            rised = "Caiu!"
            reaction = self.tweets_reactions["good"]["quotes"][0]
            emoji_reaction = self.tweets_reactions["good"]["emojis"][random.randrange(
                0, len(self.tweets_reactions["good"]["emojis"])-1)]
            sign = "-"
            chart = ":chart_decreasing:"

        price = round(float(dollar_info['ask']), 2)
        price_rised = abs(
            round((price * float(dollar_info['pctChange'])/100), 2))

        tweet = (f"""
:Canada: {rised} {emoji_reaction} - R${price} às {dollar_info['check_time']}

{reaction}

Variação {chart} {sign} {abs(float(dollar_info['pctChange']))}% (R${abs(float(price_rised))})""")

        emojis_tweet = emoji.emojize(tweet, use_aliases=True)

        return emojis_tweet

    def send_tweet(self, tweet):
        try:
            self.api.update_status(tweet)
            print(tweet)
            print("Tweet enviado com sucesso!")
        except Exception as e:
            print(e)
            raise e
