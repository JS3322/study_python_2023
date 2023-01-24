'''
 * @Process: complete
 * @Project_Name: module
 * @Package_Name: ocr
 * @Made_By: JS
 * @The_creation_time: --
 * @File_Name: numpy.py
 * @Version : Python 3.7.8
 * @contents: -
'''
import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'__pwd__'

'Naver Clova Ocr korean language ocr'
'tenserflow oct ai test project init 20211210'
doc = fitz.open('test.pdf')
page = doc.load_page(3)
mat = fitz.Matrix(2, 2)
pix = page.get_pixmap(matrix=mat)
output = 'test.png'
pix.save(output)

image_save = image.open('test.png')
result = pytesseract.image_to_string(image_save, lang='kor')
print(result)
