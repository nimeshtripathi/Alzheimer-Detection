import numpy as np
import cv2

def sub_image(brain1_p, brain2_p, flag):
    brain1 = cv2.imread(brain1_p)
    brain2 = cv2.imread(brain2_p)
    difference = cv2.subtract(brain1, brain2)
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]
    brain1[mask != 255] = [0, 0, 255]
    brain2[mask != 255] = [0, 0, 255]
    cv2.imwrite('difference_img/diff_image_' + str(flag) + '.png', brain1)
    
    #referred from: https://gist.github.com/sean-mcclure/fcd9112dde54efb7a0be402e793a6ad4
