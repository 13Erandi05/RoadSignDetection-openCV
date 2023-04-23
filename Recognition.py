import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from tabulate import tabulate

FONTSIZE = 10
COLOR = 'maroon'

im = []
sim = []
titles = ['Speed limit (20km/h)',
           'Speed limit (50km/h)','Speed limit (60km/h)',
           'Speed limit (70km/h)','Speed limit (80km/h)',
           'Speed limit (100km/h)','Speed limit (120km/h)',
           'Overtaking Not allowed','Overtaking prohibited for trucks',
           'Cossroad ahead-side roads to right and left','Priority road',
           'Give way to all traffic','Stop','Entry not allowed',
           'Lorries -truck prohibited','No entry',
           'cars not allowed','Dangerous curve left',
           'Dangerous curve right','Double curve',
           'Bumpy road','Slippery road','Road narrows on the right',
           'Road work','Traffic signals',
           'Pedestrians','Children crossing',
           'Bicycles crossing','Beware of ice/snow',
           'Turn right ahead','Turn left ahead',
           'Ahead only','Go straight or right',
           'Go straight or left','Keep right',
           'Keep left','Roundabout mandatory','Speed limit (30km/h)',
           'Dear crossing area - road']

def load_images_from_folder(folder,dim):
    im.clear()
    sim.clear()
    for filename in os.listdir(folder):
        pa = os.path.join(folder,filename)
        img = cv2.imread(pa,1)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        #resize the images
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #img = cv2.medianBlur(img,7)
        im.append(img)

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

def compare_similarity(original_img):
    img1 = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    
    for i in range(len(im)):
        img2 = im[i]
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
        size = img1.shape
        img2 = cv2.resize(img2, (size[1],size[0]), interpolation = cv2.INTER_AREA)

        error, diff = mse(img1, img2)
        sim.append(error)


def recognize_sign(ori):
    sign_name = []
    ratio = []
    data = []
    dim = (ori.shape[1], ori.shape[0])

    file= 'Dataset'
    load_images_from_folder(file,dim)
    compare_similarity(ori)

    sim_copy = sim.copy()
    sim_copy.sort()
    
    for i in range (20):
        ind = sim.index(sim_copy[len(sim_copy)-1-i])
        sign_name.append(titles[ind])
        ratio.append(sim[ind])
        plt.subplot(4,5,i+1)
        plt.title(titles[ind],c = COLOR,fontsize = FONTSIZE)
        plt.imshow(im[ind])
        plt.axis('off')

    plt.show()

    for i in range(20):
        arr = []
        arr.append(sign_name[i])
        arr.append("%.2f"%(ratio[i]*100))
        data.append(arr)

    print (tabulate(data, headers=["Sign name", "Similarity Ratio"]))
    
    return 
