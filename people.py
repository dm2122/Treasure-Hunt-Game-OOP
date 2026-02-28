import random
import time
import inquirer

import player

class Professor: #complete but needs testing
  def __init__(self, happy = False):
    self.happy = happy

  def give_detention(self, burette, pipette, phenolpthalein):
    if phenolpthalein.colour == "colourless":
      if burette.questions_wrong + pipette.questions_wrong + phenolpthalein.questions_wrong < 3:
        give_detention = False
      else:
        give_detention = True
        print("Professor: Although I am glad you managed to complete the practical, you got too many questions wrong. As a consequence, I am givin you a C4 (45 minute detention)...")
        time.sleep(5)
        print("You are currently sitting in a 45 minute detention...")
        time.sleep(5)
        print("You have now finished the detention")

  def give_rubidium(self, player, phenolphthalein):
    if phenolphthalein.colour == "colourless":
      print("Professor: Because you have completed the practical, I will gift you this small piece of rubidium. Be careful with it though, as you may remember from my lessons, rubidium is right at the bottom of group one, meaning that it reacts strongly with water, since it's outermost electron is very far from the oppositely charged nucleus, so the electron can be easily lost...")
      player.pick_up_item("rubidium")
      self.happy = True

class Oliver: #won't use this
  def __init__(self, at_home = False):
    self.at_home = at_home

class Dog:
  def __init__(self, found = False):
    self.found = found

  def find_dog(self, archimedes_dial): #complete
    if archimedes_dial.collected == False:
      print("You are now in Epping Forest, but you don't know where exactly. All you know is that there is a lost dog which you need to find, and that is exactly your task. The issue is that this is quite a big forest, and on top of that it is foggy, so it's not an easy task...")
      time.sleep(10)
      action = inquirer.prompt([
         inquirer.List('action',
           message = "You have a few options, pick one",
           choices = ["-Walk around the forest in a circle (will take longer but more systematic)", "-Walk around the forest randomly (not very systematic and higher chance of losing track of where you have been) "]),])
      option = action["action"]
      if option == "-Walk around the forest in a circle (will take longer but more systematic)":
        self.time_taken = 29
        self.found = True
        print("It took you 29 minutes of walking around the forest in a circle to find the dog")
      else:
        self.time_taken = 0
        self.found = False
        while self.found == False:
          self.time_taken += 5
          time.sleep(3)
          print("5 minutes later...")
          time.sleep(3)
          found = int(random.choice([1, 0, 0, 0]))
          if found == 1:
            self.found = True #will be used later (boss fight)
            print(f"You have found the dog after {self.time_taken} minutes")
          else:
            self.found = False
            print("You have not found the dog yet, keep looking...")
      time.sleep(3)
      print("You look at the dog's collar and see that it says 'Twado' on it")
      time.sleep(2)
      print("Twado the dog is now part of your team and your task is complete...")

  def find_dial(self, archimedes_dial, player):
    if archimedes_dial.collected == False:
      print("Twado the dog starts sniffing around the forest, and barks at you as a sign to tell you to follow him")
      time.sleep(3)
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Do you want to follow him?",
           choices = ["Yes", "No"]),])
      option = action["action"]
      if option == "No":
        print("You decide not to follow Twado the dog, so you leave the forest on your own...")
        archimedes_dial.collected = False
        self.time_taken += 3
      else:
        self.time_taken += 3
        print("You have decided to follow Twado...")
        time.sleep(3)
        print("Following Twado the dog...")
        time.sleep(3)
        print("After 5 minutes, the dog leads you to a suspicious  patch of mud, and signals to you that there is something there")
        self.time_taken += 5
        time.sleep(5)
        print("So you begin to dig into the dirt, with the help of the dog")
        time.sleep(3)
        print("3 minutes later, you discover a round, gold disk-like item. You take it out, remove the remaining dirt and realise that it is Archimides' Dial!")
        self.time_taken += 3
        archimedes_dial.collect(player)
      time.sleep(5)
    #go to next place
      

