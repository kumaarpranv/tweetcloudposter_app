from flask import Flask, render_template, request,send_file
from controller import *
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/gener/',methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        username = request.form['username']
        tweets = request.form['tweets']
        if tweets == None:
            tweets=1000
        ch = request.form['type']
        tweets=int(tweets)
        #print(username," ",tweets," ",ch)
        
        fname=start(username,tweets,ch)
        return send_file('./static/img/'+fname, attachment_filename=fname)
    return render_template('index.html')
if __name__ == '__main__':
   app.run(debug = True)