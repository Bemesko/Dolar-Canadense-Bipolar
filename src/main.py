import tweepy
import utils.auth_tokens as auth_tokens

# Authenticate to Twitter
auth = tweepy.OAuthHandler(auth_tokens.TWITTER_API_KEY,
                           auth_tokens.TWITTER_API_KEY_SECRET)
auth.set_access_token(auth_tokens.TWITTER_ACCESS_TOKEN,
                      auth_tokens.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")

    api.update_status("Olá Twitter!")
    print("Tweet Enviado!")
except Exception as e:
    print("Error during authentication")
    raise e
