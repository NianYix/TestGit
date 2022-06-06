# import pytesseract
# from PIL import Image
# # 读取图片
# im = Image.open(r'F:\Work\JerryStudy\GitPos\TestGit\图像文字识别\ttttttt.jpg')
# # 识别文字
# string = pytesseract.image_to_string(im, lang='chi_sim')
# print(string)

# from cnocr import CnOcr
# ocr = CnOcr()
# res = ocr.ocr_for_single_line('sentence.jpg')
# print("Predicted Chars:", res)

import easyocr
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext(r'C:\Users\Jerry\Desktop\bx\2021.12.20\ttttttt.jpg')
# print(result)
for i in result:
    word = i[1]
    print(word)