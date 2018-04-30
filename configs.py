# Farzard's access configs
# access_token = '911524356227874817-J2SGtzRPjK1Sj4KJMCAL4Ym23Rpbs7N'
# access_token_secret = 'TStpFH4xwT9UWx8gBkrnXethBYCjSYEkfWKYnExxpC9x0'
# consumer_key = 'h4lqnpDlOKdblfd8avhWizUVY'
# consumer_secret = 'VwFz27qqwpD2MNkDOc5CcJPa9a5YV6ayopJM5aHfesZUdGhm8z'

# #Lu'a account
# access_token = '987908747375726593-yp9g2tc5FJMfr54eIc8mI8mkboX9VNC'
# access_token_secret = 'hH5K46mLTHk5Yn51gesTnrq3YYUN5vGOBDjWx8PdBbdEm'
# consumer_key = '1RcIwPa92JvKPegrsRzSWzXht'
# consumer_secret = 'AFceGbD4TzRGmqRz8oq65ovHIsAuG7WlwkzfsqEvz5WgYJDoUw'

#Vivian
# Vivian
# Consumer Key (API Key)	9uWwELoYRA4loNboCqe4P7XZD
# Consumer Secret (API Secret)	ZhIOn2XPAnVtDjbh4iVrANG4gq7zTCJdJZAAlDpPmKAFpNz4gF
# Access Token	2344719422-4a94VSU2kjHzgFp1Kap9uoAAvE5R2n9vb4H5Atz
# Access Token Secret	O5H5r7QyOTct7yFFlePITJGcuIJPBmgyDBunIYRVjYELq

configs = {}

# processor_1 information_Lu
processor_1 = {}
processor_1['couchdb-admin-username'] = 'admin'
processor_1['couchdb-admin-password'] = 'team38'
# for local testing, it's "localhost:5984/"
processor_1['couchdb-address'] = '115.146.85.230:5984/'
processor_1['couchdb-db-name'] = 'tweet'
processor_1['google_geo_api_key'] = 'AIzaSyDvl2TZCk0kU0-3dayOGMfVUoEDw38T44o'
processor_1['consumer_key'] = '1RcIwPa92JvKPegrsRzSWzXht'
processor_1['consumer_secret'] = 'AFceGbD4TzRGmqRz8oq65ovHIsAuG7WlwkzfsqEvz5WgYJDoUw'
processor_1['access_token'] = '987908747375726593-yp9g2tc5FJMfr54eIc8mI8mkboX9VNC'
processor_1['access_token_secret'] = 'hH5K46mLTHk5Yn51gesTnrq3YYUN5vGOBDjWx8PdBbdEm'
# example:	37.781157 -122.398720 1mi
processor_1['twitter-geo-latlngrad'] = '-36.816,145.137,100.00km'

# processor_2 information_Farzard
processor_2 = {}
processor_2['couchdb-admin-username'] = 'admin'
processor_2['couchdb-admin-password'] = 'team38'
processor_2['couchdb-address'] = '115.146.85.230:5984/'
processor_2['couchdb-db-name'] = 'tweet'
processor_2['google_geo_api_key'] = 'AIzaSyD76J5qqZZNeYd7f99KWASdtAUCX3dsN4E'
processor_2['consumer_key'] = 'h4lqnpDlOKdblfd8avhWizUVY'
processor_2['consumer_secret'] = 'VwFz27qqwpD2MNkDOc5CcJPa9a5YV6ayopJM5aHfesZUdGhm8z'
processor_2['access_token'] = '911524356227874817-J2SGtzRPjK1Sj4KJMCAL4Ym23Rpbs7N'
processor_2['access_token_secret'] = 'TStpFH4xwT9UWx8gBkrnXethBYCjSYEkfWKYnExxpC9x0'
processor_2['twitter-geo-latlngrad'] = '-37.743,144.280,100.00km'

# processor_3 information_Vivian
processor_3 = {}
processor_3['couchdb-admin-username'] = 'admin'
processor_3['couchdb-admin-password'] = 'team38'
processor_3['couchdb-address'] = '115.146.85.230:5984/'
processor_3['couchdb-db-name'] = 'tweet'
processor_3['google_geo_api_key'] = 'AIzaSyCg-LnPWOeKDVYTI4rK7w7MRnkKNLIes-4'
processor_3['consumer_key'] = '9uWwELoYRA4loNboCqe4P7XZD'
processor_3['consumer_secret'] = 'ZhIOn2XPAnVtDjbh4iVrANG4gq7zTCJdJZAAlDpPmKAFpNz4gF'
processor_3['access_token'] = '2344719422-4a94VSU2kjHzgFp1Kap9uoAAvE5R2n9vb4H5Atz'
processor_3['access_token_secret'] = 'O5H5r7QyOTct7yFFlePITJGcuIJPBmgyDBunIYRVjYELq'
processor_3['twitter-geo-latlngrad'] = '-38.366,145.598,100.00km'

configs[1] = processor_1
configs[2] = processor_2
configs[3] = processor_3
