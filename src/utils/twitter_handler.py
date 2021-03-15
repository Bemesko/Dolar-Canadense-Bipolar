import tweepy.error
import json
import emoji



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
        if float(dollar_info['pctChange']) > 0:
            rised = "Subiu!"
            reaction = self.tweets_reactions["bad"]["quotes"][0]
            emoji_reaction = self.tweets_reactions["bad"]["emojis"][2]
        else:
            rised = "Caiu!"
            reaction = self.tweets_reactions["good"]["quotes"][0]
            emoji_reaction = self.tweets_reactions["good"]["emojis"][2]

        price = round(float(dollar_info['ask']), 2) 
        self.api.update_status((emoji.emojize(f"""{rised} {emoji_reaction} - R$ {price} às {dollar_info['check_time']}  
        
{reaction}
        """, use_aliases= True)))


#         texto = ":smile:"
#         print((emoji.emojize(f"""{rised} {texto} Dolar canadense: {dollar_info['ask']} às {dollar_info['check_time']}  
# {reaction}
#         """, use_aliases= True)))


#         print(emoji.emojize("oi :hushed:", use_aliases= True))



if __name__ == "__main__":
    # print("\N{grinning face}")
    pass
        
