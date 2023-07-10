from PIL import Image
from pytesseract import pytesseract

import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1
    
    
class Language(enum.Enum):
    ENG = "eng"
    RUS = "rus"
    ITA = "ita"
    
    
    
    
class ImageReader:
    
    def __init__(self, os: OS):
        if os == OS.Mac:
            print("running on: MAC\n")
            
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print("Running on Windows")
            
    def extract_text(self, image: str, lang: str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text
    
if __name__ == '__main__':
    ir = ImageReader(OS.Windows)
    text = ir.extract_text('images/mot.jpg', lang='eng')
    print(text)