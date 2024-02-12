import cv2


def brighten_image(img, alpha, beta):
    img_bright = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return img_bright


def blur_image(img, ksize_n, k_size_m, sigmaX):
    img_blur = cv2.GaussianBlur(img, ksize=(ksize_n, k_size_m), sigmaX=sigmaX)
    return img_blur


def get_edge(img):
    # getEdge = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    getEdge = cv2.adaptiveThreshold(img, 55, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    return getEdge


def remove_noise(img, pixel_d):
    color_image = cv2.bilateralFilter(img, pixel_d, 300, 300)
    return color_image


def cartoon(img, mask):
    cartoon_image = cv2.bitwise_and(img, img, mask=mask)
    return cartoon_image