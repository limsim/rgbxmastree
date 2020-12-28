from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep

tree = RGBXmasTree()
tree.brightness = 0.5

try:
    while True:
        tree.color = Color((0,255,0))
        # tree.color = Color('#fec89a')
        # tree.color = Color('red')
        # sleep(0.1)
except KeyboardInterrupt:
    tree.off()
    tree.close()