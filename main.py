#allow a player to enter their details. authenticate these details to ensure they are an authorised player
user = [['user1','password1'],['user2','password2'],['user3','password3']] #array for the usernames and passwords
userEntry = ''
tries = 3 #user gets 3 tries to enter their username and password 
foundName = False #flag to determinte whether username/password is found


while userEntry == '' and tries > 0:
  userEntry = str(input('please enter your username: '))
  for item in range (0, len(user)):
    if userEntry == user[item][0]:
      print('welcome')
      foundName = True
      passwordEntry = str(input('please enter your password: ')) 
      
      if passwordEntry == user [item][1]:  #this is pulling up an error 
          print('you are logged in')
      else:
        print('incorrect password')
        userEntry = ''
    if foundName == False:
      print('go away')
      tries -= 1
      userEntry = ''
        
          
      






import random

from random import *

songs = open('songs','r')

songs_list = songs.read().splitlines()

songs.close()

# print(songs_list)

x = sample(songs_list, 1)
print (x[0])