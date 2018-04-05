from flask import Flask
from flask import request, url_for
from flask import render_template
from flask import redirect, Response, flash
import sqlite3
import json
import cv2
from ml.Neural_Network.TrainingNN import NeuralNetwork as NN
# import matplotlib.pyplot
import numpy as np
import os


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/', methods=['POST', 'GET'])
def savingImage():
    if request.method == 'GET':
        colors = ['white', 'red', 'green', 'blue', 'yellow', 'pink',
                  'purple', 'violet', 'black', 'orange']
        return render_template('paint.html', colors_lst=colors)
    if request.method == 'POST':
        # 1) Get data from post form
        data = request.form.get('jsarr')
        lst = data[1:-1].split(',')

        # create np array and convert data type to intiger
        np_arr = np.array(lst, dtype=int)
        # BOGDAN FIXME: need to canvas width and height dynamically?
        np_image = np_arr.reshape([400, 400, 3])  # reshape it to minst

        # to avoid error: (-215) depth == CV_8U || depth == CV_16U || depth == CV_32F in function cvtColor
        np_image = np_image.astype(np.uint8)

        # works better, than linear
        small_28_by_28 = cv2.resize(
            np_image, (28, 28), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(small_28_by_28, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(small_28_by_28, cv2.COLOR_BGR2GRAY)
        print(rgb.size)
        print(gray.size)
        cv2.imwrite('np_image_rgb.jpg', rgb)
        cv2.imwrite('np_image_gray.png', gray)
        list_of_predictions = NN().predict_from_ui(gray)
        print('Number is:', list_of_predictions[1])
        # after_this_request(render_template('query_result.html'))
        # print(url_for(prediction_result))

        # return 'done'
        # redirect('/result/')
        # return after_this_request(redirect('/result/'))
        # return redirect('/result/')
        # flash('Is it flassshed?')
        # return render_template('query_result.html')
        # return list_of_predictions
        return str(list_of_predictions[1])


@app.route('/result/')
def prediction_result():
    flash('hahahahs')
    return render_template('query_result.html')
    return 'done'


@app.route('/animations')
def test_animations():
    return render_template('animations_test.html')


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':

    app.debug = True
    app.run()
