import requests
import urllib
app_access_token = '1961692708.b6455cd.cddbbff1974c407c945955482af38b18'
base_url='https://api.instagram.com/v1/'
print 'Welcome to INSTABOT'
username= raw_input('enter user name:' )


def self_info():    #getting self information

    request_url = (base_url + 'users/self/?access_token=%s') % (app_access_token)
    print 'ffcacearc ' + request_url

    information = requests.get(request_url).json()
    print 'json format', information

    if information['meta']['code'] == 200:
        if len(information['data']):
            print 'username is', (information['data']['username'])
            print 'bio is', (information['data']['bio'])
            print 'profile picture link is ', (information['data']['profile_picture'])
            print 'website is ', (information['data']['website'])
        else:
            print 'invalid user'
    else:
        print 'wrong status code'

self_info();
#
#
#
#
#
#
def user_info(username): #getting user information
     user_request_url = (base_url + 'users/search?q=%s&access_token=%s') % (username, app_access_token)
     print 'URL of user is ' + user_request_url
     user_information = requests.get(user_request_url).json()
     print 'Details of user is ', user_information

     if user_information['meta']['code'] == 200:
         print 'valid user'
     else:
         print ' invalid user'


user_info(username);
#
#
#
#
#
#
def Get_user_id(username): # getting user id
    user_url = (base_url + 'users/search?q=%s&access_token=%s') % (username, app_access_token)

    print 'url is ' + user_url

    user_info = requests.get(user_url).json()

    if user_info['meta']['code'] == 200:
        return user_info['data'][0]['id']
    else:
        print 'status 200 error'

Get_user_id(username);





def self_media(): #downloading your own image
    self_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print self_url
    self_images = requests.get(self_url).json()

    if self_images['meta']['code'] == 200:
        own_image = self_images['data'][0]['id'] + 'jpg'
        own_url = self_images['data'][0]['images']['standard_resolution']['url']
        urllib.urlretrieve(own_url, own_image)
        print 'image has been downloaded'
    else:
        print 'code 200 error'


self_media();

def get_user_image(username): #downloading_user_image
    user_url1=(base_url +   'users/%s/media/recent/?access_token=%s') % (username, app_access_token)
    print user_url1
    user_image=requests.get(user_url1).json()
    print user_image

    if user_image['meta']['code']==200:
        return user_image['data'][0]['id']
    else:
        print 'none'


get_user_image(username);



def get_user_post(username):
  user_id = Get_user_id(username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()

  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
        user_image = user_media['data'][0]['id'] + 'jpg'
        user_url = user_media['data'][0]['images']['standard_resolution']['url']
        urllib.urlretrieve(user_url, user_image)
        print 'user\'s image has been downloaded'
    else:
        print 'code 200 error'


get_user_post(username);



def like_a_post(): #like on a user's post
     like_post_url= (base_url + 'media/1569664842759368126_5793537413/likes')
     payload = {"access_token": app_access_token }
     print 'POST request url : %s' % (like_post_url)
     post_a_like = requests.post(like_post_url, payload).json()
     if post_a_like['meta']['code'] == 200:
         print 'success'
     else:
         print 'code 200 error'


like_a_post();


def comment_a_post(): #comment on a user's post
    like_post_url = (base_url + 'media/1569664842759368126_5793537413/comments')
    payload = {"access_token": app_access_token , "text": 'nice pic'}
    print 'POST request url : %s' % (like_post_url)
    post_a_comment = requests.post(like_post_url, payload).json()
    if post_a_comment['meta']['code'] == 200:
        print 'commented'
    else:
        print 'code 200 error'


comment_a_post();





