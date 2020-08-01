import cv2
import numpy as np
import glob
import os

ofile = glob.glob("origin/*")

def get_size_old(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size_old(path)


for f in ofile:
    img = cv2.imread(f)
    orgHeight, orgWidth = img.shape[:2]

    count = 0
    while 1:


        rimg = cv2.resize(img, (orgWidth-count,orgHeight-count))
        cv2.imwrite('stamp/stamp1.jpg', rimg)
        rsize = get_size_old('stamp/stamp.jpg')
        print(rsize)
        if rsize < 250000 :
            break

        count += 1
