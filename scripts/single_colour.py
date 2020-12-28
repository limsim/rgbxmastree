from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep

tree = RGBXmasTree()
tree.brightness = 0.5

try:
    while True:
        tree.color = Color('#fec89a')
        # sleep(0.1)
except KeyboardInterrupt:
    tree.off()
    tree.close()