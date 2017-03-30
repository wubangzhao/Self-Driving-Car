import matplotlib.pyplot as plt
import matplotlib.image as mplimg
import numpy as np
import cv2


blur_ksize = 5  # Gaussian blur kernel size
canny_lthreshold = 50  # Canny edge detection low threshold
canny_hthreshold = 150  # Canny edge detection high threshold


def process_an_image(img):
  # 1. Gray Scale Transformation
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  # 2. Gaussian Smoothing
  blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
  # 3. Canny Edge Detection
  edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
