from flask import Flask, Response, render_template, request
import BicepCurl as curl
import Squats as sq
import crun as cr
import stch as st

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/TempFunc1')
def BCurl():
    return Response(curl.main(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/TempFunc2')
def crun():
    return Response(cr.main(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/TempFunc3')
def sqts():
    return Response(sq.main(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/TempFunc4')
def strch():
    return Response(st.main(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Stretching')
def Stretching():
    return render_template('pg5.html')

@app.route('/BicepCurls')
def BicepCurls():
    return render_template('pg2.html')

@app.route('/Crunches')
def Crunches():
    return render_template('pg3.html')

@app.route('/Squats')
def Squats():
    return render_template('pg4.html')


@app.route('/requests', methods=['POST', 'GET'])
def killCam():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)