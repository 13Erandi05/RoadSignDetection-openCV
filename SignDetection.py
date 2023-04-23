import numpy as np
import cv2
import time
import os

def increseContrast(img,alpha,beta):
    img = cv2.addWeightrd(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
    return img

def filteringImages(img):
    img = cv2.GaussianBlur(img,(11,11),0)
    return img

def returnRedness(img):
    yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    y,u,v = cv2.split(yuv)
    return v

def threshold(img,T=150):
    _,img = cv2.threshold(img,T,255,cv2.THRESH_BINARY)
    return img

def show(img):
    cv2.imwrite('Detected Image/Image.png',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def morphology(img,kernelSize=7):
    kernel = np.ones((kernelSize,kernelSize),np.uint8)
    opening = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    return opening

def findContour(img):
    contours,hi = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def findBiggestContour(contours):
    m = 0
    c = [cv2.contourArea(i) for i in contours]
    return contours[c.index(max(c))]

def boundaryBox(img,contours):
    x,y,w,h = cv2.boundingRect(contours)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img,sign

def preprocessingImageToClassifier(image=None,imageSize=28,mu=89.77428691773):
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image = cv2.resize(image,(imageSize,imageSize))
    image = (img-mu)/std
    image = image.reshape(1,imageSize,imageSize,1)
    return image

def predict4(sign):
    img = preprocessingImageToClassifier(sign,imageSize=28)
    return np.argmax(model.predict(img))

def predict4(sign):
    img = preprocessingImageToClassifier(sign,imageSize=32)
    return np.argmax(model1.predict(img))

def crop_(img,contours):
    x,y,w,h = cv2.boundingRect(contours)
    crop = img[y+4:y+h-4, x+4:x+w-4]
    crop = cv2.resize(crop,(h-8,w-8))
    return crop

def detect_img(path):
    testCase = cv2.imread(path,1)
    img = np.copy(testCase)

    try:
        img = filteringImages(img)
        img = returnRedness(img)
        img = threshold(img,T=155)
        img = morphology(img,11)
        contours = findContour(img)
        big = findBiggestContour(contours)
        out = crop_(testCase,big)
        testCase,sign = boundaryBox(testCase,big)
        tic = time.time()
        
    
    except:
        pass

    show(testCase)
    
    return out


