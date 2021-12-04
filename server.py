import os
from flask import Flask, request, Response
from live_predictions import LivePredictions
import sys
import pathlib

working_dir_path = pathlib.Path().absolute()
# create folder for uploaded data
FOLDER = 'uploaded'
os.makedirs(FOLDER, exist_ok=True)

app = Flask(__name__)

if sys.platform.startswith('win32'):
    UPLOADS_PATH = str(working_dir_path) + '\\uploaded\\'
else:
    UPLOADS_PATH = str(working_dir_path) + '/uploaded/'


@app.route('/', methods=['GET', 'POST'])
def index():
    result = "OK"
    if request.method == 'GET':
        return '''<form enctype="multipart/form-data" action="" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="8000000" />
    <input name="uploadedfile1" type="file" /><br />
    <input type="submit" value="Upload File" />
</form>'''

    if request.method == 'POST':
        for field, data in request.files.items():
            print('field:', field)
            print('filename:', data.filename)
            if data.filename:
                data.save(UPLOADS_PATH+data.filename)
            live_prediction = LivePredictions(
                file=UPLOADS_PATH + data.filename)  # data.filename)
            print("Initialized")
            result = live_prediction.make_predictions()
            print(result)
    return result, 200


if __name__ == '__main__':
    app.run(port=80, threaded=False)
    # live_prediction = LivePredictions(file=EXAMPLES_PATH + '03-01-01-01-01-02-05.wav')
    # live_prediction.loaded_model.summary()
    # live_prediction.make_predictions()
    # live_prediction = LivePredictions(file=EXAMPLES_PATH + '10-16-07-29-82-30-63.wav')
    # live_prediction.make_predictions()
