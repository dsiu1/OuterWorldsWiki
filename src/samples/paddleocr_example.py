import numpy as np
from paddleocr import PaddleOCR
from PIL import Image

ocr = PaddleOCR(lang="en")
img = Image.open("./Bellamy_Personal_Terminal_3.png")
ocr.predict(np.array(img))
