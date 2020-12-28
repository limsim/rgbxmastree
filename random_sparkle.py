from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree()
# Turn the brightness down. This seems to be dimmest setting you can use.
tree.brightness = 0.04 

# Create a random colour.
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    # Keep on running the code forever
    while True:
      # Pick a pixel in the tree at random
      pixel = random.choice(tree)

      # random.random() generates a random decimal number between 0 and 1. 
      # If the number generated is greater than 0.5 then the selected pixel will be set to a random colour.
      # Otherwise the pixel will be turned off.
      if random.random() > 0.5:
        pixel.color = random_color()
      else:
        pixel.off()
      
      # Wait for 0.1 seconds before doing the next thing.
      sleep(0.1)

except KeyboardInterrupt:
    tree.off()
    tree.close()