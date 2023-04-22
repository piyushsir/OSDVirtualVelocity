from flask import Flask, Response, render_template, request


import cv2
global video
video = cv2.VideoCapture(0)
def gen(video):
    while True:
        success, frames=video.read()
        if not success:
            break
        else:
            ret,buffer = cv2.imencode('.jpg', frames)
            frames = buffer.tobytes()
        
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n\r\n')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/TempFunc1')
def BCurl():
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/TempFunc2')
def crun():
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/TempFunc3')
def sqts():
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')


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
    global video
    if request.method == 'POST':
        if request.form.get('stop') == "Done":
            video.release()
            cv2.destroyAllWindows()
    video = cv2.VideoCapture(0)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)