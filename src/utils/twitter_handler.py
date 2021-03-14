import tweepy.error
import json

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

    def tweet_dollar_price(self, dollar_info):
        self.api.update_status(f"""{subiu} Dolar canadense: {dollar_info['ask']} às {dollar_info['check_time']}  
        {self.tweets_reactions['good'][0]}
        """)



if __name__ == "__main__":
    # print("\N{grinning face}")
    pass
        
