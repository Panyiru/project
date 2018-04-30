from searchAPIHarvester import TweetProcessor
from configs import configs

import couchdb
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('harvester-manager.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

harvester_id = sys.argv[1]
couchdb_address = sys.argv[2]

conf = configs[int(harvester_id)]

couchserver = couchdb.Server('http://'+conf['couchdb-admin-username']+':'
                             +conf['couchdb-admin-password'] + '@'
                             +couchdb_address)


db = couchserver[conf['couchdb-db-name']]

logging.info('Database connection established')

tweetPrc = TweetProcessor(conf['google_geo_api_key'], conf['consumer_key'], conf['consumer_secret'],
                          conf['access_token'], conf['access_token_secret'], conf['twitter-geo-latlngrad'],str(harvester_id), db)

logging.info('TweetProcessor created')
tweetPrc.run()
logging.error("Tweet processing stopped")