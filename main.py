import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av #strealing video library
import tensorflow as tf

st.title('Streamlit App Test')
st.write('Hello world')

face_detection = cv2.CascadeClassifier('facial-expression-recognition/haar_cascade_face_detection.xml')

# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
settings = {
	'scaleFactor': 1.3, 
	'minNeighbors': 5, 
	'minSize': (50, 50)
}

labels = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad']

model = tf.keras.models.load_model('facial-expression-recognition/network-5Labels.h5')

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # ret, img = camera.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected = face_detection.detectMultiScale(gray, **settings)

        for x, y, w, h in detected:
            cv2.rectangle(img, (x, y), (x+w, y+h), (245, 135, 66), 2)
            cv2.rectangle(img, (x, y), (x+w//3, y+20), (245, 135, 66), -1)
            face = gray[y+5:y+h-5, x+20:x+w-20]
            face = cv2.resize(face, (48,48)) 
            face = face/255.0

            predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax()
            state = labels[predictions]
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,state,(x+10,y+15), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
            
        # cv2.imshow('Facial Expression', img)
        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_processor_factory=VideoProcessor)