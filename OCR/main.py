import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# import our OCR function
from ocr_core import *
from monitor import *
import time
start_time = time.time()


# define a folder to store and later serve the images
cwd = os.getcwd()

UPLOAD_FOLDER = cwd+'/static'
UPLOAD_FOLDER_2 = cwd+'/Medical'


# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_2'] = UPLOAD_FOLDER_2
# function to check the file extension


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page1():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            extracted_text = ocr_core(UPLOAD_FOLDER + '/' + filename)
            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=filename)
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/uploadMed', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('uploadMed.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('uploadMed.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_2'], filename))
            extracted_text = ocr_core_2(UPLOAD_FOLDER_2 + '/' + filename)
            # extract the text and display it
            return render_template('uploadMed.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=filename)
    elif request.method == 'GET':
        return render_template('uploadMed.html')




print("Process finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    app.run()
