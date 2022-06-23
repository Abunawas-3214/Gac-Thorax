import numpy as np

# Pre Processing Grayscaling
def preGrayscale(img):
    H, W = img.shape[:2]
    gray = np.zeros((H, W), np.uint8)
    for i in range(H):
        for j in range(W):
            gray[i, j] = np.clip((int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2]))/3, 0, 255)
    return gray

# Pre Processing Contrast Streaching
def preContrastStreatching(img):
    H, W = img.shape[:2]
    ct = np.zeros((H, W), np.uint8)

    r1 = 100
    s1 = 50
    r2 = 150
    s2 = 200

    for i in range(H):
        for j in range(W):
            x = img[i][j]
            if(0 <= x and x <= r1):
                ct[i, j] = np.clip((s1/r1 * x), 0, 255)
            elif(r1 < x and x <= r2):
                ct[i, j] = np.clip((((s2 - s1) / (r2 - r1)) * (x - r1) + s1), 0, 255)
            elif(r2 < x and x <= 255):
                ct[i, j] = np.clip((((255 - s2) / (255 - r2)) * (x - r2) + s2), 0, 255)
    return ct

# Pre Processing Median Filtering
def preMedianFiltering(img):
    H, W = img.shape[:2]
    filter_size = 9

    mf = np.zeros((H, W), np.uint8)

    filter_array = [img[0][0]] * filter_size

    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            filter_array[0] = img[i - 1, j - 1]
            filter_array[1] = img[i, j - 1]
            filter_array[2] = img[i + 1, j - 1]
            filter_array[3] = img[i - 1, j]
            filter_array[4] = img[i, j]
            filter_array[5] = img[i + 1, j]
            filter_array[6] = img[i - 1, j + 1]
            filter_array[7] = img[i, j + 1]
            filter_array[8] = img[i + 1, j + 1]

            filter_array.sort()

            mf[i, j] = np.clip(filter_array[4], 0, 255)

    return mf