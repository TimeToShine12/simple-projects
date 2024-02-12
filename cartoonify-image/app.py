import cv2
import numpy as np
import streamlit as st
from PIL import Image


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

def main():
    st.title('OpenCV App')

    image_file = st.file_uploader('Upload image', type=['jpg', 'png', 'jpeg'])

    if not image_file:
        return None

    st.sidebar.markdown('Brightening Input Parameters')
    brightness_alpha = st.sidebar.slider('Alpha for brightness:', min_value=0, max_value=100, value=1)
    brightness_beta = st.sidebar.slider('Beta for brightness:', min_value=-50, max_value=100, value=1)

    st.sidebar.markdown('Bluing Input Parameters')
    kernel_size_n = st.sidebar.slider('Kernel size rows:', min_value=1, max_value=15, value=5, step=2)
    kernel_size_m = st.sidebar.slider('Kernel size columns:', min_value=1, max_value=15, value=5, step=2)
    sigma_x = st.sidebar.slider('SigmaX:', min_value=0.1, max_value=4.1, value=0.5, step=0.1)
    pixel_d = st.sidebar.slider('Diameter of pixel:', min_value=0, max_value=20, value=10)

    orig_img = Image.open(image_file)
    orig_img = np.array(orig_img)

    processed_image = brighten_image(img=orig_img, alpha=brightness_alpha, beta=brightness_beta)
    processed_image = blur_image(processed_image, ksize_n=kernel_size_n, k_size_m=kernel_size_m, sigmaX=sigma_x)

    cartoon_img = blur_image(orig_img, ksize_n=kernel_size_n, k_size_m=kernel_size_m, sigmaX=sigma_x)

    gray = cv2.cvtColor(orig_img, cv2.COLOR_RGB2GRAY)
    gray = blur_image(gray, ksize_n=kernel_size_n, k_size_m=kernel_size_m, sigmaX=sigma_x)
    edge = get_edge(gray)
    noiseless = remove_noise(orig_img, pixel_d=pixel_d)
    cartoon_img = cartoon(noiseless, edge)


    st.image([orig_img, edge, cartoon_img], caption=['Original Image', 'Edged Image', 'Cartoon Image'])

if __name__ == '__main__':
    main()