class Crowd: #Just need to add this to Camden Town class
  def __init__(self, crowded = True):
    self.crowded = crowded

  def disperse(self):
    self.crowded = False
    return self.crowded

class Sadiq_Khan: #complete in Camden Town class
  def __init__(self, happy = False):
    self.happy = happy

  def be_happy(self):
    self.happy = True

class Bob_the_builder: #complete just need to test
  def __init__(self, happy = False, tired = True, building_constructed = False):
    self.happy = happy
    self.tired = tired
    self.building_constructed = building_constructed

  def eat(self, player, lidl):
    if self.tired == True:
      self.time_taken = 0
      print("You are now at the construction site located by London Fields.")
      time.sleep(7)
      print(f"Bob: Hello {player.name}, I am Bob the Builder, and I need to get this thing built, but I am too tired from all the work so far and need something to eat")
      time.sleep(5)
      action = inquirer.prompt([
         inquirer.List('action',
           message = "You reckon you could get me something to eat?",
           choices = ["Yes", "No"]),])
      option = action["action"]
      if option == "No":
        print("Bob: Oh well, I guess I'll have to ask someone else, or just not finish this building at all")
        self.time_taken += 3
        self.happy = False
        self.tired = True
      else:
        print("Bob: Great! I think there is a Lidl about 10 minutes away from here, so that's probably your best bet. Ideally I would like something which would give me a lot of energy; something high in carbs...") #options: croissant, nutella, juice, pan, strawberries
        time.sleep(7)
        print("You are know walking to Lidl...")
        time.sleep(3)
        print("After 10 minutes you have arrived at Lidl. Now it's time to get in there and pick the ideal food option for Bob")
        print("It's quite a small Lidl, so there isn't much to choose from...")
        lidl.take_item()
        print(f"You have selected {lidl.item_selected}. We'll see if Bob the Builder is happy with this...") 
        time.sleep(5)
        print("You are now walking back to the construction site...")
        self.time_taken += 25
        print("Bob: Hello again, let's see what you have gotten me...")
        if lidl.item_selected == "Croissant" or "Nutella":
          print("Bob: Oh wow, that is an amzing choice! This item is not only full of carbohydrates but it is also absolutely delicious! I will eat this real quick and should get back to work in around 15 minutes once the sugar kicks in...")
          time.sleep(10)
          print("You are waiting for the sugar to kick in...")
          time.sleep(3)
          print("15 minutes later")
          time.sleep(1)
          print("Bob: I feel great now and will get on with finishing this build off!")
          self.time_taken += 15
          self.happy = True
          self.tired = False
        elif lidl.item_selected == "Juice" or "Strawberries":
          print("Bob: Hmm, this isn't quite the best choice as fruits do not have much carbohydrates in them, but I appreciate your help nonetheless. I would feel bad if you had to go all the way back to Lidl to buy me something else, so I will consume this product, and go to Lidl myself once I feel like it...")
          time.sleep(12)
          print("You are waiting for the above to happen...")
          time.sleep(3)
          print("40 minutes later")
          print("Bob: I just bought myself a croissant and ate it on the way here, so the sugar has kicked in and I am ready to get on with the build!")
          self.time_taken += 40
          self.happy = True
          self.tired = False
        else:
          print("Bob: Are you an idiot? I asked for something to eat, and you got me a pan?? What the heck do you want me to do with that?")
          time.sleep(3)
          action = inquirer.prompt([
             inquirer.List('action',
               message = f"You better explain yourself {player.name}",
               choices = ["I don't know", "I wanted you to cook something using this pan", "I thought you would enjoy eating this pan", "I wanted to annoy you"]),])
          option = action["action"]
          if option == "I wanted you to cook something using this pan":
            print("Bob: Hmm, I guess that's not a bad reason. You know what, I won't let this be the reason we fall out, but I am gonna have to go to Lidl myself and get something to eat...")
            time.sleep(12)
            print("You are waiting for the above to happen...")
            time.sleep(3)
            print("40 minutes later")
            print("Bob: I just bought myself a croissant and ate it on the way here, so the sugar has kicked in and I am ready to get on with the build!")
            self.time_taken += 42
            self.happy = True
            self.tired = False
          else:
            print("Bob: Brilliant, I don't even want to look at you anymore. Just go away; disappear from my sight")
            time.sleep(3)
            print("Bob is not happy with you, and he is still tired, so you will not be able to use his help.")
            self.time_taken += 17
            self.happy = False
            self.tired = True
    #travel to next place
        

  def build(self):
    if self.happy == True and self.tired == False:
      time.sleep(5)
      print("...building in progress...")
      time.sleep(5)
      self.building_constructed = True #this will be used later
      self.time_taken += 60
      print("An hour later, Bob has finished building")
      time.sleep(2)
      print("Bob: Finally, this masterpiece is complete, and it would not have been possible without you. Since my work here is done and I am grateful for your help, I am now at your disposoal! If you ever need me, just sing 'Bob the builder, can we fix it' and I will get to you as soon as possible")

  def fix_plane(self, b747): 
    self.time_taken = 0
    print("You sing the lyrics 'Bob the builder, can we fix it, bob the builder, yes we can!' to signal to Bob that you need his help...")
    time.sleep(5)
    print("You are waiting for Bob the Builder to arrive")
    time.sleep(5)
    self.time_taken += 20
    print("After only 20 minutes, Bob has arrived")
    time.sleep(2)
    print("Bob the Builder: Already need my help eh? No worries, what do you need help with")
    time.sleep(3)
    print("Sebastian: We need to fix up the cockpit inside the plane: I just need to get the yoke inserted back")
    time.sleep(3)
    print("Bob: Ok, shouldn't be too big of a problem. Let's get over to the plane then shall we...")
    time.sleep(3)
    print("You along with Captain Sebastian and Bob the Builder are walking over to the B747 plane...")
    time.sleep(3)
    self.time_taken += 5
    print("Now that you are all on board after 5 minutes, Bob attempts to insert the yoke where it belongs")
    time.sleep(2)
    print("Bob: Thankfully the yoke just has to be connected mechanically, I don't think this will take too long...")
    time.sleep(3)
    print("10 minutes later")
    time.sleep(3)
    print("Bob: Alright, should be all done now")
    time.sleep(1)
    print("You: Thanks a lot Bob")
    time.sleep(1)
    print("Bob: No problem, I'm gonna have to go now, but I'll see you around. See ya!")
    b747.ready = True
    
