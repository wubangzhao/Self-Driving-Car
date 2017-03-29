
blur_ksize = 5



def process_an_image(img):
  # 1. Gray Scale Transformation
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  # 2. Gaussian Smoothing
  blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
