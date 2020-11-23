#################################### IMPORT LIBRARIES ##############################
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.signal import convolve2d
import os
import imquality.brisque as brisque
import PIL.Image
from PIL import Image
import time

################################### BLURNESS #######################################
def blur(path):
    def variance_of_laplacian(image):
        return cv2.Laplacian(image,cv2.CV_64F).var()
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    return fm

################################### BRISQUE ########################################
def brisq(path):
    img = PIL.Image.open(path)
    sc = brisque.score(img)
    return sc

#################################### NOISE ########################################
def estimate_noise(path):
    img = cv2.imread(path)
    I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    H, W = I.shape
    M = [[1, -2, 1],
       [-2, 4, -2],
       [1, -2, 1]]

    sigma = np.sum(np.sum(np.absolute(convolve2d(I, M))))
    sigma = sigma * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))
    return sigma

#################################### BRIGHTNESS #######################################
def calculate_brightness(path):
    image = Image.open(path)
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    br = 1 if brightness == 255 else brightness / scale
    return br

################################ CONTRAST ########################################
def contrast(path):
    img = cv2.imread(path)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contrast = img_grey.std()
    return contrast

################################ FINAL FUNCTION #################################
def final_check(path):
    blurness = blur(path)
    brisque = brisq(path)
    noise = estimate_noise(path)
    brightness = calculate_brightness(path)
    contra = contrast(path)
    if blurness<100 or brisque > 55 or noise>10 or brightness<0.4 or contra <30:
        return "Failed"
    else:
        return "Passed"

print(final_check('./pan1_sample7.jpg'))