import pytesseract
import cv2

class OCREngine:
    def extract_text(self, frame_path: str) -> str:
        img = cv2.imread(frame_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text.strip()
