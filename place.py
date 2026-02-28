import inquirer
import time

from people import Sadiq_Khan
class Tilted_towers: 
  def __init__(self, sweats_present = True):
    self.sweats_present = sweats_present
    
  def decrease_sweats(self, player):
    self.time_taken = 0
    leave = False
    print("Renegade Raider: Welcome to Tilted Towers, the home of Fortnite sweats. I have been expecting you, apparently you have to collect a reboot card, but that's all I have been told. The Reboot card is located right inside the clocktower, at the top. Looks like you're gonna have to build up to get there. Be careful though, as soon as the sweats hear you they will be after you.")
    time.sleep(10)
    answer = input("Renegade Raider: You seem like a new guy, so I should probably tell you about some of the controls. To build a wall, press Z. to build a floor, press X. To build stairs, press C. And to build a roof/cone, press V. You got that?(yes/no): ")
    if answer.upper() == "NO":
      print("Renegade Raider: That's fine, I will give you a few more seconds to learn the controls. Wall = Z, Floor = X, Stairs = C, Roof/Cone = V.")
      time.sleep(10)
    else:
      time.sleep(3)
    print("Renegade Raider: Great, now go out there and get that reboot card! Good luck!")
    time.sleep(3)
    print("You are currently walking down the stairs of an apartment block. This building is safe as Renegade Raider 'cleaned house' earlier")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("You are now at the bottom of the building about to leave through the doors inside of you. You cannot see or hear anyone, but you know there are definitely some sweats lurking around. Getting across Tilted Towers is no east task, you must have a plan, and it's exactly time to do that. How will you get to the clocktower (which is two buildings and an open space away) while staying as safe as possible...")
    time.sleep(5)
    action = inquirer.prompt([
       inquirer.List('action',
         message = "Which of the following will you do",
         choices = ["Just run", "Use the shockwave grenade which is in front of you on the floor"]),])
    method = action["action"]
    if method == "Just run":
      self.time_taken += 2
      print("You decided to run...")
      time.sleep(2)
      print("You are now running across Tilted, and you see in the corner of your eye a player with a sniper rifle, aiming right at you...")
      time.sleep(5)
      start_time = time.time()
      jump = input("QUICK, enter A to jump!: ")
      end_time = time.time()
      time_elapsed = end_time - start_time
      if jump.upper() == "A" and time_elapsed < 3:
        print("You jumped in time and avoided getting sniped")
        time.sleep(3)
        print("Continue your run and go inside the bottom floor of the clocktower through the door...")
        time.sleep(3)
      elif jump.upper() == "A" and time_elapsed > 3:
        print("You jumped too late and got shot by the sniper, but you are still alive. You will need to hide inside the clocktower at the bottom and use the shield potion which is there. It will take you 10 minutes...")
        time.sleep(5)
        print("...you are healing up fully...")
        time.sleep(3)
        self.time_taken += 10
      elif jump.upper() != "A" and time_elapsed < 3:
        print("You were quick but entered the wrong key. Because of this, you didn't jump and got hit by the sniper, although you are still alive. You will need to hide inside the clocktower at the bottom and use the shield potion which is there. It will take you 10 minutes...")
        time.sleep(5)
        print("...you are healing up fully...")
        time.sleep(3)
        self.time_taken += 10
      else:
        print("You pressed the wrong key and still did it too slow, so you get headshoted by the sniper, but you are somehow alive. You will need to hide inside the clocktower at the bottom and use the shield potion which is there. It will not heal you up fully, but it's always something. It will take you 10 minutes...")
        time.sleep(7)
        print("...you are healing up partially...")
        time.sleep(3)
        self.time_taken += 10
      print("You are now safe at the bottom of the clocktower healed up either fully or partially")
      time.sleep(3)
    if method == "Use the shockwave grenade which is in front of you on the floor":
      self.time_taken += 4
      health = 200
      print("You decided to use shockwave grenades...")
      time.sleep(2)
      print("You have just dropped a shockwave grenade at your feet and have been launched upwards and fornwrds, crashing through multiple buuldings...")
      time.sleep(3)
      print("Because of this, all the sweats in Tilted towers are now aware of you")
      time.sleep(3)
      print("Now that you have landed on the ground right in front of the clocktower, you can go and retreive...")
      time.sleep(3)
      print("Oh no, one of the Fortnite sweats has noticed where you are and are now after you; they are running towards you...and now they are building. You need to get ready for this fight...")
      time.sleep(5)
      print("On top of the 4 different structures you need to know the controls for (Wall = Z, Floor = X, Ceiling = C, Roof/Cone = V), you also need to know how to shoot-to shoot press S,to jump-to jump press A, and to edit your built-to edit press G (the rest of the editing will be done for you)")
      time.sleep(10)
      print("Time is currently frozen, so you have as much time as possible to get used to these controls. Whenever you are ready, answer 'yes' to the question that will follow...")
      time.sleep(3)
      answer_ready = input("Are you ready? (yes/no): ")
      while answer_ready.upper() != "YES":
        answer_ready = input("Are you ready? (yes/no): ")
      print("Now that you are ready, let's unfeeze time...")
      time.sleep(2)
      start_time = time.time()
      build_wall = input("The enemy is 5 metres ahead of you, QUICK build a wall now to block his incoming shot: ")
      end_time = time.time()
      time_elapsed = end_time - start_time
      if build_wall.upper() == "Z" and time_elapsed < 5:
        print("Great, you have correctly built a wall quick enough to block the enemy's incoming shot")
      elif build_wall.upper() != "Z" and time_elapsed < 5:
        print("You have not built a wall correctly, but since you were quick with what you did, you managed to block some of the shells from the enemy's shotgun and you have lost 50 hp")
        health = health - 50
      elif build_wall.upper() == "Z" and time_elapsed >= 5:
        print("You have built a wall correctly, but you were too slow and the enemy managed to land some damage on you. You have lost 50 hp")
        health = health - 50
      else:
        print("You have not built a wall correctly, and you were too slow with whatever you did, so the enemy managed to headshot you. You have lost 100 hp")
        health = health - 100
      time.sleep(5)
      print("...")
      time.sleep(5)
      print("You may have survived the enemy's shot, but they are still after you. To protect yourself from all slides, build 4 walls and a roof/cone (in that order) to surround yourself in build...")
      time.sleep(5)
      start_time = time.time()
      build_hut = input("Do that now: ")
      end_time = time.time()
      time_elapsed = end_time - start_time
      if build_hut.upper() == "ZZZZV" and time_elapsed < 6:
        print("You have successully 'boxed' yourself and thus blocked any shots")
      elif build_hut.upper() != "ZZZZV" and time_elapsed < 6:
        print("You have not 'boxed' yourself correctly, but whatever you did was quick, so the enemy shoot at you properly and you only lost 50 hp")
        health = health - 50
      elif build_hut.upper() == "ZZZZV" and time_elapsed > 6:
        print("You have 'boxed' yourself correctly, but you were too slow and the enemy managed to land a half-decent shot on you. You have lost 50 hp")
        health = health - 50
      else:
        print("You have not built a wall correctly, and you were too slow with whatever you did, so the enemy managed to headshot you. You have lost 100 hp")
        health = health - 100
      time.sleep(5)
      print("...")
      time.sleep(5)
      if health == 150:
        print("You are at 150 hp, so you are doing quite well")
      elif health == 200:
        print("You are at 200 hp, so you are doing very well")
      elif health == 100:
        print("You are at 100 hp, so you are doing alright")
      elif health == 50:
        print("You are at 50 hp, so you are not doing soi well - you need to be very careful now")
      else:
        print("You are at 0 hp, so you have been eliminated by the enemy. Therefore you have failed the mission and will be sent back to the real world...")
        leave = True
        #player will leave tilted towers
      time.sleep(5)
      print("The enemy is no trying to break through one of your walls. This is a perfect opportunity to finally eliminate them. You should edit the wall in front of you to make a window (by pressing the required key), and then shoot the player...")
      time.sleep(10)
      start_time = time.time()
      edit_kill_enemy = input("Do that now: ")
      end_time = time.time()
      time_elapsed = end_time - start_time
      if edit_kill_enemy.upper() == "GS" and time_elapsed < 4:
        print("Well done, you have successfully eliminated the player, and you did it quick enough to avoid you getting shot at by the enemy.")
      elif edit_kill_enemy.upper() == "GS" and time_elapsed > 4:
        print("You have killed the eliminated the player, but they still managed to get a shot on you. You have lost 50hp")
        health = health - 50
      elif edit_kill_enemy.upper() != "GS" and time_elapsed < 4:
        print("You have not edited the wall correctly, but you were fast and managed to disorientate the player, so you landed a shot on them and they are now eliminated, but you have lost 50 hp")
        health = health - 50
      else:
        print("You did not execute the manouvre correctly and whatever you did was too slow, so the enemy managed to headshot you. Luckily, Renegade Raider was watching and sniped the enemy, so they are eliminated, but you still lost 100 hp")
        health = health - 100
      time.sleep(5)
      print("...")
      time.sleep(5)
      if health == 150:
        print("You are at 150 hp, so you did quite well. You will need to go inside the clocktower and drink the shield potion that is there to heal up. This will take 5 minutes...")
        time.sleep(6)
        print("...healing up...")
        time.sleep(3)
        self.time_taken += 5
        leave = False
      elif health == 200:
        print("You are at 200 hp, so you did very well. You do not need to heal up")
        leave = False
      elif health == 100:
        print("You are at 100 hp, so you did alright. You will need to go inside the clocktower and drink the 2 shield potions that are there to heal up. This will take 10 minutes...")
        time.sleep(6)
        print("...healing up...")
        time.sleep(3)
        self.time_taken += 10
        leave = False
      elif health == 50:
        print("You are at 50 hp, so you didn't do so well, but you are stil alive. You will need to go inside the clocktower and use the med-kit and drink 2 shield potions that are there to heal up. This will take 15 minutes...")
        time.sleep(8)
        print("...healing up...")
        time.sleep(3)
        self.time_taken += 15
        leave = False
      else:
        print("You are at 0 hp, so you have been eliminated by the enemy. Therefore you have failed the mission and will be sent back to the real world...")
        leave = True
        #player will leave tilted towers
    time.sleep(5)              
    print("Since you are at the bottom of the clocktower and the reboot card is at the top of the tower, you will have to build up to the top...")
    time.sleep(4)
    build_stairs = input("You can do this by building 5 sets of stairs. Do that now here: ")
    while build_stairs.upper() != "CCCCC":
      build_stairs = input("You have not built the stairs correctly. Try again: ")
    print("Well done, you are now at the top of the tower, and the reboot card is right in front of you")
    reboot_pick_up = input("Press E to pick it up: ")
    while reboot_pick_up.upper() != "E":
      reboot_pick_up = input("Incorrect input. Try again")
    print("You have picked up the reboot card, but you still do not know who it belongs to??? Head over to the reboot van and reboot whoever this person is...")
    time.sleep(5)
    print("-Oh wait, Renegade Raider is rebooting the person already. Seems like whenever you pick up a reboot card, other people in your team also take possession of it. I wonder who this person is...")
    time.sleep(5)
    print("10 seconds later...")
    time.sleep(5)
    print("Beep Beep (sound of someone getting rebooted)")
    time.sleep(2)
    print("You look up into the sky and see a blue character gliding down from the sky straight into the middle of Tilted towers. As they get lower and lower, you realise that it is...")
    time.sleep(8)
    ("Ninja!!!")
    print("You see Ninja immediately land at the top of a building and grab some loot, before going out and eliminating all the sweats...")
    time.sleep(5)
    print("All you hear is gunfire and occasianally Ninja shouting out phrases like 'Get off me! You're on me get off me!' and ' Back to the lobby you go'")
    time.sleep(5)
    print("Having eliminated all the sweats, he grapples over to you at the top of the clocktower and proceeds to say something to you...")
    time.sleep(5)
    print(f"Ninja: Hello {player.name} and thanks for helping reboot me. As a sign of gratitude, I have cleared out all the sweats in Tilted Towers. Additionally, any time you need my help, wherever you are, just shout 'Get off me' and I'll come to you. Cya!")
    time.sleep(10)
    print("Now that Ninja is rebooted and there are no more sweats left in Tilted Towers, your mission here is complete...")
    time.sleep(3)
    if leave == True:
      self.sweats_present = True
    if leave == False:
      self.sweats_present = False
    print("Returning to the real world...")
    time.sleep(3)
    player.location = "Home"
    print("You have returned home")
    #player goes back to irl...
    
    
        
