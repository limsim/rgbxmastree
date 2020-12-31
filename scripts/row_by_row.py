from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree()
tree.brightness = 0.04

try:
  rowOrder = [0,24,19,6,12,16,15,7,1,23,20,5,11,17,14,8,2,22,21,4,10,18,13,9]

  row1 = [(1, 1, 1), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 1)]
  row2 = [(1, 1, 1), (1, 1, 1), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1)]
  row3 = [(1, 1, 1), (1, 1, 1), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1)]

  allRows = [row1, row2, row3]

  while True:
    darkTree = [(0,0,0)] * 25

    for j in range(3):
      tree.value = allRows[j]
      sleep(1)

    tree.off()
  

  # tree.value = [
  #   (1,1,1), (0,0,0), (0,0,0), (0,0,0), (0,0,0),
  #   (1,1,1), (1,1,1), (0,0,0), (0,0,0), (0,0,0),
  #   (0,0,0), (1,1,1), (0,0,0), (0,0,0), (1,1,1),
  #   (1,1,1), (0,0,0), (0,0,0), (1,1,1), (0,0,0),
  #   (0,0,0), (0,0,0), (0,0,0), (1,1,1), (0,0,0)
  # ]
    
except KeyboardInterrupt:
  tree.off()
  tree.close()