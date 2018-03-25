from flask import Flask
from flask import request, url_for
from flask import render_template
from flask import redirect, Response
import sqlite3
import json
import cv2
from ml.Neural_Network.TrainingNN import NeuralNetwork as NN
# import matplotlib.pyplot
import numpy as np
import os


app = Flask(__name__)

# @app.route("/")
# @app.route('/<imagename>', methods=['POST', 'GET'])
# def mainpage(imagename=None):
#     if request.method == 'GET':
        
#         if imagename:
#             imgname=(imagename,)
#             con = sqlite3.connect('Image.db')
#             cur = con.cursor()
#             cur.execute("SELECT * FROM Image WHERE imgname=?", imgname)
#             rows = cur.fetchall()
#             if rows:
#                 for row in rows:
#                     imgname = row[0]
#                     imgdata = row[1]
#                 return render_template('paint.html', saved=imgdata)
#             else:
#                 resp = Response("""<html> <script> alert("Image not found");document.location.href="/" </script> </html>""")
#                 return resp
#         else:
#             return render_template('paint.html')
#     if request.method == 'POST':
#         print('SAAAVING STUUUFs')
#         imgname=request.form['imagename']
#         imgdata=request.form['string']
#         data=(imgname, imgdata)
#         con = sqlite3.connect("Image.db")
#         cur=con.cursor()
#         cur.execute("CREATE TABLE IF NOT EXISTS Image(imgname text, imgdata string)")
#         cur.execute("INSERT INTO Image VALUES(?, ?)", data)
#         con.commit()
#         con.close()
#         resp = Response("saved")
#         return resp


@app.route('/', methods=['POST', 'GET'])
def savingImage():
    if request.method == 'GET':
        return render_template('paint.html')
    if request.method == 'POST':
        # 1) Get data from post form
        data = request.form
        # data is  class 'werkzeug.datastructures.ImmutableMultiDict'
        new_data = data.keys()  # one of the key is our canvas rgb
        for ke in new_data:
            lst = ke[1:-1].split(',')  #key is string with square brackets separated by comma
        np_arr = np.array(lst, dtype=int)  #create np array and convert data type to intiger
        # BOGDAN FIXME: need to canvas width and height dynamically?
        np_image = np_arr.reshape([500, 500, 3])  # reshape it to minst

        np_image = np_image.astype(np.uint8) #to avoid error: (-215) depth == CV_8U || depth == CV_16U || depth == CV_32F in function cvtColor

        small_28_by_28 = cv2.resize(np_image, (28, 28), interpolation = cv2.INTER_AREA) # works better, than linear
        rgb = cv2.cvtColor(small_28_by_28, cv2.COLOR_BGR2RGB)  
        gray = cv2.cvtColor(small_28_by_28, cv2.COLOR_BGR2GRAY)
        print(rgb.size)
        print(gray.size)
        cv2.imwrite('np_image_rgb.jpg', rgb)
        cv2.imwrite('np_image_gray.png', gray)
        list_of_predictions = NN().predict_from_ui(gray)
        print(list_of_predictions)

        return 'Done'



if __name__ == '__main__':
    app.debug = True
    app.run()