class WHS: #just need to add to Professor class
  def __init__(self, chaos = True):
    self.chaos = chaos

  def get_good(self):
    chaos = False
    return chaos

class Great_cambridge_roundabout: #complete, just need to test
  def __init__(self, traffic = True):
    self.traffic = traffic

  def reduce_traffic(self, player):
    self.time_taken = 3
    if self.traffic == True:
      print("You are now next to the Great Cambridge roundabout, and you see a huge amount of traffic ahead of you, amongst which is a 217 bus, which is carrying Oliver inside...")
      time.sleep(7)
      print("You need Oliver to get to his house, so he can retrieve a secret item and give it to you. But at this rate, Oliver won't get there anytime soon due to the traffic. Your task is to figure out a way of reducing this traffic...")
      time.sleep(10)
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Here is a list of possible options. Pick whichever one you think will work best:",
           choices = ["-With the help of police enforcement, divert all traffic only along the A10 (217 route)", "-Just wait it out and do nothing", "Encourage drivers to be calm and not cut in with their vehicles"]),])
      solution = action["action"]
      if solution == "-With the help of police enforcement, divert all traffic only along the A10 (217 route)":
        print("You have decided to divert all traffic along the A10, in effect closing the other roads connecting to the roundabout. This is a brilliant solution: the 217 will be on its way towards Waltham Cross quite quickly, however we will need to wait approximately 10 minutes for police enforcement to arrive...")
        time.sleep(10)
        print("Waiting for police to arrive at Great Cambridge roundabout...")
        time.sleep(3)
        print("10 minutes later...")
        time.sleep(3)
        self.time_taken += 10
        print("Great, the police has arrived and the traffic along the 217 route at this roundabout should begin to ease soon...")
        time.sleep(5)
        self.time_taken += 5
        print("After only 5 minutes, the 217 has passed the roundabout and is now heading towards Waltham Cross. There is no significant traffic on the rest of the route, so the journey for Oliver to his house should be quick. You will have to wait here until Oliver comes back...")
        time.sleep(10)
        print("Waiting for Oliver...")
        time.sleep(3)
        self.time_taken += 40
        print("After only 40 minutes, Oliver has arrived back to you with the mystery item. You took a closer look and realise that it is a key, attached to which is a tag. The tag is very worn out and the only letters you can make out (from left to right) and 'E', 's', 'A', 'c', 'o'.")
        time.sleep(2)
        ans = input("Do you want to pick it up? (yes/no): ")
        if ans.upper() == "YES":
          player.pick_up_item("key")
        else:
          print(f"You have decided to not pick up the key. You have just wasted {self.time_taken} minutes")
        self.traffic = False
      elif solution == "-Just wait it out and do nothing":
        print("Eventually the traffic will ease, but not soon enough, and Oliver will not get to his house in time. You have failed the task...")
        self.traffic = True
      else:
        print("You have decided to encourage drivers to be calm so they do not cut in, preventing unnecessary chaos and traffic. This solution should work, but it may still take a while to see the effects of it...")
        time.sleep(10)
        print("You are enncouraging drivers to remain calm...")
        time.sleep(3)
        print("10 minutes later...")
        time.sleep(3)
        self.time_taken += 10
        print("Great, now that you have done that, we just need to wait and hope that it did something...")
        time.sleep(5)
        self.time_taken += 15
        print("After 15 minutes, the 217 has passed the roundabout and is now heading towards Waltham Cross. There is no significant traffic on the rest of the route, so the journey for Oliver to his house should be quick. You will have to wait here until Oliver comes back...")
        time.sleep(10)
        print("Waiting for Oliver...")
        time.sleep(3)
        self.time_taken += 40
        print("After only 40 minutes, Oliver has arrived back to you with the mystery item. You took a closer look and realise that it is a key, attached to which is a tag. The tag is very worn out and the only letters you can make out (from left to right) and 'E', 's', 'A', 'c', 'o'.")
        time.sleep(2)
        ans = input("Do you want to pick it up? (yes/no): ")
        if ans.upper() == "YES":
          player.pick_up_item("key")
        else:
          print(f"You have decided to not pick up the key. You have just wasted {self.time_taken} minutes")
        self.traffic = False
    
