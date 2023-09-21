# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:24:32 2021

@author: myung
pip install face_recognition


face_recognition.py 파일 사용하면 않된다 
파일명을 다른 이름으로 한다


"""

import face_recognition
import cv2
import numpy as np
import os

#member img 만든다 
member_face_encodings = []
member_names=[]
dirname = 'member'
files = os.listdir(dirname)
for filename in files:
    name, ext = os.path.splitext(filename)
    if ext == '.png':
        member_names.append(name)
        pathname = os.path.join(dirname, filename)
        img = face_recognition.load_image_file(pathname)
        face_encoding = face_recognition.face_encodings(img)[0]
        member_face_encodings.append(face_encoding)



video_capture = cv2.VideoCapture(0)
while True:
   
    ret, frame = video_capture.read()

   
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(member_face_encodings, face_encoding)
    
        name = "Unknown"
    
        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]
    
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(member_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = member_names[best_match_index]
        print(name)
    
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
        # Draw a label with a name below the face
        labelimg=cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(labelimg, name, (left, bottom - 35+15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
