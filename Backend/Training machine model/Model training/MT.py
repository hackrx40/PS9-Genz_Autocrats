import pandas as pd

for ini in range(1,10):
    if ini == 1:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice1.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out1.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 2 :
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice2.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out2.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 3:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice3.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out3.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 4:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice4.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out4.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 5:
        from pikepdf import Pdf, Name, PdfImage
        old_pdf = Pdf.open("Amazon 5.pdf")
        page_1 = old_pdf.pages[0] 
        raw_image = page_1.images['/FXX1']
        pdf_image = PdfImage(raw_image)
        pdf_image.extract_to(fileprefix="Amazon_5")
        import pytesseract as tess
        from PIL import Image
        D5= Image.open('Amazon_5.jpg')
        text = tess.image_to_string(D5)
        invoice5 = Image.open('Amazon 5a.jpg')
        texta = tess.image_to_string(invoice5)
        if text == texta:
            print("It's a Legal Document") 
    elif ini == 6:
        import pytesseract as tess
        from PIL import Image
        D6= Image.open('Amazon 6..jpg')
        text1 = tess.image_to_string(D6)
        invoice6 = Image.open('Amazon 6a.jpg')
        text2 = tess.image_to_string(invoice6)
        if text1 == text2:
            print("It's a Legal Document") 
    elif ini == 7:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice7.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out7.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 8:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice8.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out8.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
    elif ini == 9:
        initial = pd.read_excel("C:\\Users\\tanuc\\\Same_Shape\\invoice9.xlsx")
        update = pd.read_excel("C:\\Users\\tanuc\\Same_Shape\\inv_out9.xlsx")
        compare = initial.equals(update)
        ini=ini+1
        if compare == True:
            print("It's a Legal Document") 
else:
    print("It's a Fraud Document")