import time
import inquirer

class Reboot_card: #did not use
  def __init__(self, collected = False):
    self.collected = collected

  def collect(self):
    self.collected = True

class Rubidium(Reboot_card): #to be used in boss fight

  def react(self, solution):
    if solution == "water":
      self.reaction = "violent"
      self.damage_dealt = 25
    else:
      self.reaction = "useless"
      self.damage_dealt = 0

class Key(Reboot_card):

  def use(self, station):
    station.ineract_station()

class bus_217: #did not use this
  def __init__(self, location = "Great Cambridge Roundabout"):
    self.location = location

  def drive(self):
    print("The 217 is now on its way towards Waltham Cross...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("The 217 is at Bush Hill Park")

class Archimedes_dial:
  def __init__(self, collected = False):
    self.collected = collected

  def collect(self, player):
    player.pick_up_item("Archimedes' Dial") #fixed?
    if "Archimedes' Dial" in player.inventory:
      self.collected = True
    else:
      self.collected = False

class Central_line:
  def __init__(self, stations = ["Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton"]):
    self.stations = stations

  def travel_to(self, current_station, destination):
    current_station_element_no = self.stations.index(current_station)
    destination_element_no = self.stations.index(destination)
    time_taken = abs(current_station_element_no - destination_element_no)
    self.time_taken = time_taken * 2
    print(f"Travelling from {current_station} to {destination}:")
    if current_station_element_no < destination_element_no:
      for i in range(current_station_element_no, destination_element_no):
        time.sleep(1)
        print("Passing " + self.stations[i])
      time.sleep(1)
      print(f"Arriving at {destination}")
    else:
      for i in range(current_station_element_no, destination_element_no, -1):
        time.sleep(1)
        print("Passing " + self.stations[i])
      time.sleep(1)
      print(f"Arriving at {destination}")
      

class Burette: #complete
  def __init__(self, HCL_measured = False):
    self.HCL_measured = HCL_measured

  def measure_HCL(self):
    self.kicked = False
    self.k = 1
    self.questions_wrong = 0
    self.time_taken = 3
    while self.kicked == False and self.k == 1:
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Professor: Which of the following pieces of equipment do we use to measure the acid?",
           choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
      equipment = action["action"]
      if equipment == "Burette":
        print("Professor: Yes, we use a Burette to measure the acid. Let's go ahead and do that. Remember to make sure the bottom of the meniscus is on the line.")
        self.HCL_measured = True
      elif equipment == "You don't measure and add it in excess":
        print("Professor: Hmm, I think your getting confused with a different practical. Remember that in a titraion we want to be as precise as possible. I think you should go read a chemistry textbook...")
        time.sleep(5)
        print("You are now reading a chemistry textbook to learn more abut titration. This will take you 10 minutes")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You now know that you have to use a Burette to measure the acid. Let's try measuring the Hydrochloric Acid again...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Professor: Hello again. Do you now know which of the following pieces of equipment we use to measure the acid?",
             choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
        equipment = action["action"]
        if equipment == "Burette":
          print("Professor: Yes that is correct. Let's go ahead and do that. Remember to make sure the bottom of the meniscus is on the line")
          self.HCL_measured = True
        else:
          print("Professor: You are just stupid. Get out of here.")
          self.kicked = True
          print("The Professor is very angry with you and doesn't want to carry on the practical with you, so you leave Woodside High School")
        #player kicked out from practical-complete
        #let player travel to new location
      else:
        print("Professor: That is not quite right. You should read a chemistry textbook to learn a bit more about titration...")
        time.sleep(5)
        print("You are now reading a chemistry textbook to learn more abut titration. This will take you 10 minutes")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You now know that you have to use a Burette to measure the acid. Let's try measuring the Hydrochloric Acid again...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Professor: Hello again. Do you now know which of the following pieces of equipment we use to measure the acid?",
             choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
        equipment = action["action"]
        if equipment == "Burette":
          print("Professor: Yes that is correct. Let's go ahead and do that. Remember to make sure the bottom of the meniscus is on the line")
          self.HCL_measured = True
        else:
          print("Professor: You are just stupid. Get out of here.")
          self.kicked = True
          print("The Professor is very angry with you and doesn't want to carry on the practical with you, so you leave Woodside High School")
          #player kicked out from practical-complete
          #let player travel to new location
        if self.HCL_measured == True:
          print("You are now measuring out the required volume of HCL")
          self.k += 1
    
class Pipette: #complete
  def __init__(self, NaOH_measured = False):
    self.NaOH_measured = NaOH_measured

  def measure_NaOH(self, burette):
    self.kicked = False
    self.k = 1
    self.time_taken = 3
    self.questions_wrong = 0
    while self.kicked == False and self.k == 1 and burette.kicked == False:
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Professor: We use a Burette to measure out the volume of HCL, but what apparatus do we use to measure out our base, in this case the Sodium Hydroxide?",
           choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
      equipment = action["action"]
      if equipment == "Burette":
        print("Professor: You think you are clever don't you. You are wrong, we do not use the same apparatus to measure out the base and acid. Have you learnt nothing from my lessons! Go and refresh your memory by reading through the slides...")
        time.sleep(5)
        print("You are now reading through the slides about titration to refresh your memory. This will take you 10 minutes")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You now know that you have to use a Pipette to measure out the base. Let's try measuring the Sodium Hydroxide...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Professor: I hope you now know what we use to measure out NaOH",
             choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
        equipment = action["action"]
        if equipment == "Pipette":
          print("Professor: Correct. Let's go ahead and do that. Remember to make sure the bottom of the meniscus is on the line")
          self.NaOH_measured = True
        else:
          print("Professor: I have never seen someone so imbecilic in my whole life. Go away")
          self.kicked = True
          print("The Professor is very angry with you and doesn't want to carry on the practical with you, so you leave Woodside High School")
          #player kicked out from practical-complete
          #let player travel to new location
      elif equipment != "Pipette":
        print("Professor: Incorrect. I thought my lessons would have taught your something. Go and refresh your memory by reading through the slides...")
        time.sleep(5)
        print("You are now reading through the slides about titration to refresh your memory. This will take you 10 minutes")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You now know that you have to use a Pipette to measure out the base. Let's try measuring the Sodium Hydroxide...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        action = inquirer.prompt([
           inquirer.List('action',
             message = "Professor: I hope you now know what we use to measure out NaOH",
             choices = ["Measuring cylinder", "Burette", "Toaster", "Pipette", "You don't measure and add it in excess"]),])
        equipment = action["action"]
        if equipment == "Pipette":
          print("Professor: Correct. Let's go ahead and do that. Remember to make sure the bottom of the meniscus is on the line")
          self.NaOH_measured = True
        else:
          print("Professor: I have never seen someone so imbecilic in my whole life. Go away")
          self.kicked = True
          print("The Professor is very angry with you and doesn't want to carry on the practical with you, so you leave Woodside High School")
          #player kicked out from practical-complete
          #let player travel to new location
      else:
        print("Professor: Yes well done, we use a Pipette to measure out the base. Remember the Pipette is that weird tube thing with a wheel at the top. Go ahead and measure out the required volume of NaOH, making sure the bottom of the meniscus is on the line.")
        self.NaOH_measured = True
      if self.NaOH_measured == True:
        print("You are now measuring out the required volume of NaOH...")
        time.sleep(3)
        self.k += 1

