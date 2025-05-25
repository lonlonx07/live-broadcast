from flask import Blueprint, request, render_template, Response
import cv2

views = Blueprint('views', __name__)
cam_id = ""

@views.route('/')
def home():
    return "Hello World"

def generate_frames():
    camera = cv2.VideoCapture(cam_id)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@views.route('/cam_feed')
def cam_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@views.route('/stream/<cam>', methods=["GET"])
def stream(cam):
    global cam_id
    cam_id = int(cam)
    return render_template('stream.html')