class Epping_forest: #not used yet
  def __init__(self, foggy = True):
    self.foggy = foggy

  def reduce_fog(self):
    foggy = False
    return foggy

class Camden_town_station: #complete
  def __init__(self, overcrowded = True):
    self.overcrowded = overcrowded

  def reduce_crowd(self, player):
    self.time_taken = 10
    if self.overcrowded == True:
      print(f"Sadiq Khan: Finally some help, thank you for coming {player.name}. This is a big problem we have here in Camden Town Station. For many years now, this station has suffered from immense levels of overcrowding, but today especially it is really bad. I feel it is time to resolve this once and for all...")
      time.sleep(10)
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Do you have any ideas?",
           choices = ["Close the station forever", "Create multiple station exits (long term)", "Encourage passengers to use Kentish Town station instead", "Don't do anything"]),])
      idea = action["action"]
      if idea == "Close the station forever":
        print("Sadiq Khan: Well, I'm afraid that's not a good idea. Closing the station down for good would obviously get rid of overcrowding here, but it would put strain on surrounding stations such as Kentish town. Also, Camden Town station is incredibly important as it connects all 4 branches of the Northern line. Not gonna lie, I am slightly dissapointed with you - I was expecting better...")
        time.sleep(10)
        print("The Mayor of London has rejected your idea, and since you were of no help, he will not reward you. You have wasted your time...")
        time.sleep(3)
        self.overcrowded = True
        self.voucher = 0
      elif idea == "Create multiple station exits (long term)":
        print("Sadiq Khan: Hmm you know what, that is quite a good idea. It will unfortunately take a long time, but once it is executed it will reduce the crowd levels at this station to a reasonable level. Although I would have preferred a solution that we can use now, I highly appreciate your help. Therefore, I will give you this mystery item, but don't open it too quick, it will activiate itself when it's time...")
        player.pick_up_item("mystery item beta")
        time.sleep(12)
        self.overcrowded = True
      elif idea == "Encourage passengers to use Kentish Town station instead":
        print("Sadiq Khan: Wow, that is an amazing idea! It is something that we can do right now and it will definitely work. Thank you so much for your help. As a sign of appreciation, I will give you this mystery item, but don't open it too quick, it will activiate itself when it's time...")
        player.pick_up_item("mystery item alpha")
        time.sleep(10)
        self.overcrowded = False
      else:
        print("Sadiq Khan: Oh wow, so you are just gonna ditch me. Fine, just go away, and never talk to me again")
        time.sleep(4)
        self.overcrowded = True
  
