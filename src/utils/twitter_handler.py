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

    def tweet_dollar_price(self, dollar_info):
        self.api.update_status(
            f"Dólar Canadense valendo: {dollar_info['ask']}")


if __name__ == "__main__":
    print("\N{grinning face}")
