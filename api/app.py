import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from manager import Manager

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}
manager = Manager()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            response = manager(file)
            print(f'save_file_time: {response.get("save_file_time")}')
            print(f'save_convert_time: {response.get("save_convert_time")}')
            print(f'recognition_time: {response.get("recognition_time")}')
            print(f'classification_time: {response.get("classification_time")}')
            print(f'punctuation_time: {response.get("punctuation_time")}')

            print(f'crime: {response["class"].get("crime")}')
            print(f'max_value: {response["class"].get("max_value")}')
            print(f'max_type: {response["class"].get("max_type")}')

            print(f'text: {response.get("text")}')

#            return redirect(url_for('download_file', name=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''
 
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    app.run(
#        host = args.host,
#        port = args.port,
        debug = True
    )
