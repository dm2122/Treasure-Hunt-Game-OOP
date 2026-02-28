import time
import random
import inquirer

from player import Player


from place import Tilted_towers
from place import WHS
from place import Great_cambridge_roundabout
from place import Epping_forest
from place import Camden_town_station
from place import Home
from place import Construction_site
from place import Heathrow
from place import Lidl
from place import East_acton_station

from people import Professor
from people import Oliver
from people import Dog
from people import Crowd
from people import Sadiq_Khan
from people import Bob_the_builder
from people import Postman_pat
from people import Captain_Sebastian
from people import Brad_beans

from item import Reboot_card
from item import Rubidium
from item import Key
from item import B747
from item import bus_217
from item import Archimedes_dial
from item import Central_line
from item import Burette
from item import Pipette
from item import Phenolphthalein
from item import B747_yoke

#instances of places
tilted_inst = Tilted_towers()
whs_inst = WHS()
roundabout_inst = Great_cambridge_roundabout()
forest_inst = Epping_forest()
camden_inst = Camden_town_station()
home_inst = Home()
construction_inst = Construction_site()
heathrow_inst = Heathrow()
lidl_inst = Lidl()
east_acton_inst = East_acton_station()

#instances of people
professor_inst = Professor()
oliver_inst = Oliver()
dog_inst = Dog()
crowd_inst = Crowd()
khan_inst = Sadiq_Khan()
bob_inst = Bob_the_builder()
pat_inst = Postman_pat()
seb_inst = Captain_Sebastian()
brad_inst = Brad_beans()

#instances of items
reboot_inst = Reboot_card()
rubidium_inst = Rubidium()
key_inst = Key()
bus_inst = bus_217()
dial_inst = Archimedes_dial()
central_inst = Central_line()
burette_inst = Burette()
pipette_inst = Pipette()
phenolphthalein_inst = Phenolphthalein()
yoke_inst = B747_yoke()
b747_inst = B747()

#game starts:
print("Hello and welcome to this extremely fun Treasure Hunt game called 'Treasure Hunt game'.")
answer = input("Would you like to read through the instructions and general information about the game? (yes/no) (hint: you are advised to read through the instructions before playing the game for the first time):  ")
if answer.upper() == "YES":
  print("You have decided to read through the instructions and general information...")
  time.sleep(5)
  print("Even though this game is a 'treasure hunt' game, it is quite an untypical one, although it still incoporates the essential elements of such a game. There are features of this game which you will discover that make it unique, and one of the main features is that you need to watch the clock. Every significant action that you take in this game will take you a certain amount of in-game time, and your goal is to beat the game in as little in-game time as possible - this means you will need to be efficient and smart with what you do in this game.")
  answer = input("Enter any key to continue: ")
  if answer == ("fsafh"):
    time.sleep(1)
  else:
    time.sleep(1)
  print("Now for the more important points. When playing this game, you will see two types of statments displayed in the console. One type of statement will have a name followed by a colon. This is quite self explanatory - it means that the person whose name is written before the colon is saying something. The other type of statment will just be any other normal statement, such as this one that you are reading right now. These statements are just the narrator giving you information which you may find useful. Most of the statements you will see will be from the narrator (me)")
  answer = input("Enter any key to continue: ")
  if answer == ("fsafh"):
    time.sleep(1)
  else:
    time.sleep(1)
  print("Another thing you may want to be aware of is roughly where everything is. There are several places in this game, which you will need to move between. The map of the game is based on London, so if you don't know London too well, then you may have problems when it comes to saving time. You will be starting the game at HOME, which is as you may expect. Home is located near Cheshunt, so the closest place to your home is Epping Forest. You will be given a list of all places that you can go throughout the game, including at the start. The way you will get between all these places is by your close friend POSTMAN PAT, who has heard of your mission and is willing to help you. He will be with you pretty much everywhere (in his vehicle), including at the start of the game")
  answer = input("Enter any key to continue: ")
  if answer == ("fsafh"):
    time.sleep(1)
  else:
    time.sleep(1)
    print("At this point you may be wondering what the aim of the game is, and ironically enough, it is NOT to find treasure. You are not going to be told what the aim of the game is, but what you are allowed to know is that you need to get somewhere FAR AWAY which is generally NOT POSSIBLE. You will know that you are on track to reach the end of game once you are close. Another thing to keep in mind is that there is NO SINGLE way to win. This means that what you do throughout the entire game will affect how you can beat the game. You are encouraged to think OUTSIDE THE BOX. Do with all of that what you will...")
    answer = input("Enter any key to continue: ")
    if answer == ("fsafh"):
      time.sleep(1)
    else:
      time.sleep(1)
  print("Finally, I have made this game as stupid and annoying as possible, while also maintaining the essential elements of a 'treasure hunt' game which people wouldn't want to rage quite right away. Overall this is a fun and interesting game, so I hope you enjoy it.")
  time.sleep(10)
else:
  print("You have decided not to read through the instructions and general information")
  time.sleep(3)
print("You will be starting the game at HOME. Let's get started!")
name = input("Enter player name: ")
player_inst = Player(name)
player_inst.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)