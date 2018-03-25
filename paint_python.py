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
        return render_template('paint.html')
    if request.method == 'POST':
        # 1) Get data from post form
        data = request.form.get('jsarr')
        lst = data[1:-1].split(',')

        np_arr = np.array(lst, dtype=int)  #create np array and convert data type to intiger
        # BOGDAN FIXME: need to canvas width and height dynamically?
        np_image = np_arr.reshape([400, 400, 3])  # reshape it to minst

        np_image = np_image.astype(np.uint8) #to avoid error: (-215) depth == CV_8U || depth == CV_16U || depth == CV_32F in function cvtColor

        small_28_by_28 = cv2.resize(np_image, (28, 28), interpolation = cv2.INTER_AREA) # works better, than linear
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


if __name__ == '__main__':

    app.debug = True
    app.run()