class Postman_pat: #complete just need to test and add to player class
  def __init__(self):
    nothing = True

  def drive(self, location):
    self.location = location
    self.time_taken = 0
    destination = inquirer.prompt([
      inquirer.List('destination',
        message = "select a destination",
        choices = ["Home", "Tilted Towers", "Epping Forest", "Great Cambridge Roundabout", "Woodside High School", "East Acton station", "Camden Town station", "Constrcution site", "Heathrow airport"]), ])
    self.destination = destination["destination"]
    if self.location == self.destination: #time not accounted for
      print("Pat: You are already here bro")
      self.drive(self.location)
    elif self.destination == "Tilted Towers":
      if self.location == "Home":
        print("Pat: You can go to Tilted Towers directly from here!")#player goes tilted
      else:
        print("Pat: Well I can't take you to Tilted Towers, but I can take you Home, and you can access Tilted Towers from there.")#player goes home then tilted
        time.sleep(5)
        print("Travelling Home...")
        time.sleep(3)
        print("After a certain while you have arrived Home")
    elif self.destination == "East Acton station": #time accounted for
      print("Pat: Oh no, sorry mate I can't take you to East Acton station, those endz scare me. I can take you to a different station on the central line, such as Liverpool Street, and you can then take the central line from there.")
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Pat: How does that sound?",
           choices = ["Yeah sure", "How about a different station?"]),])
      option = action["action"]
      if option == "Yeah sure":
        print("Pat: Okay then, let me drive you to Liverpool street station...")
        if self.location == "Construction site" or "Camden Town station":
          self.time_taken += 10
        elif self.location == "Epping Forest" or "Home" or "Heathrow airport":
          self.time_taken += 50
        else:
          self.time_taken += 30
        time.sleep(5)
        print(f"You have now arrived at Liverpool street station after {self.time_taken} minutes, and are about to board the central line...")
        time.sleep(5)
        self.destination = "Liverpool Street"
        self.location = "Liverpool Street station"
      else:
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Pat: That's fine, just choose a different station",
             choices = ["Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush"]),])
        option = action["action"]
        if self.location == "Construction site" or "Camden Town station":
          self.time_taken += 15
        elif self.location == "Epping Forest" or "Home" or "Heathrow airport":
          self.time_taken += 55
        else:
          self.time_taken += 35
        print(f"Pat: Okay then, let me drive you to {option}. I am not too familiar with the route, so it may take a while, maybe around {self.time_taken} minutes.")
        self.destination = option
        time.sleep(5)
        print(f"You have now arrived at {self.destination} station after {self.time_taken} minutes, and are about to board the central line...")
        time.sleep(5)
    elif self.location in ["Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton"]:
      print(f"Sure, I can get you to {self.destination}")#continue 
      if self.destination == "Construction site" or self.destination == "Camden Town station":
        self.time_taken += 15
      elif self.destination == "Epping Forest" or self.destination == "Home" or self.destination == "Heathrow airport":
        self.time_taken += 55
      else:
        self.time_taken += 35
      print(f"Pat: Okay then, let me drive you to {self.destination}. I am not too familiar with the route, so it may take a while, maybe around {self.time_taken} minutes.")
      self.location = self.destination + " station"
    else: #time not accounted for
      print(f"Pat: Sure thing, let me take you to {self.destination}")
      print(self.location)
      print(self.destination)
    

