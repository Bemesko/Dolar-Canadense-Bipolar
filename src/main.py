import tweepy
import tweepy.error
import utils.auth_tokens as auth_tokens

# Authenticate to Twitter
auth = tweepy.OAuthHandler(auth_tokens.TWITTER_API_KEY,
                           auth_tokens.TWITTER_API_KEY)
auth.set_access_token(auth_tokens.TWITTER_ACCESS_TOKEN,
                      auth_tokens.TWITTER_ACCESS_TOKEN)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")

    api.update_status("Tweet com emoji ��")
    print("Tweet Enviado!")
except tweepy.error.TweepError as tweepError:
    print("Error during authentication")
    raise tweepError
