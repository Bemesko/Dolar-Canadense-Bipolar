import tweepy.error
import json


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
        try:
            self.api.update_status(f""" 
            Dólar Canadense : {dollar_info['ask']} às {dollar_info['create_date']}
            
            """ + datastore["good"][0]+"""
            
            """)
            print("Tweet Enviado com Sucesso!")
        except Exception as e:
            print(e)
            raise e


if __name__ == "__main__":
    # print("\N{grinning face}")
    print(datastore["good"][0])