class Captain_Sebastian: #complete for now
  def __init__(self, stressed = True):
    self.stressed = stressed

  def ask_help(self, b747, b747_yoke, bob_the_builder, player):
    if b747.fixed == False:
      if b747_yoke.collected == False:
        self.time_taken = 0
        print("You are now at Heathrow airport terminal 5, and you see someone approaching you - they look quite stressed")
        time.sleep(5)
        print("Captain Sebastian: Hello, I am Captain Sebastian and thank you so much for coming, I have been told to expect you.")
        time.sleep(5)
        print("Sebastian: You see, I'm in a bit of a situation right now. I have to fly a Boeing 747 to JFK airport in New York, in about 2 hours.")
        time.sleep(5)
        print("Sebastian: The issue is that the plane is missing a yoke, that steering thing in the cockpit which is used to fly the aircraft, and I have no idea where it is.")
        time.sleep(6)
        print("Sebastian: How does this kind of thing even happen?")
        time.sleep(2)
        print("Sebastian: How will I even find the yoke?!")
        time.sleep(2)
        print("Sebastian: If I don't do this flight I will be fired as a Captain and actually as a pilot altogether, I won't be able to find a job, I will be homeless HELP!!!")
        time.sleep(7)
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Sebastian: Phew, okay sorry about that I got a bit carried away. All I'm really trying to say is are you willing to help me?",
             choices = ["Yes", "No"]),])
        option = action["action"]
        if option == "No":
          print("Sebastian: Oh, well I was not expecting that. Why did you come here then in the first place? Back to panicking for me I guess")
          self.stressed = True
          self.time_taken += 3
          #player leaves airport
        elif option == "Yes":
          print("Sebastian: I knew you would say yes. Well then, where do we even start. I guess we could ask as much staff as possible whether they have seen a yoke. Actually, we could try robbing a yoke - nah that's too risky. Hmm, ooh I've got a great idea - how about create a makeshift yoke and just use that instead. After all, these yokes work purely mechanicaly to control the plane.")
          time.sleep(15)
          print("Sebastian: Actually, on second thoughts, neither of us are likely to be specialised enough in this field to do that.")
          time.sleep(5)
          self.time_taken += 3
          action = inquirer.prompt([
             inquirer.List('action',
               message = "I have no idea. What do you think?",
               choices = ["Ask around heathrow to find the yoke", "Steal a yoke from a different aircraft", "Create a makeshift yoke"]),])
          option = action["action"]
          if option == "Ask around heathrow to find the yoke":
            print("Sebastian: That was my original idea, and it's the lowest effort one, so why not ask do this. I'll tell you what, I will stay here in terminal 5 and ask around, and then go to terminal 4 to do the same there. You could go to terminals 2 and 3 and search there. Sound good? Great, now let's crack on and find this yoke!")
            print("You will now get on the Piccadilly line to go to terminals 2 and 3...")
            time.sleep(5)
            print("After 5 minutes, you have arrived at terminal 2. Now it's time to look for this yoke")
            find_yoke_time = 0
            while b747_yoke.collected == False:
              time.sleep(3)
              find_yoke_time += 5
              b747_yoke.collected = random.choice([True, False, False, False, False, False])
              if b747_yoke.collected == True:
                print(f"After {find_yoke_time} minutes, you have found the yoke.")
                b747_yoke.collect(player) #player_inst = Player(...)
              else:
                print(f"After {find_yoke_time} minutes, you have not yet found the yoke.")
            self.time_taken += find_yoke_time
            print("Now that you have collected the yoke, you can go back to terminal 5 and let Captain Sebastian know...")
            time.sleep(5)
            self.time_taken += 5
            print("After 5 minutes you have arrived back at Heathrow T5, and you immediately spot Captian Sebastian")
            time.sleep(5)
            ("Sebastian: Oh my goodness, you actually managed to find the yoke, well I don't know if it's the exact one, but either way it should hopefully work.")
            time.sleep(5)
          elif option == "Steal a yoke from a different aircraft":
            print("tbc") #tbc
          else:
            print("tbc") #tbc
        #the above code is only executed if yoke is not found
        #the following code is only executed if plane is not fixed
        print("Sebastian: Well, I guess we should head to the plane and see if we can get this to work...")
        self.time_taken += 5
        time.sleep(5)
        print("walking to the aircraft")
        time.sleep(3)
        print("After 5 minutes, you and Captain Sebastian have made it onboard the 747")
        time.sleep(5)
        print("Sebastian: Hmm, to be honest I'm not sure if this is going to work; there is no way we will be able to insert this yoke correctly. I reckon we need a specialist to help us with this")
        time.sleep(5)
        if bob_the_builder.building_constructed == True:
          action = inquirer.prompt([
             inquirer.List('action',
               message = "Do you know someone who could help?",
               choices = ["Bob the Builder", "No"]),])
          option = action["action"]
          if option == "No":
            print("Sebastian: Aw man, that is unfortunate. Looks like this plane isn't going anywhere. However, if you could manage to find someoone to help with this, even if it woud take a few hours, I would highly appreciate it. We can always delay the flight if necessary...")
          else:
            print("Sebastian: Wowow, really? That is amazing. Well in that case, get this guy over here so he can fix the plane!")
            bob_the_builder.fix_plane(b747)
            b747.fixed = True
          self.stressed = False
          self.time_taken += 2
      
  def offer_free_flight(self):
    flight_destination = input("Choose any place an this planet: ")
    return flight_destination

class Brad_beans:
  def __init__(self, asleep = True):
    self.asleep = asleep

  def wake_up(self):
    print("Someone: AHH, who's that! What's happeninng why am I here, oh wait station I need to close it!")
    time.sleep(5)
    print("Someone: Oh hello there, who are you? It seems like you have closed the station down. That's my job, but I highly appreciate your services, as you can see I fell asleep...")
    time.sleep(5)
    print(f"You tell the person that your name is {player.name}.")
    time.sleep(3)
    print(f"Bradley: Ah yes hello {player.name}, my name is Detective Bradley Beans, but you can just call me Brads. Thanks a lot again for your help, without you I may have been fired by tomorrow! To say thank you, whenever you are in trouble where I could help, such as with a mystery, then I will sense that and get straight to you")
    time.sleep(8)
    print("Bradley: But for now, good luck with whatever and see you soon!")