from PIL import Image
from collections import Counter
import numpy as np
import cv2
import os

im = []
sim = []
val = []

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        pa = os.path.join(folder,filename)
        img = cv2.imread(pa,1)
        #resize the images
        im.append(img)
        ref_arr = np.asarray(img)
        flat_array = ref_arr.flatten()
        RH = Counter(flat_array)

        H = []
        for i in range(256):
            if i in RH.keys():
                H.append(RH[i])
            else:
                H.append(0)
        val.append(H)
        

def L2Norm(H1,H2):
    distance =0
    for i in range(len(H1)):
        distance += np.square(H1[i]-H2[i])
    return np.sqrt(distance)

file= 'Dataset'
load_images_from_folder(file)

#print(val[0])
original = cv2.imread(r'res.jpg',1)
ref_arr = np.asarray(original)

flat_array = ref_arr.flatten()
RH = Counter(flat_array)

H = []
for i in range(256):
    if i in RH.keys():
        H.append(RH[i])
    else:
        H.append(0)

#print(H)

for i in range(len(val)):
    dis = L2Norm(H,val[i])
    if not np.isnan(dis):
        sim.append(dis)
        print(dis)
    else:
        continue

print(max(sim))
index = sim.index(max(sim))
cv2.imshow("res",im[index])
print(index)