class Phenolphthalein: # complete
  def __init__(self, colour = "pink"):
    self.colour = colour

  def turn_colourless(self, pipette):
    self.k = 1
    self.time_taken = 3
    self.questions_wrong = 0
    while pipette.kicked == False and self.k == 1:
      action = inquirer.prompt([
         inquirer.List('action',
           message = "Professor: We are almost done, just one last thing; we will now pour the NaOH into a conical flask, add a few drops of our indicator (phenolphthalein) and add our HCL into the same conical flask drop by drop from the Burette. My quesion to you is: What colour will the solution turn once it is neutralised",
           choices = ["Colourless", "It will stay pink", "Brick red"]),])
      colour_answer = action["action"]
      if colour_answer == "Colourless":
        print("Professor: Well done, you are right. Remember to add HCL into the beaker drop by drop from the Burette, and keep swirling the conical flask until this colour change occurs...")
        time.sleep(3)
        print("You are carring out the titration...")
        time.sleep(3)
        print("The solution has turned colourless and you have closed off the bottom of the Burette. The practical is complete")
        self.colour = "colourless"
      elif colour_answer == "It will stay pink":
        print("Professor: You are clearly quite unintelligent. If the solution stayed the same colour then what would even be the point of adding the indicator? You better go and ask a teacher for help, because I can't be bothered with you anymore...")
        time.sleep(5)
        print("You are now looking for a teacher in the science department of Woodside High School to help you answer the Professor's question")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You found a teacher called Dr. Hasan, who told you that phenolphthalein turns colourless when in a neutral solution. Go back to the room B210 and let the Professor know that you have the answer...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        print("...")
        time.sleep(5)
        print("You are telling the Professor the answer...")
        print("Professor: Finally you got to the answer, let's go ahead and complete this practical. Remember to add HCL into the beaker drop by drop from the Burette, and keep swirling the conical flask until this colour change occurs...")
        time.sleep(3)
        print("You are carring out the titration...")
        time.sleep(3)
        print("The solution has turned colourless and you have closed off the bottom of the Burette. The practical is complete")
        self.colour = "colourless"
      else:
        print("Professor: That is not quite the right answer. You better go and ask a teacher for help, because clearly annything I tell you comes out one ear and out the other...")
        time.sleep(5)
        print("You are now looking for a teacher in the science department of Woodside High School to help you answer the Professor's question")
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("10 minutes later...")
        time.sleep(1)
        print("You found a teacher called Dr. Hasan, who told you that phenolphthalein turns colourless when in a neutral solution. Go back to the room B210 and let the Professor know that you have the answer...")
        time.sleep(3)
        self.time_taken += 10
        self.questions_wrong += 1
        print("...")
        time.sleep(5)
        print("You are telling the Professor the answer...")
        print("Professor: Finally you got to the answer, let's go ahead and complete this practical. Remember to add HCL into the beaker drop by drop from the Burette, and keep swirling the conical flask until this colour change occurs...")
        time.sleep(3)
        print("You are carring out the titration...")
        time.sleep(3)
        print("The solution has turned colourless and you have closed off the bottom of the Burette. The practical is complete")
        self.colour = "colourless"
        self.k += 1

class B747_yoke: #added to captian sebastian class
  def __init__(self, collected = False):
    self.collected = collected

  def collect(self, player):
    player.pick_up_item("B747 yoke")
    self.collected = True

class B747:
  def __init__(self, ready = False, fixed = False):
    self.ready = ready
    self.fixed = fixed

  def fly(self, destination):
    print(f"Flying to {destination}")