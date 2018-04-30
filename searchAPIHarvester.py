import tweepy
from textblob import TextBlob
from geoHandler import Geohandler
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('search-api.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""
Skeleton taken from https://dev.to/bhaskar_vk/how-to-use-twitters-search-rest-api-most-effectively
"""


class TweetProcessor():
    def __init__(self,google_geo_api_key, twitter_consumer_key, twitter_consumer_secret, twitter_access_token,
                 twitter_access_token_secret, twitter_geo_param, processor_id, couchdb, since_id=None, max_id=-1,tweets_per_query=100,
                 search_query='*'):
        self.google_geo_api_key = google_geo_api_key
        self.twitter_consumer_key = twitter_consumer_key
        self.twitter_consumer_secret = twitter_consumer_secret
        self.twitter_access_token = twitter_access_token
        self.twitter_access_token_secret = twitter_access_token_secret
        self.twitter_geo_param = twitter_geo_param
        self.couchdb = couchdb
        self.since_id = since_id
        self.max_id = max_id
        self.tweets_per_query = tweets_per_query
        self.search_query = search_query
        self.processor_id = processor_id

        auth = tweepy.OAuthHandler(self.twitter_consumer_key, self.twitter_consumer_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True,
                        wait_on_rate_limit_notify=True)

        if not self.api:
            print("Can't Authenticate")

        self.geo_handler = Geohandler(google_geo_api_key)



    def run(self):

        #searchQuery = '*'
        #geo = '-37.808704,144.960472,10km'
        #tweetsPerQry = 100  # this is the max the API permits

        # If results from a specific ID onwards are read, set since_id to that ID.
        # else default to no lower limit, go as far back as API allows
        #self.since_Id = None

        # If results only below a specific ID are, set max_id to that ID.
        # else default to no upper limit, start from the most recent tweet matching the search query.
        #self.max_id = -1



        maxTweets = 100000000  # Some arbitrary large number
        tweetCount = 0
        while tweetCount < maxTweets:
            try:
                if self.max_id <= 0:
                    if not self.since_id:
                        new_tweets = self.api.search(q=self.search_query, count=self.tweets_per_query,geocode=self.twitter_geo_param)
                    else:
                        new_tweets = self.api.search(q=self.search_query, count=self.tweets_per_query,
                                                since_id=self.since_id,geocode=self.twitter_geo_param)
                else:
                    if not self.since_id:
                        new_tweets = self.api.search(q=self.search_query, count=self.tweets_per_query,
                                                max_id=str(self.max_id - 1),geocode=self.twitter_geo_param)
                    else:
                        new_tweets = self.api.search(q=self.search_query, count=self.tweets_per_query,
                                                max_id=str(self.max_id - 1),
                                                since_id=self.since_id, geocode=self.twitter_geo_param)
                if not new_tweets:
                    logger.error("No more tweets found. Quitting...")
                    break

                tweetCount += len(new_tweets)

                for twit_obj in new_tweets:
                    tweet = twit_obj._json

                    if tweet and tweet['coordinates'] and tweet['coordinates']['coordinates']:
                        lat=tweet['coordinates']['coordinates'][1]
                        lng=tweet['coordinates']['coordinates'][0]
                        address = self.geo_handler.getAddress(lat,lng)
                        post_code = self.geo_handler.getPostCode(address)

                        sentiment = TextBlob(tweet['text']).sentiment.polarity
                        try:
                            process_info = {'post-code': post_code, 'address': address,
                                            'sentiment': sentiment, 'processor-id': self.processor_id}
                            tweet['process-info'] = process_info

                            #In case there are duplicates in database
                            if not (str(tweet['id']) in self.couchdb):
                                self.couchdb[str(tweet['id'])] = tweet

                            else:
                                doc = self.couchdb[str(tweet['id'])]
                                self.couchdb.delete(doc)
                                self.couchdb[str(tweet['id'])] = tweet

                            logger.info("Tweet added to the database with id: " + str(tweet['id']))
                        except Exception as e:
                            logger.exception("Error writing to database: " + str(e))

                    #Also move those data without location into database
                    else:
                        sentiment = TextBlob(tweet['text']).sentiment.polarity
                        try:
                            process_info = {'post-code': None, 'address': None,
                                            'sentiment': sentiment, 'processor-id': self.processor_id}
                            tweet['process-info'] = process_info

                            # In case there are duplicates in database
                            if not (str(tweet['id']) in self.couchdb):
                                self.couchdb[str(tweet['id'])] = tweet

                            else:
                                doc = self.couchdb[str(tweet['id'])]
                                self.couchdb.delete(doc)
                                self.couchdb[str(tweet['id'])] = tweet

                            logger.info("Tweet added to the database with id: " + str(tweet['id']))
                        except Exception as e:
                            logger.exception("Error writing to database: " + str(e))


                print("Downloaded {0} tweets".format(tweetCount))
                self.max_id = new_tweets[-1].id

            except tweepy.TweepError as e:
                # Just exit if any error
                logger.exception("Tweepy error : " + str(e))
                break