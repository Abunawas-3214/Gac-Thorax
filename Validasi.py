import cv2
import os
import pandas as pd
import numpy as np

def getAccuration(ImgTest, ImgManual):
    Test = np.array(ImgTest).flatten()
    Test = np.where(Test < 126, 0, 255)
    Manual = np.array(ImgManual).flatten()

    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(np.size(Test)):
        if (Test[i] == 255 and Manual[i] == 255):
            TP += 1
        if (Test[i] == 0 and Manual[i] == 0):
            TN += 1
        if (Test[i] == 255 and Manual[i] == 0):
            FP += 1
        if (Test[i] == 0 and Manual[i] == 255):
            FN += 1

    accuration = ((TP + TN) / (TP+TN+FP+FN)) * 100
    return accuration
    # df = pd.DataFrame(Test)
    # breakpoint()

def validate(ImageTest):
    ManualImagePath = 'static/manual/'
    dir_list = os.listdir(ManualImagePath)
    bestAccuration = 0
    for i in dir_list:
        ManualImage = cv2.imread('static/manual/' + i, 0)
        accImage = getAccuration(ImageTest, ManualImage)
        if bestAccuration < accImage:
            bestAccuration = accImage

    return bestAccuration