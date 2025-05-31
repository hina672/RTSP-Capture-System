from flask import Flask, render_template, Response, request, send_file
import cv2
import os
import time
import pandas as pd
from datetime import datetime

app = Flask(__name__)

rtsp_url = "rtsp://admin:123456@192.168.1.188/stream1"
save_dir = "saved_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(rtsp_url)
last_captured_frame = None  

def generate_frames():
    global last_captured_frame
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            last_captured_frame = frame 
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/capture', methods=['POST'])
# def capture():
#     global last_captured_frame
#     if last_captured_frame is not None:
#         # filename = os.path.join(save_dir, f"{int(time.time())}.png")
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         filename = os.path.join(save_dir, f"{timestamp}.png")

#         cv2.imwrite(filename, last_captured_frame)
#         return {'status': 'success', 'filename': filename}
#     return {'status': 'fail'}, 500

@app.route('/capture', methods=['POST'])
def capture():
    global last_captured_frame
    if last_captured_frame is not None:
        timestamp = int(time.time())
        filename = f"{timestamp}.png"
        filepath = os.path.join(save_dir, filename)
        cv2.imwrite(filepath, last_captured_frame)


        log_path = os.path.join(save_dir, "image_log.xlsx")

        if os.path.exists(log_path):
            df = pd.read_excel(log_path)
        else:
            df = pd.DataFrame(columns=["Image Name", "Image Path", "Timestamp"])

        new_entry = pd.DataFrame([{
            "Image Name": filename,
            "Image Path": filepath,
            "Timestamp": pd.to_datetime(timestamp, unit='s')
        }])

 
        df = pd.concat([df, new_entry], ignore_index=True)

        df.to_excel(log_path, index=False)

        return {'status': 'success', 'filename': filename}
    
    return {'status': 'fail'}, 500


@app.route('/snapshot')
def snapshot():
    global last_captured_frame
    if last_captured_frame is not None:
        ret, buffer = cv2.imencode('.jpg', last_captured_frame)
        return Response(buffer.tobytes(), mimetype='image/jpeg')
    return "No snapshot", 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)



