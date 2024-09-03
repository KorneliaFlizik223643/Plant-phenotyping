import cv2 
import os
from patchify import patchify


# Crop image from path
def cropping(image_path):
    # Read an image from the path 
    img = cv2.imread(image_path)
    # Convert the image to a grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Use adaptive thresholding to create a binary image
    _, thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)
    # Find contours in the binary image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Find the contour with the largest area
    largest_contour = max(contours, key=cv2.contourArea)
    # Find bounding box coordinates of the contour
    x, y, w, h = cv2.boundingRect(largest_contour)
    # Make it square
    h=w
    # Crop the region of interest from the original image
    cropped_image = img[y:y + h, x:x + w]
    cropped_folder = "Cropped"
    output_file_path = os.path.join(cropped_folder, os.path.basename(image_path))
    cv2.imwrite(output_file_path, cropped_image)
    
    return cropped_image


# Crop image 
def crop_image(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    coordinates=[x,y,w,h]
    cropped_image = image[y:y + h, x:x + h]
    
    return cropped_image, coordinates

def padder(image, patch_size):
    h = image.shape[0]
    w = image.shape[1]
    height_padding = ((h // patch_size) + 1) * patch_size - h
    width_padding = ((w // patch_size) + 1) * patch_size - w

    top_padding = int(height_padding/2)
    bottom_padding = height_padding - top_padding

    left_padding = int(width_padding/2)
    right_padding = width_padding - left_padding

    padded_image = cv2.copyMakeBorder(image, top_padding, bottom_padding, left_padding, right_padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    return padded_image

# Predict patches
def predict_patches(image_path, model, patch_size):
    # Read, crop and patch
    image = cv2.imread(image_path)
    image, _ =crop_image(image)
    image = padder(image, patch_size)
    patches = patchify(image, (patch_size, patch_size, 1), step=patch_size)
    # Adjust patches for prediction
    i = patches.shape[0]
    j = patches.shape[1]
    patches = patches.reshape(-1, patch_size, patch_size, 1)
    patches.shape
    #predict
    preds = model.predict(patches/255,verbose=0) 
    preds = preds.reshape(i, j, patch_size, patch_size)
    preds.shape
    
    return image, preds
