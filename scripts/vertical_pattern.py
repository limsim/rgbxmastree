from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree()
# tree.brightness = 0.04 

def random_colour():
  colours = ['blue', 'green', 'yellow', 'cyan', 'magenta', 'red']
  randomIndex = int(len(colours) * random.random())
  return colours[randomIndex]

column1 = [0,1,2] #1
column2 = [24,23,22] #2
column3 = [19,20,21] #3
column4 = [6,5,4] #4
column5 = [12,11,10] #5
column6 = [16,17,18] #6
column7 = [15,14,13] #7
column8 = [7,8,9] #8

theColumnTree = [column1, column2, column3, column4, column5, column6, column7, column8]

try:
  while True:
    chosenColour = random_colour()
    for x in range(8):
      for y in theColumnTree[x]:
        tree[y].color = Color(chosenColour)
        # sleep(0.1)
    # This is the pixel at the top of the tree
    # tree[3].color = Color(chosenColour)

except KeyboardInterrupt:
  tree.off()
  tree.close()