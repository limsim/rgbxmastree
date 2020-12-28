from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random
from decimal import *

getcontext().prec = 1

tree = RGBXmasTree()
# tree.brightness = 0.04 

def random_colour():
  r = Decimal(random.random())
  g = Decimal(random.random())
  b = Decimal(random.random())
  return (r, g, b)

def generate_random_gradient():
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
    ['green', 'red'],
    ['blue', 'magenta']
  ]

  # Workout the number of colour pairs available.
  numberOfColourPairs = len(colourPairs)
  # Choose a random colour pair.
  chosenColourPair = colourPairs[int(random.random() * numberOfColourPairs)]
  colourFrom = chosenColourPair[0]
  colourTo = chosenColourPair[1]

  # Create a 25 step colour gradient (because there are 25 pixels on the tree) 
  # that goes from the first colour in the colour pair to the second colour.
  for c in Color(colourFrom).gradient(Color(colourTo), 25):
    colourGradient.append(c)

  return colourGradient


column1 = [0,1,2,3] #1
column2 = [4,5,6] #4
column3 = [7,8,9] #8
column4 = [10,11,12] #5
column5 = [13,14,15] #7
column6 = [16,17,18] #6
column7 = [19,20,21] #3
column8 = [22,23,24] #2
theColumnTree = [column1, column2, column3, column4, column5, column6, column7, column8]

# The sequence of pixels to light up so that they appear to go in rows
rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,8,10,18,13,9]
# This order includes the pixel at the top of the tree.
# rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,8,10,18,13,9,3]

numberOfPixels = len(rowOrder)

try:
  while True:
    # Generate the colours for each pixel.
    randomColourGradient = generate_random_gradient()
    # Turn the pixels on pixel by pixel with each colour on the generate_random_gradient.
    for x in range(24):
      tree[rowOrder[x]].color = randomColourGradient[x]
      if x == (numberOfPixels - 1):
        sleep(0.5)       
    
    # After all pixels are lit up turn it all off and start again.
    # tree.off()
    
except KeyboardInterrupt:
  tree.off()
  tree.close()