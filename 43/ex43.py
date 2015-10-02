from sys import exit
from random import randint

class Scene(object):

  def enter(self):
    print "This scene is not yet configured. Subclass it and implement enter()"
    exit(1)

class Engine(object):

  def __init__(self, scene_map):
    self.scene_map = scene_map
  
  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

    current_scene.enter()
    

class Death(Scene):
  quips = [
    "You died. You're bad at this game",
    "Nice try, but no cigar"
  ]

  def enter(self):
    print self.quips[randint(0, len(self.quips)-1)]
    exit(1)


class CentralCorridor(Scene):

  def enter(self):
    print "Here is the Central Corridor of your besieged ship as it is being boarded."
    print "You see a Gothon of Planet Percal."
    action = raw_input("> ")
    if action == "shoot!":
      print "miss. He kills you"
      return 'death'
    elif action == "dodge!":
      print "fall down. He kills you"
      return 'death'
    elif action == "tell a joke":
      print "The Gothon laughs so hard that you have a "
      print "moment to shoot him and duck into the Weapon Armory"
      return 'laser_weapon_armory'
    else:
      print "DOES NOT COMPUTE!"
      return 'central_corridor'


class LaserWeaponArmory(Scene):

  def enter(self):
    print """In the Armory, you try to guess the keypad to get
      at the bomb. You have 10 guesses."""
    
    code = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
    #hard-code to test
    code = "999"
    guess = raw_input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
      print "BZZZZZEDD!"
      guesses += 1
      guess = raw_input("[keypad]> ")

    if guess == code:
      print "You grab the bomb and race to place it on the Bridge"
      return 'the_bridge'
    else:
      print "The lock buzzes and the mechanism fuses shut."
      print "The Gothons find and kill you."
      return 'death'

class TheBridge(Scene):

  def enter(self):
    print """You burst onto the bridge and see 5 Gothons. Do you
      throw the bomb or slowly place the bomb?"""

    action = raw_input("> ")

    if action == "throw the bomb":
      print """In a panic you throw the bomb at the Gothons and leap for the door. 
        As you do, they shoot you"""
      return 'death'

    elif action == "slowly place the bomb":
      print """You place the bomb on the floor and, pointing your blaster 
          at it, make for the escape pods."""
      return 'escape_pod'


class EscapePod(Scene):

  def enter(self):
    print "You see 5 escape pods, and you don't know which ones are damaged."
    print "Which one do you take?"
    
    good_pod = randint(1, 5)
    #hard-code to test
    good_pod = 1
    guess = raw_input("[pod #]> ")

    print "You jump into pod %s eject from the mother ship" % guess
    if int(guess) != good_pod:
      print "The pod disintegrates, and you die!"
      return 'death'
    else:
      print "The pod flies smoothly into space. You look behind and see"
      print "the mother ship explode, taking the Gothon ship along with it!"
      return 'finished'
      

class Finished(Scene):

  def enter(self):
    print "You won! Good job!"
    return 'finished'


class Map(object):
  
  scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
  }
  
  def __init__ (self, start_scene):
    self.start_scene = start_scene
  
  def next_scene(self, scene_name):
    result = Map.scenes.get(scene_name)
    return result

  def opening_scene(self):
    return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
