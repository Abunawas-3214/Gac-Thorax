import cv2
import numpy as np
import LungSegmentation as Segmentation
import Validasi as vd
import os
import shutil

UPLOAD_FOLDER = 'static/uploads/'

def GAC():
    Img = cv2.imread('static/uploads/upload.jpg', 0)
    max_its = 300

    # Segmentasi paru-paru kanan
    init_mask_kanan = np.zeros((256, 256))
    init_mask_kanan[44:174, 48:104] = 1
    ParuKanan = Segmentation.LungSegmentation(Img, init_mask_kanan, max_its, 0.5)

    # Segmentasi paru-paru kiri
    init_mask_kiri = np.zeros((256, 256))
    init_mask_kiri[34:158, 153:215] = 1
    ParuKiri = Segmentation.LungSegmentation(Img, init_mask_kiri, max_its, 0.5)

    # Hasil segmentasi
    Result = ParuKanan + ParuKiri
    cv2.imwrite('static/uploads/result.jpg', Result)

    # Mendapatkan Nilai Akurasi
    ImageTest = cv2.imread('static/uploads/result.jpg', 0)
    akurasi = vd.validate(ImageTest)
    print('Akurasi = '+akurasi)