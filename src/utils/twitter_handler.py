import tweepy.error
import json


with open("src/utils/tweets.json", "r") as data_file:
    datastore = json.load(data_file)


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
        self.api.update_status(f""" 
        Dolar canadense {}: {dollar_info['ask']} às {dollar_info['create_date']}
        
        """+ datastore["good"][0]+"""
        
        """)




if __name__ == "__main__":
    # print("\N{grinning face}")
    print(datastore["good"][0])
        
