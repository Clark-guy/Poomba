from flask import Flask, render_template_string, Request, Response
from picamera2 import Picamera2
import cv2, serial, time


ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=115200,
        timeout=1
)

ser.write(bytes([128]))
time.sleep(0.1)
ser.write(bytes([131]))
time.sleep(0.1)

song = [
        140, 0, 11,
        60, 32,
        69, 32,
        67, 32,
        64, 16,
        60, 16,
        62, 16,
        64, 16,
        62, 16,
        60, 16,
        57, 32,
        55, 32]

picam2 = None

def getCamera():
  global picam2
  if picam2 is None:
    picam2= Picamera2()
    picam2.configure(picam2.create_preview_configuration())
    picam2.start()
  return picam2

def generate_frames():
    """Yield JPEG frames for MJPEG streaming"""
    cam=getCamera()
    while True:
        frame = cam.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route('/')
def hello_world():
  return render_template_string('''Hi James World!\n

  <img src="{{ url_for('video') }}" width="640" height="480" />
  <div>
    <button onclick="sendCommand()">Send Serial</button>
    <button onclick="goForward()">Go Forward</button>
    <button onclick="goBackwards()">Go Backwards</button>
    <button onclick="turnLeft()">Turn Left</button>
    <button onclick="turnRight()">Turn Right</button>
    <button onclick="reset()">Reset</button>
    <button onclick="dock()">Dock</button>
  </div>


  <script>
  function sendCommand() {
    fetch("/sing", { method: "POST" });
      //.then(response => response.text())
      //.then(data => alert(data));
  }
  function reset() {
    fetch("/reset", { method: "POST" });
  }
  function dock() {
    fetch("/dock", { method: "POST" });
  }


  function goForward() {
    fetch("/forward", { method: "POST" });
  }
  function goBackwards() {
    fetch("/backwards", { method: "POST" });
  }
  function turnLeft() {
    fetch("/left", { method: "POST" });
  }
  function turnRight() {
    fetch("/right", { method: "POST" });
  }
  </script>
  ''')


@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/dock", methods=["POST"])
def dock():
    ser.write(bytes([143]))
    print('docking')
    time.sleep(5)
    return "", 204


@app.route("/reset", methods=["POST"])
def reset():
    ser.write(bytes([7]))
    print('resetting')
    time.sleep(1)
    ser.write(bytes([128]))
    return "", 204


@app.route("/sing", methods=["POST"])
def sing():
    ser.write(bytes(song))
    time.sleep(0.1)
    ser.write(bytes([141,0]))
    print('running song')
    time.sleep(5)

    return "", 204

@app.route("/forward/start", methods=["POST"])
def forward_start():
    ser.write(bytes([145,0x00,0x64,0x00,0x64]))
    return "", 204

@app.route("/forward/stop", methods=["POST"])
def forward_stop():
    ser.write(bytes([145,0x00,0x00,0x00,0x00]))
    return "", 204

@app.route("/forward", methods=["POST"])
def forward():
    ser.write(bytes([145,0x00,0x64,0x00,0x64]))
    time.sleep(2)
    ser.write(bytes([145,0x00,0x00,0x00,0x00]))
    time.sleep(2)
    return "", 204

@app.route("/backwards", methods=["POST"])
def backwards():
    ser.write(bytes([145,0x00,0x64,0x00,0x64]))
    time.sleep(2)
    ser.write(bytes([145,0x00,0x00,0x00,0x00]))
    time.sleep(2)
    return "", 204

@app.route("/left", methods=["POST"])
def left():
    ser.write(bytes([145,0x00,0x64,0x00,0x00]))
    time.sleep(1)
    ser.write(bytes([145,0x00,0x00,0x00,0x00]))
    time.sleep(2)
    return "", 204

@app.route("/right", methods=["POST"])
def right():
    ser.write(bytes([145,0x00,0x00,0x00,0x64]))
    time.sleep(1)
    ser.write(bytes([145,0x00,0x00,0x00,0x00]))
    time.sleep(2)
    return "", 204

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True)