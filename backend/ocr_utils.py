import pytesseract
from PIL import Image
import io

def extract_ingredients(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("L")  # 그레이스케일
    text = pytesseract.image_to_string(image, lang='kor')
    lines = [line.strip().lower() for line in text.split("\n") if line.strip()]
    return lines