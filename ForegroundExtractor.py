# CREATED BY FRANCESCO CALABRESE

import sys
import os
import cv2
import numpy as np



def img_process(img_path):
    file = img_path

    # READING
    src = cv2.imread(file, 1)

    # LUMINANCE (GRAYSCALE)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # THRESHOLD
    _, alpha = cv2.threshold(tmp, 251, 255, cv2.THRESH_BINARY_INV)

    # MORPHOLOGY DILATION AND EROSION

    # KERNELs
    kernel3 = np.ones((3, 3), np.uint8)
    kernel5 = np.ones((5, 5), np.uint8)
    kernel7 = np.ones((7, 7), np.uint8)
    kernel9 = np.ones((9, 9), np.uint8)

    morphed = alpha

    # SOFT OPEN
    morphed = cv2.erode(morphed, kernel3, iterations=1)
    morphed = cv2.dilate(morphed, kernel3, iterations=1)

    # CLOSE
    morphed = cv2.dilate(morphed, kernel5, iterations=1)
    morphed = cv2.erode(morphed, kernel5, iterations=1)

    # HARD CLOSE
    morphed = cv2.dilate(morphed, kernel7, iterations=1)
    morphed = cv2.erode(morphed, kernel7, iterations=1)

    # OPEN
    morphed = cv2.erode(morphed, kernel5, iterations=1)
    morphed = cv2.dilate(morphed, kernel5, iterations=1)

    # SUPER HARD CLOSE
    morphed = cv2.dilate(morphed, kernel9, iterations=1)
    morphed = cv2.erode(morphed, kernel9, iterations=1)

    alpha = morphed

    # RGB SINGLE CHANNELS EXTRACTION
    b, g, r = cv2.split(src)

    # RGB+APLHA CHANNELS MERGE
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)

    # WRITE
    file_folder = os.path.dirname(img_path)
    file = os.path.basename(img_path)
    filename, file_extension = os.path.splitext(file)
    if len(file_folder) > 0:
        file_folder = file_folder + "/"
    result_file_path = file_folder + "RES_" + filename + ".png"
    print(result_file_path)
    cv2.imwrite(result_file_path, dst)



def main():

    args_count = len(sys.argv)
    if args_count < 2:
        sys.exit("ERROR: No arguments received")
    #TODO: Loop execution for each argument
    if os.path.exists(sys.argv[1]):
        img_process(sys.argv[1])
    else:
        sys.exit("ERROR: Invalid path")

main()
