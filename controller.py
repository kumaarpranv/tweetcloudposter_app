import tweepy 
import numpy as np
import matplotlib.pyplot as plt
import re
import string
import random

consumer_key = "00oLJWTD182lTx2By83GRvtur" 
consumer_secret = "D3Yg85pKTNCesq21N6puPg8HzhqJyAKK1CJnIzaXleGixOGSNg"
access_key = "1098598656368955395-15ySyk5e5ApYx0dKq6pKWsjx8WFyaB"
access_secret = "NQxUeqn3el2Zz41ZFJihZ66q2QEX1RCAxS3S9W7gvBDri"


def set_params(user,num):
    username=user 
    number=num 

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

def space_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, ' ', input_txt)
    return input_txt

def get_tweets(username,no_of_tweets):         
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth)        
        tweets=[]
        for i in range(int(no_of_tweets/20)):
            for j in api.user_timeline(screen_name=username, page = i):
                tweets.append(j)
      
      
        # Empty Array 
        tmp=[]  
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
        return tmp


tw_header=(1500,500)
hd_1080=(1900,1080)
hd_phone=(1600,900)
fb_pc=(820,312)
fb_ph=(640,360)

def start(username,number,ch):
    if(ch=="tw"):
        dims= tw_header
    elif(ch=="hdpc"):
        dims=hd_1080
    elif(ch=="hdph"):
        dims=hd_phone
    elif(ch=="fbpc"):
        dims=fb_pc
    elif(ch=="fb_ph"):
        dims=fb_ph
    else:
        dims=tw_header 
    tweets=get_tweets(username,number)
    tweets = np.vectorize(remove_pattern)(tweets, "@[\w]*") 
    tweets = np.vectorize(remove_pattern)(tweets, "RT : [\w]*")
    tweets = np.vectorize(remove_pattern)(tweets, "https?:\/\/.*[\r\n]*")
    tweets = np.vectorize(remove_pattern)(tweets, "\n")
    tweets = np.vectorize(space_pattern)(tweets, "[!@$%^&*()[]{};:,./<>?\|`~-=_+]")

    all_words=' '.join([text for text in tweets])

    letters = string.ascii_lowercase
    fname=''.join(random.choice(letters) for i in range(6))
    fname+='.png'
    from wordcloud import WordCloud 
    wordcloud = WordCloud(width=dims[0], height=dims[1], random_state=21, max_font_size=200).generate(all_words) 
    plt.figure(figsize=(10, 7)) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis('off')
    plt.imsave('./static/img/'+fname,wordcloud) 

    return fname
