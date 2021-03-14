import tweepy
import utils.auth_tokens as auth_tokens
import utils.twitter_handler as twitter_handler

# Authenticate to Twitter
tweepy_auth = tweepy.OAuthHandler(auth_tokens.TWITTER_API_KEY,
                                  auth_tokens.TWITTER_API_KEY)
tweepy_auth.set_access_token(auth_tokens.TWITTER_ACCESS_TOKEN,
                             auth_tokens.TWITTER_ACCESS_TOKEN)

tweepy_api = tweepy.API(tweepy_auth, wait_on_rate_limit=True,
                        wait_on_rate_limit_notify=True)

twitter_handler = twitter_handler.TwitterHandler(tweepy_auth, tweepy_api)

try:
    tweepy_api.verify_credentials()
    print("Authentication OK")

    tweepy_api.update_status("Tweet com emoji ��")
    print("Tweet Enviado!")
except tweepy.error.TweepError as tweepError:
    print("Error during authentication")
    raise tweepError
