# Inside app.py
import os
from flask import Flask,request,render_template

from .config import ROOT_PATH
print(ROOT_PATH)
app = Flask(__name__)

@app.route('/')
def home():
    image_names = os.listdir(ROOT_PATH +'/static')
    print(image_names)
    return render_template('index.html', image_names=image_names)

if __name__ == '__main__':
   app.run()