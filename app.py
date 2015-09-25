import requests
import pprint
import sys

# See http://www.unixtimestamp.com/ to generate Unix timestamps online
payload = {
            'until': 1443200285, # Unix timestamps
            'since': 1443200285, # Unix timestamps
            'limit': 100, # number of posts
            'access_token': '', # your access token
        }

base_api = 'https://graph.facebook.com'
posts_endpoint = base_api + '/me/posts/'

posts_response = requests.get(posts_endpoint, params=payload)

if posts_response.status_code != requests.codes.ok:
    print('Error: ' + posts_response.json()['error']['message'])
    sys.exit(0)

posts_dict = posts_response.json()['data']
#pprint.pprint(posts_dict)

print("Total posts to delete: %d" % len(posts_dict))
for post in posts_dict:
    print("Deleting [%s] %s" % (post['id'], post['name']))
    requests.delete(base_api + '/' + post['id'], params=payload)
    print("Deleted [%s] %s\n" % (post['id'], post['name']))
