import tweepy.error


class TwitterHandler():
    def __init__(self, auth, api):
        self.auth = auth
        self.api = api

        try:
            self.api.verify_credentials()

            print("Autenticação OK!")
        except tweepy.error.TweepError as tweepError:
            print("Erro na autenticação!")
            raise tweepError

    def tweet_dollar_price(self, dollar_price):
        self.api.update_status("")
