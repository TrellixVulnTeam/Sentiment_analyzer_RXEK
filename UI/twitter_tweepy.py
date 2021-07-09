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
    ID=url.pop()
    tweet=api.get_status(ID,tweet_mode='extended')
    return tweet.full_text


def select_option(opt,data):
    elecion =''
    if(opt=='user'):
        print('usuario')
    elif(opt=='hashtag'):
        print('hashtag')
    elif(opt=='url'):
        elecion = getTweet(data)
    print(elecion)
    return elecion
