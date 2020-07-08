import os
from datetime import datetime
from flask import Flask,request,render_template

from .config import ROOT_PATH, TIME_FORMAT

app = Flask(__name__)

@app.route('/')
def home():
    #list all images in static folder
    image_names = os.listdir(ROOT_PATH +'/static')
    print(image_names)
    #sort follow date time
    image_names.sort(key=lambda d: datetime.strptime(d,TIME_FORMAT+".jpg"))

    return render_template('index.html', image_names=image_names)

if __name__ == '__main__':
   app.run()