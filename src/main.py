import tweepy
import utils.auth_tokens as auth_tokens

# Authenticate to Twitter
auth = tweepy.OAuthHandler(auth_tokens.TWITTER_API_KEY,
                           auth_tokens.TWITTER_API_KEY_SECRET)
auth.set_access_token(auth_tokens.TWITTER_ACCESS_TOKEN,
                      auth_tokens.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    raise e
