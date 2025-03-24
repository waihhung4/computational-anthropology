import fitz  # PyMuPDF
import cv2
import numpy as np
import os

# Step 1: Extract a page from the PDF as an image
def extract_pdf_page_as_image(pdf_path, page_number, output_image_path):
    """
    Extract a specific page from a PDF and save it as an image.
    """
    # Open the PDF
    doc = fitz.open(pdf_path)
    page = doc[page_number]

    # Render the page as an image
    pix = page.get_pixmap(dpi=300)  # Set resolution to 300 DPI for better quality
    pix.save(output_image_path)
    print(f"Saved page {page_number+1} as an image: {output_image_path}")
    return output_image_path

# Step 2: Extract table rows from the page image
def extract_table_rows(image_path, output_dir):
    """
    Extract rows of a table from an image and save them as separate images.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to enhance the table
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Find contours (to detect rows in the table)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours top-to-bottom by Y-coordinate
    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    # Loop through each detected row
    for idx, contour in enumerate(sorted_contours):
        # Get bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Ignore small contours (filter noise)
        if h > 20 and w > 200:  # Adjust these thresholds based on table structure
            # Crop the row
            row = image[y:y+h, x:x+w]

            # Save the row as an image
            output_path = os.path.join(output_dir, f"row_{idx+1}.png")
            cv2.imwrite(output_path, row)
            print(f"Saved row {idx+1} to {output_path}")

    print(f"Row extraction complete. Check {output_dir} for results.")

# Step 3: Combine everything to process a PDF and extract rows
def extract_rows_from_pdf(pdf_path, page_number, output_dir):
    """
    Extract rows from a specific page of a PDF and save them as separate images.
    """
    # Temporary path to save the page as an image
    page_image_path = os.path.join(output_dir, "page_image.png")

    # Step 1: Extract the PDF page as an image
    extract_pdf_page_as_image(pdf_path, page_number, page_image_path)

    # Step 2: Extract table rows from the page image
    rows_output_dir = os.path.join(output_dir, "rows")
    extract_table_rows(page_image_path, rows_output_dir)
# Example Usage
if __name__ == "__main__":
    # Path to the PDF
    pdf_path = "chinese and sumerian.pdf"
    page_number = 185  # Page to extract (0-based index)
    output_dir = "images"

    # Extract scripts from the specified page
    extract_rows_from_pdf(pdf_path, page_number, output_dir)
