#allow a player to enter their details. authenticate these details to ensure they are an authorised player
import random
from random import *

#Constant 
MENU_VALUES = ['S','A','Q']

def song():
  songs = open('songs','r')
  songs_list = songs.read().splitlines()
  songs.close()
  # print(songs_list)
  song = sample(songs_list, 1)
  print(song)

def menu():
  while True:
    print('''MENU;

    S. guese the song
    A. guese the artist
    Q. quit''')
    value = input('Pelse enter a value; ')
    if value in MENU_VALUES:
      if value == 'Q':
        print('ThankYou for playing')
        return 
      elif value == 'S':
        print('Guese the song: ')
        song()
      elif value == 'A':
        print('Guese the artist')
        song()
      else:
        

user = [['user1','password1'],['user2','password2'],['user3','password3']] #array for the usernames and passwords
userEntry = ''
tries = 3 #user gets 3 tries to enter their username and password 
foundName = False #flag to determinte whether username/password is found
authenticatedUser = False 



while userEntry == '' and tries > 0:
  userEntry = input('please enter your username: ')
  for item in user:
    if userEntry == item[0]:
      print('welcome')
      foundName = True
      passwordEntry = str(input('please enter your password: ')) 
      
      if passwordEntry == item[1]:  #this is pulling up an error 
          print('you are logged in')
          authenticatedUser = True 
      else:
        print('incorrect password')
        userEntry = ''
  if foundName == False:
    print('You are not authorised')
    tries -= 1
    userEntry = ''

if authenticatedUser == True:
  menu()

