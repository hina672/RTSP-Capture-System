# RTSP Camera Stream & Snapshot Web App

This project is a Flask-based web application that streams live video from an RTSP IP camera, allows snapshot capturing, and logs image details in an Excel file. The web interface displays live feeds and snapshot previews, with support for multiple cameras.

## 🚀 Features

- Live RTSP video stream using OpenCV and Flask.
- Snapshot capture from the live stream.
- Stores captured images in a local folder.
- Logs snapshot details (name, path, timestamp) to an Excel file.
- Web-based interface with preview boxes.
- Support for dual-camera capture (extendable).


## 🛠 Technologies Used

- Python 3
- Flask
- OpenCV
- Pandas
- HTML5 / CSS
- RTSP Camera Stream


## 📡 RTSP Camera Setup

Update the RTSP URL in `app.py`:

```python
rtsp_url = "rtsp://admin:123456@192.168.1.188/stream1"
````

Make sure the IP and credentials match your camera configuration.

## ▶️ How to Run

1. **Install Dependencies**

```bash
pip install flask opencv-python pandas openpyxl
```

2. **Run the App**

```bash
python app.py
```

3. **Open in Browser**

Visit: http://127.0.0.1:5000

## 🖼 Capture Snapshots

Click **"Capture Both Snapshots"** to take pictures from both cameras. Snapshots will be saved in the `saved_images/` folder and automatically logged in `image_log.xlsx`.

## 📝 Future Improvements

* Add support for multiple RTSP streams.
* Store logs in a database instead of Excel.
* Add download or email options for snapshots.
* Add authentication for security.

