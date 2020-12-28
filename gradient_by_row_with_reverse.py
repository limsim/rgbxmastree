from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random
from decimal import *
import numpy as np

getcontext().prec = 1

tree = RGBXmasTree()
tree.brightness = 0.04

def random_colour():
  return tuple(np.random.choice(range(256), size=3))

def generate_random_gradient_from_list():
  colourGradient = []

  # Available colours
  # black
  # blue
  # green
  # yellow
  # cyan
  # white
  # magenta
  # red

  colours = ['blue', 'green', 'yellow', 'cyan', 'white', 'magenta', 'red']

  colourFrom = random.choice(colours)
  colourTo = random.choice(colours)

  return [colourFrom, colourTo]

def generate_random_gradient_by_pair():
  colourGradient = []

  # This are all the colour pairs your tree can transition to and from
  # You can modify this list to your liking. 
  # The colours that you can use a listed above.
  colourPairs = [['red', 'blue'], 
    ['yellow', 'red'], 
    ['blue', 'green'], 
    ['green', 'blue'], 
    ['orange', 'red'], 
    ['white', 'red'],
    ['red', 'white'],
    ['cyan', 'white'],
    ['magenta', 'red'],
    ['red', 'magenta'],
    ['red', 'blue'],
    ['blue', 'red'],
    ['red', 'green'],
    ['green', 'red']
  ]

  # Workout the number of colour pairs available.
  numberOfColourPairs = len(colourPairs)
  # Choose a random colour pair.
  chosenColourPair = colourPairs[int(random.random() * numberOfColourPairs)]
  colourFrom = chosenColourPair[0]
  colourTo = chosenColourPair[1]

  return [colourFrom, colourTo]

def generate_random_gradient_by_hex_pair():

  # This are all the colour pairs your tree can transition to and from
  # You can modify this list to your liking. 
  # The colours that you can use a listed above.
  colourPairs = [['#00ff87', '#60efff'],
  ['#ff1b6b', '#45caff'],
  ['#432371', '#faae7b'],
  ['#ff0f7b', '#f89b29'],
  ['#9bafd9', '#103783'],
  ['#e9d022', '#e60b09'],
  ['#CF1A4B', '#3952F5']
  ]

  # Workout the number of colour pairs available.
  numberOfColourPairs = len(colourPairs)
  # Choose a random colour pair.
  chosenColourPair = colourPairs[int(random.random() * numberOfColourPairs)]
  colourFrom = chosenColourPair[0]
  colourTo = chosenColourPair[1]

  return [colourFrom, colourTo]

def generate_gradient(colourFrom, colourTo):
  colourGradient = []
  
  # Create a 25 step colour gradient (because there are 25 pixels on the tree) 
  # that goes from the first colour in the colour pair to the second colour.
  for c in Color(colourFrom).gradient(Color(colourTo), 25):
    colourGradient.append(c)

  return colourGradient

rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,8,10,18,13,9,3]
rowOrder += list(reversed(rowOrder))

try:
  while True:
    colourPair = generate_random_gradient_from_list()

    # Uncomment the line below (remove the '#') to see what the colour are being used.
    # print(f'{colourPair[0]} -> {colourPair[1]}')
    randomColourGradient = generate_gradient(colourPair[0], colourPair[1])
    for x in range(50):
      tree[rowOrder[x]].color = randomColourGradient[x%25]
      if x > 26:
        tree[rowOrder[x]].off()        
    
    tree.off()
    
except KeyboardInterrupt:
  tree.off()
  tree.close()