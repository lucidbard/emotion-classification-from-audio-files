import os
from flask import Flask, request
from live_predictions import LivePredictions
# create folder for uploaded data
FOLDER = 'uploaded'
os.makedirs(FOLDER, exist_ok=True)

app = Flask(__name__)


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
                data.save(data.filename)
            live_prediction = LivePredictions(
                file=str(working_dir_path) + "samplemad.wav")  # data.filename)
            print("Initialized")
            result = live_prediction.make_predictions()
            print(result)
    return app.Response(response=result, status=200)


if __name__ == '__main__':
    app.run(port=80)
