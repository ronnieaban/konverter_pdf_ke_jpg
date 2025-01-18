import fitz  # PyMuPDF
from PIL import Image
import os
import sys

def pdf_to_jpg(pdf_path, output_folder, dpi=300):
    """
    Convert PDF pages to JPG images
    
    Args:
        pdf_path (str): Path to input PDF file
        output_folder (str): Directory to save JPG images
        dpi (int): Output image resolution (default: 300)
    
    Returns:
        list: Paths to generated JPG files
    """
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        if not pdf_document.is_pdf:
            raise ValueError("Invalid PDF file")
            
        # Create output directory if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        jpg_files = []
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Convert each page to JPG
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            zoom = dpi / 72  # Convert DPI to zoom factor
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image and save as JPG
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            output_path = os.path.join(output_folder, f"{base_name}_page{page_num + 1}.jpg")
            img.save(output_path, "JPEG", quality=95)
            jpg_files.append(output_path)
            
        return jpg_files
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_pdf> <output_folder>")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_folder = sys.argv[2]
    
    if not os.path.isfile(input_pdf):
        print(f"Error: Input file {input_pdf} does not exist")
        sys.exit(1)
        
    jpg_files = pdf_to_jpg(input_pdf, output_folder)
    
    if jpg_files:
        print(f"Successfully converted {len(jpg_files)} pages")
        print(f"JPG files saved in: {output_folder}")
    else:
        print("Conversion failed")
