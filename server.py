import os
from flask import Flask, request

# create folder for uploaded data
FOLDER = 'uploaded'
os.makedirs(FOLDER, exist_ok=True)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return '''<form enctype="multipart/form-data" action="" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="8000000" />
    <input name="uploadedfile1" type="file" /><br />
    <input name="uploadedfile2" type="file" /><br />
    <input name="uploadedfile3" type="file" /><br />
    <input type="submit" value="Upload File" />
</form>'''

    if request.method == 'POST':
        for field, data in request.files.items():
            print('field:', field)
            print('filename:', data.filename)
            if data.filename:
                data.save(os.path.join(FOLDER, data.filename))
        return "OK"


if __name__ == '__main__':
    app.run(port=80)
