class TweetGrabber():
    
    def __init__(self,myApi,sApi,at,sAt):
        import tweepy
        self.tweepy = tweepy
        auth = tweepy.OAuthHandler(myApi, sApi)
        auth.set_access_token(at, sAt)
        self.api = tweepy.API(auth)
        
        
    def strip_non_ascii(self,string):
        ''' Returns the string without non ASCII characters'''
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)
        
    def keyword_search(self,keyword,csv_prefix):
        import csv        
        API_results = self.api.search(q=keyword,rpp=1000,show_user=True,tweet_mode='extended')

        with open(f'{csv_prefix}.csv', 'w', newline='') as csvfile:
            fieldnames = ['tweet_id', 'keyword','tweet_text', 'date', 'user_id', 'follower_count',
                          'retweet_count','user_mentions']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for tweet in API_results:
                text = self.strip_non_ascii(tweet.full_text)
                date = tweet.created_at.strftime('%m/%d/%Y')        
                writer.writerow({
                                'tweet_id': tweet.id_str,
                                'keyword': keyword,
                                'tweet_text': text,
                                'date': date,
                                'user_id': tweet.user.id_str,
                                'follower_count': tweet.user.followers_count,
                                'retweet_count': tweet.retweet_count,
                                'user_mentions':tweet.entities['user_mentions']
                                })   
        return API_results

        
    def user_search(self,user,csv_prefix):
        import csv
        API_results = self.tweepy.Cursor(self.api.user_timeline,id=user,tweet_mode='extended').items()

        with open(f'{csv_prefix}.csv', 'w', newline='') as csvfile:
            fieldnames = ['tweet_id', 'tweet_text', 'date', 'user_id', 'user_mentions', 'retweet_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for tweet in API_results:
                text = self.strip_non_ascii(tweet.full_text)
                date = tweet.created_at.strftime('%m/%d/%Y')        
                writer.writerow({
                                'tweet_id': tweet.id_str,
                                'tweet_text': text,
                                'date': date,
                                'user_id': tweet.user.id_str,
                                'user_mentions':tweet.entities['user_mentions'],
                                'retweet_count': tweet.retweet_count
                                })        
