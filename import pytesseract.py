import pytesseract
from PIL import Image
import json
import re
import cv2
import numpy as np
import os

def preprocess_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get a binary image
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Apply dilation and erosion to remove small noise
    kernel = np.ones((1, 1), np.uint8)
    processed_image = cv2.dilate(binary, kernel, iterations=1)
    processed_image = cv2.erode(processed_image, kernel, iterations=1)
    
    # Save the processed image temporarily
    temp_filename = "temp_processed_image.png"
    cv2.imwrite(temp_filename, processed_image)
    
    return temp_filename

def extract_aadhar_from_image(image_path):
    # Preprocess the image to improve OCR accuracy
    processed_image_path = preprocess_image(image_path)
    
    # Load the processed image using PIL
    image = Image.open(processed_image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    print("OCR Text Extracted:", text)
    
    # Use regex to find a 12-digit number with or without spaces which we assume is the aadhar
    match = re.search(r'\b\d{4} ?\d{4} ?\d{4}\b', text)
    if match:
        # Return aadhar without spaces
        aadhar = match.group().replace(' ', '')
        print(f"Extracted aadhar: {aadhar}")
        return aadhar
    
    return None

def get_aadhar_details(aadhar, file_path='sample_aadhar_data.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    for person in data:
        if person['aadhar'] == aadhar:
            return person
    return None

def main():
    image_path = input("Enter the absolute path to the Aadhar image: ")
    
    # Check if the provided path is an absolute path
    if not os.path.isabs(image_path):
        print("Please provide an absolute path.")
        return
    
    aadhar = extract_aadhar_from_image(image_path)
    
    if aadhar:
        details = get_aadhar_details(aadhar)
        
        if details:
            print("Aadhar Details Found:")
            print(json.dumps(details, indent=4))
        else:
            print("No details found for aadhar:", aadhar)
    else:
        print("No valid aadhar found in the image.")

if __name__ == "__main__":
    main()
