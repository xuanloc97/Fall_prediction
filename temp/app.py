# Inside app.py
import os
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def home():
    image_names = os.listdir('/home/xuanloc/PROJECT/server_django/temp/static')
    print("sss")
    print(image_names)
    return render_template('index.html', image_names=image_names)
	# return "Hello World!"
if __name__ == '__main__':
   app.run()