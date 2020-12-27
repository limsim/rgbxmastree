from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random
from decimal import *

getcontext().prec = 1

tree = RGBXmasTree()
tree.brightness = 0.04

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

  colourPairs = [['red', 'blue'], 
    ['yellow', 'red'], 
    ['blue', 'green'], 
    ['green', 'blue'], 
    ['orange', 'red'], 
    ['white', 'red'],
    ['red', 'white'],
    ['cyan', 'white'],
    ['magenta', 'red'],
    ['red', 'magenta']
  ]

  numberOfColourPairs = len(colourPairs)
  int(random.random() * numberOfColourPairs)
  chosenColourPair = colourPairs[int(random.random() * numberOfColourPairs)]
  colourFrom = chosenColourPair[0]
  colourTo = chosenColourPair[1]

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

rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,8,10,18,13,9,3]
rowOrder += list(reversed(rowOrder))

try:
  while True:
    randomColourGradient = generate_random_gradient()
    for x in range(50):
      tree[rowOrder[x]].color = randomColourGradient[x%25]
      if x > 25:
        tree[rowOrder[x]].off()        
    
    tree.off()
    
except KeyboardInterrupt:
  tree.off()
  tree.close()