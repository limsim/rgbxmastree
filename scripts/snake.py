from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree()
tree.brightness = 0.5

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
    ['blue', 'magenta'],
    ['#f77f00', '#55a630']
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

# The sequence of pixels to light up so that they appear to go in rows
rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,4,10,18,13,9]
# This order includes the pixel at the top of the tree.
# rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,4,10,18,13,9,3]

numberOfPixels = len(rowOrder)

try:
  while True:
    # Generate the colours for each pixel.
    randomColourGradient = generate_random_gradient()
    # Turn the pixels on pixel by pixel with each colour on the generate_random_gradient.
    for x in range(21):
      tree[rowOrder[x]].color = randomColourGradient[x]
      tree[rowOrder[x + 1]].color = randomColourGradient[x+1]
      tree[rowOrder[x + 2]].color = randomColourGradient[x+1]
      tree[rowOrder[x + 3]].color = randomColourGradient[x+1]
      tree[rowOrder[x - 1]].off()

      sleep(0.05)
      if x == 20:
        tree[rowOrder[x]].off()
        sleep(0.05)
        tree[rowOrder[x + 1]].off()
        sleep(0.05)
        tree[rowOrder[x + 2]].off()
        sleep(0.05)
        tree[rowOrder[x + 3]].off()
        sleep(0.05)
    
    # After all pixels are lit up turn it all off and start again.
    # tree.off()
    
except KeyboardInterrupt:
  tree.off()
  tree.close()