
import tweepy


def o_auth():
    auth = tweepy.OAuthHandler("WfuAkJq5Z1ZaPnMpxaLCqaayJ",
                               "YHfIKJkZno5os636QLfVmS6qjbjTM5XP9uUV8XyOre35lul4Zn")
    auth.set_access_token("4798274380-EGipvsU51HZjnoEJri1oVBU4lhHKpWeh3qsBNk8",
                          "dpe95qyKrOHNfW7x2ZFLg74WumQLrAM8towc8lefU2PKf")

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return auth


api = tweepy.API(o_auth())


def getTweet(url):
    url = url.split('/')
    ID = url.pop()
    tweet = api.get_status(ID, tweet_mode='extended')
    return tweet.full_text


def get_tweets_by_user(user):
    lista =[]
    tweets = api.user_timeline(user, tweet_mode='extended')

    for i in tweets[:10]:
    
        value=i.full_text
       
        lista.append(value)
   
    return lista
# get_tweets_by_user('_tech_J')
def get_tweets_by_query(query):
    lista =[]
    tweets = api.search(query, tweet_mode='extended')

    for i in tweets[:10]:
        print(i)
        value=i.full_text
       
        lista.append(value)
   
    return lista
def select_option(opt, data):
 
    elecion = ''
    if(opt == 'user'):
        elecion = get_tweets_by_user(data)
    elif(opt == 'hashtag'):
        elecion=get_tweets_by_query(data)
    elif(opt == 'url'):
        elecion = getTweet(data)
   
    return elecion
