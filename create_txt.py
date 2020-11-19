import os
import random

# txt_file = open('/home/zlm/dataset/SeaShips/ImageSets/Main/trainval.txt', 'r')
txt_file = open('/home/zlm/dataset/SeaShips/ImageSets/Main/val.txt', 'r')
lines = txt_file.read().splitlines()
txt_file.close()
# new_txt_file = open('/home/zlm/dataset/SeaShips/ImageSets/Main/trainval.txt', 'w')
new_txt_file = open('/home/zlm/dataset/SeaShips/ImageSets/Main/val.txt', 'w')
for line in lines:
    new_txt_file.write('/home/zlm/dataset/SeaShips/images/' + line + '.jpg'+'\n')
    print(line)

new_txt_file.close()
