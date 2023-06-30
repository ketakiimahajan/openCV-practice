import cv2
import threading
from flask import Flask, Response

# Image frames sent to the Flask object
global video_frame1, video_frame2
video_frame1 = None
video_frame2 = None

# Use locks for thread-safe viewing of frames in multiple browsers
global thread_lock
thread_lock = threading.Lock()

# Create the Flask object for the application
app = Flask(__name__)

def captureFrames():
    global video_frame1, video_frame2, thread_lock

    # Video capturing from OpenCV
    video_capture1 = cv2.VideoCapture(0)
    video_capture2 = cv2.VideoCapture(1)

    while True and video_capture1.isOpened() and video_capture2.isOpened():
        return_key1, frame1 = video_capture1.read()
        return_key2, frame2 = video_capture2.read()
        
        if not return_key1 or not return_key2: #??????
            break

        # Create copies of the frames and store them in the global variables,
        # with thread-safe access
        with thread_lock:
            video_frame1 = frame1.copy()
            video_frame2 = frame2.copy()

        if cv2.waitKey(1000) & 0xFF == ord('m'):
            break

    video_capture1.release()
    video_capture2.release()

def encodeFrame():
    global thread_lock
    while True:
        # Acquire thread_lock to access the global video_frame objects
        with thread_lock:
            
            global video_frame1, video_frame2
            if video_frame1 is None or video_frame2 is None: 
                continue

            video_frame1 = cv2.resize(video_frame1, (320, 240))
            video_frame2 = cv2.resize(video_frame2, (320, 240))

            joined_frame = cv2.vconcat([video_frame1, video_frame2])

            return_key, encoded_image = cv2.imencode(".jpg", joined_frame)
            if not return_key:
                continue

        # Output image as a byte array
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encoded_image) + b'\r\n')

@app.route("/")
def streamFrames():
    return Response(encodeFrame(), mimetype="multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
    # Create a thread and attach the method that captures the image frames to it
    process_thread = threading.Thread(target=captureFrames)
    process_thread.daemon = True

    # Start the thread
    process_thread.start()

    app.run("0.0.0.0", port="8000")
