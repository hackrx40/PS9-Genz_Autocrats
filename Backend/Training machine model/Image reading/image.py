from pikepdf import Pdf, Name, PdfImage

old_pdf = Pdf.open("Amazon 5.pdf")
page_1 = old_pdf.pages[0]
#print(list(page_1.images.keys())) = ['/FXX1']

raw_image = page_1.images['/FXX1']
pdf_image = PdfImage(raw_image)
pdf_image.extract_to(fileprefix="Amazon_5")




import pytesseract as tess
from PIL import Image
D5= Image.open('Amazon_5.jpg')
text = tess.image_to_string(D5)
invoice5 = Image.open('Amazon 5a.jpg')
texta = tess.image_to_string(invoice5)
if text != texta:   
    print("It's a Fraud Document") 
else:
    print("It's a Legal Document") 

    
    
    
import pytesseract as tess
from PIL import Image
D6= Image.open('Amazon 6..jpg')
text1 = tess.image_to_string(D6)
invoice6 = Image.open('Amazon 6..jpg')
text2 = tess.image_to_string(invoice6)
if text1 != text2:
    print("It's a Fraud Document") 
else:
    print("It's a Legal Document")



#Udated code
import pytesseract as tess
from PIL import Image
D5= Image.open('FIR.jpg')
text = tess.image_to_string(D5)
invoice5 = Image.open('FIRa.jpg')
texta = tess.image_to_string(invoice5)
if text != texta:   
    print("It's a Fraud Document") 
else:
    print("It's a Legal Document")