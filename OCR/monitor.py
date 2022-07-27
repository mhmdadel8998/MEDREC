import pytesseract
from pytesseract import Output
from functions import *
import time
start_time = time.time()
# image = cv2.imread('Monitor.jpg')


def ocr_core_2(filename):
    """
    This function will handle the core OCR processing of images.
        """


    path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    image_path = filename

    # Opening the image & storing it in an image object\
    image = cv2.imread(image_path)
    


    #image = Image.open(image_path)
    gray = get_grayscale(image)
    #remove_noise[remove_noise < 160] += 50    # Inrease values of pixels (amplification) to make text clearer
    noise = remove_noise(gray)
    noise[noise < 160] += 50    # Inrease values of pixels (amplification) to make text clearer
    thresh = thresholding(noise)
    opening_image = opening(thresh)
    opening_image = 255 - opening_image       # Invert image to be black text on white background
    canny_image  = canny(gray)
    canny_image = canny_image

    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    #custom_config = r'--oem 3 --psm 6'
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    #text = pytesseract.image_to_string(opening_image)
    text = pytesseract.image_to_string(opening_image, config=custom_config)
    #text = pytesseract.image_to_data(opening_image ,output_type=Output.DICT, config=custom_config, lang='eng')



    #print(text[:-1])


    print(text.split())
    text = text.split()
    
    d = {
        'HR_bpm': text[0],
        'Blood_Pressure': text[2],
        'RR_RPM': text[4]
        }

    print(d)

    import json

    with open('convert.txt', 'w') as convert_file:
     convert_file.write(json.dumps(d))


    
    

    # text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return d




print("Process finished of main.py --- %s seconds ---" % (time.time() - start_time))
















# custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
# print(pytesseract.image_to_string(image, config=custom_config))

# custom_config = r'--oem 3 --psm 6 outputbase digits'
# print(pytesseract.image_to_string(image, config=custom_config))

# custom_config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
# pytesseract.image_to_string(img, config=custom_config)


# d = pytesseract.image_to_data(opening ,output_type=Output.DICT, config=custom_config, lang='eng')
# # print(d.keys())

# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(float(d['conf'][i])) > 2:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)



# # display image

# cv2.imshow('captured text',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# saving the captured text in a text file
 
# parse_text = []

# word_list = []

# last_word = ''

# for word in text['text']:

#    if word!='':
#         digitWord = ""    # Create empty string to store new parsed string
#         for s in word:      # Loop through chars in current word
#              if s.isdigit():    # Select only digits in this word
#                  digitWord += s
#         word_list.append(digitWord)
#         last_word = word

# if (last_word!='' and word == '') or (word==text['text'][-1]):

#     parse_text.append(word_list)

# word_list = []



# import csv

# with open('OUTPUT_TEXT.txt',  'w', newline="") as file:

#    csv.writer(file, delimiter=" ").writerows(parse_text)
