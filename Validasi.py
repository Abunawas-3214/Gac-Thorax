import cv2
import numpy as np

def validasi(ImgTest, ImgManual):
    Test = ImgTest.astype(int)
    Manual = ImgManual

    hitam = 0
    np.where(Test)


ImgTest = cv2.imread('static/uploads/result.jpg', 0)
ImgManual = cv2.imread('static/manual/JPCLN0_1.jpg', 0)
validasi(ImgTest, ImgManual)