'''Implement a class called player that represents a cricket player. The playerclass should have a 
method called play() which prints "The players is playing cricket. Derive a two classes, Batsman and 
Bowler, from the player class. Override the play() method in each derived classto print "The batsman 
is batting" and "The blower is blowing",respectively. Write a program to create subjects or both the 
Batsman and Bowler classes and call tha play() method for each object.'''


# Define the base class Player 
class Player: 
  def play(self): 
    print("The player is playing cricket.") 

# Define the derived class Batson: 
class Batsman (Player): 
  def play(self): 
    print("The batsman is batting.") 

# Define the derived class Bowler 
class Bowler (Player): 
  def play(self): 
    print("The bowler is bowling.") 

# Create objects of Batsman and Bowler classes 
batsman = Batsman ()
bowler = Bowler ()

# call the play() 1 method for each object 
batsman.play()
bowler.play()