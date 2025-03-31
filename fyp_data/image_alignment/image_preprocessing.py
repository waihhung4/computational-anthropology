import fitz
import cv2
import numpy as np
import os

def extract_pdf_page_as_image(pdf_path, page_number, output_image_path):
    doc = fitz.open(pdf_path)
    page = doc[page_number]

    pix = page.get_pixmap(dpi=300)
    pix.save(output_image_path)
    print(f"Saved page {page_number+1} as an image: {output_image_path}")
    return output_image_path

def extract_table_rows(image_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    for idx, contour in enumerate(sorted_contours):
        x, y, w, h = cv2.boundingRect(contour)

        if h > 20 and w > 200:
            row = image[y:y+h, x:x+w]

            output_path = os.path.join(output_dir, f"row_{idx+1}.png")
            cv2.imwrite(output_path, row)
            print(f"Saved row {idx+1} to {output_path}")

    print(f"Row extraction complete. Check {output_dir} for results.")

def extract_rows_from_pdf(pdf_path, page_number, output_dir):

    page_image_path = os.path.join(output_dir, "page_image.png")

    extract_pdf_page_as_image(pdf_path, page_number, page_image_path)

    rows_output_dir = os.path.join(output_dir, "rows")
    extract_table_rows(page_image_path, rows_output_dir)

if __name__ == "__main__":
    pdf_path = "chinese and sumerian.pdf"
    page_number = 185
    output_dir = "images"

    extract_rows_from_pdf(pdf_path, page_number, output_dir)
