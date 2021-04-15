#allow a player to enter their details. authenticate these details to ensure they are an authorised player
user = [['user1', 'password1'],['user2', 'password2'],['user3', 'password3']] #array for the usernames and passwords
userEntry = ''
tries = 3 #user gets 3 tries to enter their username and password 
found = False #flag to determinte whether username/password is found


while userEntry == '' and tries > 0:
  userEntry = str(input('please enter your username: '))
  for item in range (0, len(user)):
    if userEntry == user[item][0]:
      print("welcome")
      foundName = True
      password = input("please enter your password: ")
      for j in passwords:
        if password == j:
          print("you're logged in")
          found = True
        else:
          print("incorrect password")
      break #Not sure about this - is it worth keeping? 
    else:
      print("go away")
      tries += 1

import random

from random import *

songs = open("songs","r")

songs_list = songs.read().splitlines()

songs.close()

# print(songs_list)

x = sample(songs_list, 1)
print (x[0])