class Home:
  def __init__(self, items_present = []):
    self.items_present = items_present

  def leave_item(self, player):
    action = inquirer.prompt([
       inquirer.List('action',
         message = "select an item to drop",
         choices = player.inventory),])
    item = action["action"]
    self.items_present.append(item)
    player.drop_item(item)

  def take_item(self, item, player):
    action = inquirer.prompt([
       inquirer.List('action',
         message = "select an item to drop",
         choices = player.inventory),])
    item = action["action"]
    self.items_present.remove(item)
    player.pick_up_item(item)

class Construction_site: #probs won't use
  def __init__(self, building_constructed = False):
    self.building_constructed = building_constructed

  def build(self):
    self.building_constructed = True
    return self.building_constructed

class Heathrow:
  def __init__(self, runway_cleared = False):
    self.runway_cleared = runway_cleared

  def clear_runway(self):
    self.runway_cleared = True
    return self.runway_cleared

class Lidl:
  def __init__(self, available_food = ["Croissant", "Nutella rip-off", "orange juice", "cast iron pan", "Strawberries"]):
      self.available_food = available_food

  def take_item(self):
     action = inquirer.prompt([
       inquirer.List('action',
         message = "select an item",
         choices = self.available_food),])
     self.item_selected = action["action"]
     self.available_food.remove(self.item_selected)
     return self.available_food

class East_acton_station:
  def __init__(self, open = True):
    self.open = open

  def close_station(self, player, brad_beans):
    self.time_taken = 5
    if self.open == True:
      print("You are know at the entrance of East Acton Station, and you can see the gate which you need to close. Seems like you need a key to close it")
      time.sleep(5)
      if "key" in player.inventory:
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Do you have a key?",
             choices = ["Yes", "No"]),])
        option = action["action"]
      else:
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Do you have a key?",
             choices = ["No"]),])
        option = action["action"]
      if option == "No":
        print("Oh no, you won't be able to close the station without a key. You're gonna have to abandon mission, unless you can find a key")
      else:
        print("Great, let's use that key to get this station closed")
        time.sleep(3)
        print("You are closing the station down...")
        time.sleep(3)
        print("You have now shut the gates to the station, therefore closing it. Guess it's time to -")
        brad_beans.wake_up()
        self.open = False #will be used later (boss fight)
      time.sleep(5)
      if "key" in player.inventory:
        print("It is now time to go back on the central line to go to Postman Pat (Even though you have closed the station down, you can still use the trains running through it)...")
      else:
        print("It is now time to go back on the central line to go to Postman Pat...")
      time.sleep(5)