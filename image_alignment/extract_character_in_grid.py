import cv2
import numpy as np
from PIL import Image

for number in range(1, 111):
    
    if number == 56 or number == 58:
        continue
    
    sumerian_path = f'squares/{number}/sumerian.png'
    chinese_path = f'squares/{number}/chinese.png'
    sumerian = cv2.imread(sumerian_path)
    chinese = cv2.imread(chinese_path)

    # Convert to grayscale
    gray_sumerian = cv2.cvtColor(sumerian, cv2.COLOR_BGR2GRAY)
    gray_chinese = cv2.cvtColor(chinese, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to binarize the image
    _, thresh_sumerian = cv2.threshold(gray_sumerian, 200, 255, cv2.THRESH_BINARY_INV)
    _, thresh_chinese = cv2.threshold(gray_chinese, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours_sumerian, _ = cv2.findContours(thresh_sumerian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_chinese, _ = cv2.findContours(thresh_chinese, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours and extract bounding boxes
    for i, contour in enumerate(contours_sumerian):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        
        grid_sumerian = sumerian[y:y + h, x:x + w]
        
        # Save the grid as an image
        grid_image = Image.fromarray(cv2.cvtColor(grid_sumerian, cv2.COLOR_BGR2RGB))
        grid_image.save(f'squares/{number}/sumerian/grid_{i}.png')

    for i, contour in enumerate(contours_chinese):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        
        grid_chinese = chinese[y:y + h, x:x + w]
        
        # Save the grid as an image
        grid_image = Image.fromarray(cv2.cvtColor(grid_chinese, cv2.COLOR_BGR2RGB))
        grid_image.save(f'squares/{number}/chinese/grid_{i}.png')

    print(f"{number}: Extraction complete.")