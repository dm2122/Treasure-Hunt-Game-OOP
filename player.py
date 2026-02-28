import inquirer
import time

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

class Player:
  def __init__(self, name, location = "Home", inventory = None, health = 100, time_taken = 0):
    if inventory is None:
      inventory = []
    self.name = name
    self.location = location
    self.inventory = inventory
    self.health = health
    self.time_taken = time_taken

  def pick_up_item(self, item):
    if len(self.inventory) == 5:
      print("Your inventory is full.")
      print(f"This is your inventory: {self.inventory}")
      answer = input("Would you like to drop an item? (yes/no): ")
      if answer.upper() == "YES":
        item_drop = input("Which item would you like to drop? (enter the item you would like to drop exactly as it appears in your inventory): ")
        self.inventory.remove(item_drop)
        print(f"You have dropped {item_drop}.")
        print(f"This is your inventory now: {self.inventory}")
        self.inventory.append(item)
        print(f"You have picked up {item}.")
        print(f"This is your inventory now: {self.inventory}")
    else:
      self.inventory.append(item)
      print(f"You have picked up {item}.")
      print(f"This is your inventory now: {self.inventory}")

  def drop_item(self, item):
    self.inventory.remove(item)
    print(f"You have dropped {item}.")
    print(f"This is your inventory now: {self.inventory}")

  def travel(self, postman_pat, tilted_towers, central_line, east_acton_station, home, camden_town_station, bob_the_builder, burette, pipette, phenolphthalein, great_cambridge_roundabout, dog, captain_sebastian, professor):
    postman_pat.drive(self.location)
    destination = postman_pat.destination
    if self.location == "Home" and destination == "Tilted Towers": #time added
      self.time_taken += 0
      time.sleep(3)
      print("Entering the world of Fortnite...")
      time.sleep(3)
      tilted_towers.decrease_sweats(self)
      self.time_taken += tilted_towers.time_taken #adding together all the time taken...
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst) #add travel method at the end of each of these. 
    elif (self.location == "Epping Forest" and destination == "Home") or (self.location == "Epping Forest" and destination == "Tilted Towers"): #time added
      if destination == "Tilted Towers":
        self.time_taken += 10
        time.sleep(3)
        print("Entering the world of Fortnite...")
        time.sleep(3)
        tilted_towers.decrease_sweats(self)
        self.time_taken += tilted_towers.time_taken
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        self.time_taken += 10
        if len(self.inventory) > 0:
          answer = input("Would you like to leave an item at home? (yes/no): ")
          if answer.upper() == "YES":
            home.leave_item(self)
        if len(home.items_present) > 0:
          answer = input("Would you like to take an item from home? (yes/no): ")
          if answer.upper() == "YES":
            home.take_item(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Woodside High School" or self.location == "Great Cambridge Roundabout") and (destination == "Tilted Towers" or destination == "Home"): #time added
      if destination == "Tilted Towers":
        self.time_taken += 30
        time.sleep(3)
        print("Entering the world of Fortnite...")
        time.sleep(3)
        tilted_towers.decrease_sweats(self)
        self.time_taken += tilted_towers.time_taken
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        if len(self.inventory) > 0:
          answer = input("Would you like to leave an item at home? (yes/no): ")
          if answer.upper() == "YES":
            home.leave_item(self)
        if len(home.items_present) > 0:
          answer = input("Would you like to take an item from home? (yes/no): ")
          if answer.upper() == "YES":
            home.take_item(self)
        self.time_taken += 40
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Camden Town station" or self.location == "Heathrow airport" or self.location == "Construction site") and (destination == "Tilted Towers" or destination == "Home"): #time added
      if destination == "Tilted Towers":
        self.time_taken += 40
        time.sleep(3)
        print("Entering the world of Fortnite...")
        time.sleep(3)
        tilted_towers.decrease_sweats(self)
        self.time_taken += tilted_towers.time_taken
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        self.time_taken += 40
        if len(self.inventory) > 0:
          answer = input("Would you like to leave an item at home? (yes/no): ")
          if answer.upper() == "YES":
            home.leave_item(self)
        if len(home.items_present) > 0:
          answer = input("Would you like to take an item from home? (yes/no): ")
          if answer.upper() == "YES":
            home.take_item(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Home" or self.location == "Epping Forest" or self.location == "Heathrow airport") and (destination == "Camden Town station" or destination == "Construction site"): #time added
      self.time_taken += 40
      if destination == "Camden Town station":
        camden_town_station.reduce_crowd(self)
        self.time_taken += camden_town_station.time_taken
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        bob_the_builder.eat(self, lidl_inst)
        bob_the_builder.build()
        self.time_taken += bob_the_builder.time_taken
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif destination == "East Acton station": #continue time here...
      central_line.travel_to(postman_pat.destination, "East Acton")
      self.time_taken += central_line.time_taken
      east_acton_station.close_station(self, brad_inst)
      central_line.travel_to("East Acton", postman_pat.destination, )
      self.time_taken += central_line.time_taken
      postman_pat.drive(postman_pat.desination)
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Woodside High school" or self.location == "Great Cambridge roundabout") and (destination == "Camden Town station" or destination == "Construction site"):
      self.time_taken += 10
      if destination == "Camden Town station":
        camden_town_station.reduce_crowd(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        bob_the_builder.eat(self, lidl_inst)
        bob_the_builder.build()
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif destination in central_line.stations:
      print(postman_pat.destination) #testing this...
      central_line.travel_to(postman_pat.destination, "East Acton")
      self.time_taken += central_line.time_taken
      east_acton_station.close_station(self, brad_inst)
      central_line.travel_to("East Acton", postman_pat.destination, )
      self.time_taken += central_line.time_taken
      postman_pat.drive(postman_pat.destination)
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      
    elif (self.location == "Home" or self.location == "Epping Forest") and (destination == "Woodside High School" or destination == "Great Cambridge Roundabout"):
      self.time_taken += 30
      if destination == "Woodside High School":
        print("You are now at Woodside High School in the science department, in room B210")
        burette.measure_HCL()
        pipette.measure_NaOH()
        phenolphthalein.turn_colourless(pipette_inst)
        professor.give_detention(burette_inst, pipette_inst, phenolphthalein_inst)
        professor.give_rubidium(self, phenolphthalein_inst)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        great_cambridge_roundabout.reduce_traffic(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Camden Town station" or self.location == "Construction site") and (destination == "Woodside High School" or destination == "Great Cambridge Roundabout"):
      self.time_taken += 10
      if destination == "Woodside High School":
        print("You are now at Woodside High School in the science department, in room B210")
        burette.measure_HCL()
        pipette.measure_NaOH()
        phenolphthalein.turn_colourless(pipette_inst)
        professor.give_detention(burette_inst, pipette_inst, phenolphthalein_inst)
        professor.give_rubidium(self, phenolphthalein_inst)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        great_cambridge_roundabout.reduce_traffic(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Heathrow airport") and (destination == "Woodside High School" or destination == "Great Cambridge Roundabout"):
      self.time_taken += 40
      if destination == "Woodside High School":
        print("You are now at Woodside High School in the science department, in room B210")
        burette.measure_HCL()
        pipette.measure_NaOH()
        phenolphthalein.turn_colourless(pipette_inst)
        professor.give_detention(burette_inst, pipette_inst, phenolphthalein_inst)
        professor.give_rubidium(self, phenolphthalein_inst)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
      else:
        great_cambridge_roundabout.reduce_traffic(self)
        self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif self.location == "Home" and destination == "Epping Forest":
      self.time_taken += 10
      dog.find_dog(dial_inst)
      dog.find_dial(dial_inst, self)
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Great Cambridge roundabout" or self.location == "Woodside High School") and destination == "Epping Forest":
      self.time_taken += 30
      dog.find_dog(dial_inst)
      dog.find_dial(dial_inst, self)
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Camden Town station" or self.location == "Construction site") and destination == "Epping Forest":
      self.time_taken += 40
      dog.find_dog(dial_inst)
      dog.find_dial(dial_inst, self)
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif self.location == "Heathrow airport" and destination == "Epping Forest":
      self.time_taken += 50
      dog.find_dog()
      dog.find_dial()
      self.travel(pat_inst, tilted_inst, central_inst, east_acton_inst, home_inst, camden_inst, bob_inst, burette_inst, pipette_inst, phenolphthalein_inst, roundabout_inst, dog_inst, seb_inst, professor_inst)
    elif (self.location == "Home" or self.location == "Epping Forest") and destination == "Heathrow airport":
      self.time_taken += 50
      captain_sebastian.ask_help(b747_inst, yoke_inst, bob_inst, self)
      if captain_sebastian.stressed == False:
        bob_the_builder.fix_plane(b747_inst)
        #tbc when sebastian and 747 classes fully complete
    elif (self.location == "Woodside High school" or self.location == "Great Cambridge roundabout") and destination == "Heathrow airport":
      self.time_taken += 30
      captain_sebastian.ask_help(b747_inst, yoke_inst, bob_inst, self)
      if captain_sebastian.stressed == False:
        bob_the_builder.fix_plane(b747_inst)
        #tbc when sebastian and 747 classes fully complete
    elif (self.location == "Camden Town station" or self.location == "Construction site") and destination == "Heathrow airport":
      self.time_taken += 50
      captain_sebastian.ask_help(b747_inst, yoke_inst, bob_inst, self)
      if captain_sebastian.stressed == False:
        bob_the_builder.fix_plane(b747_inst)
        #tbc when sebastian and 747 classes fully complete