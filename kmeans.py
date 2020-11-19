from utils.utils import *
# k = kmean_anchors(path='/home/zlm/dataset/SeaShips/ImageSets/Main/trainval.txt', n=9, img_size=(416, 416), thr=0.20, gen=1000)
# 33,8,  63,14,  98,21,  156,26,  127,40,  206,37,  290,32,  211,58,  335,58
# k = kmean_anchors(path='/home/zlm/dataset/SMD/frame_space=5/ImageSets/Main/trainval.txt', n=9, img_size=(416, 416), thr=0.20, gen=1000)
# 8,6,  12,8,  21,15,  34,10,  48,13,  31,29,  103,32,  52,84,  177,46
k = kmean_anchors(path='/home/zlm/dataset/SMD/single-class/ImageSets/Main/trainval.txt', n=9, img_size=(416, 416), thr=0.20, gen=1000)
#11,7,  27,9,  21,15,  45,12,  32,25,  69,19,  106,33,  54,72,  167,45