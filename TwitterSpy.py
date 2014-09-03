#Python program that checks a user's tweets every N seconds for a tweet containing a specified string

from twitter import *
from pprint import pprint
import time
import msvcrt
import json
import ast
import webbrowser



ACCESS_TOKEN = "2784389341-wqC1Tck0nMU16VMtRn9UQwGh1jOXsKC0p5vQdI"
ACCESS_TOKEN_SECRET = "pYc3kXRjrREVlTwkHhCaSynKqC91fskfTsKmH5GfB61MA"

CONSUMER_KEY = "MtiQ2xbUIcG5gFu3gfUrsgsxa"
CONSUMER_SECRET = "S8VeGHCF0EGRVHFwo42zU57Nz1gIbuQuphV7lnXIqZfPHHDQLH"





t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))



search_string = input("Enter a search string: ")
search_interval = input("Enter search interval(seconds)")

twitter_name = "@TwitterNameGoesHere"



def checkTweets(name):
    

    try:
        while True:
            tweets = t.statuses.user_timeline(screen_name=twitter_name, count=1, exclude_replies=True)
           
            

            json_string = json.dumps(tweets)

            jason = json.loads(json_string)

            pprint("Tweets --> " + json_string)
            #print("URL --> " + jason[0]['entities']['urls'][0]['expanded_url'])
          

            
            
            if name in jason[0]['text']:
                
                print("Found Match!")

                #Extract the URL from the tweet
                url = jason[0]['entities']['urls'][0]['expanded_url']
                print("URL --> " + url)
                
                   
                    
                



                #Open user's browser and navigate to the URL from the tweet
                webbrowser.open(url, new=0, autoraise=True)



                #Alternatively you could write the matched tweet to a file

              
                break
                
                
            else:
                print("Sorry, no match found! Retrying in 5 seconds")
                time.sleep(int(search_interval))
                continue
            break
    except KeyboardInterrupt:
        pass

    

    
checkTweets(search_string)  
    
    


