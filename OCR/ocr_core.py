from ctypes import sizeof
from PIL import Image
from numpy import append
import pytesseract


# Defining paths to tesseract.exe
# and the image we would be using





def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    image_path = filename

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    # Displaying the extracted text
    # print(text[:-1])

    #print(text.split())
    text = text.split()
    print(text)
    #Example List
    # list = ['Name:', 'Address:', 'Date','SSN:','History:','Ongoing','Diagnosis','Future']
    # index=[]
    # ###################################Labels##################################
    # patients_name=[]
    # patients_Address=[]
    # patients_date=[]
    # patients_ssn=[]
    # patients_history=[]
    # patients_Ongoing=[]
    # patients_Diagnosis=[]
    # patients_Future=[]

    # for i in list:
    #     index.append(text.index(i))
    # print(index)

    # #for i in range(len(text)):
    # for i in range(index[0]+1,index[1]):
    #     patients_name.append(text[i])
    # print(patients_name)



    # for i in range(index[1]+1,index[2]):
    #     patients_Address.append(text[i])
    # print(patients_Address)


    # for i in range(index[2]+3,index[3]):
    #     patients_date.append(text[i])
    # print(patients_date)



    # for i in range(index[3]+1,index[4]):
    #     patients_ssn.append(text[i])
    # print(patients_ssn)


    # for i in range(index[4]+1,index[5]):
    #     patients_history.append(text[i])
    # print(patients_history)


    
    # for i in range(index[5]+5,index[6]):
    #     patients_Ongoing.append(text[i])
    # print(patients_Ongoing)





    # for i in range(index[6]+4,index[7]):
    #     patients_Diagnosis.append(text[i])
    # print(patients_Diagnosis)
    


    # for i in range(index[7]+4, len(text)):
    #     patients_Future.append(text[i])
    # print(patients_Future)


    # dict = {
    #     'Name': ' '.join(patients_name),
    #     'Address': ' '.join(patients_Address),
    #     'Date': ' '.join(patients_date),
    #     'SSN': ' '.join(patients_ssn),
    #     'History':' '.join(patients_history),
    #     'Ongoing symptoms reported at examination':' '.join(patients_Ongoing),
    #     'Diagnosis opinion and prognosis':' '.join(patients_Diagnosis),
    #     'Future treatment and rehabilitation':' '.join(patients_Future)
    #     }


    

    # print(dict)


    # import json

    # with open('convertReport.txt', 'w') as convert_file:
    #  convert_file.write(json.dumps(dict))







  



    # text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

