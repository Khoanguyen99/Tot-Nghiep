import cv2
import numpy as np 
import os
import sqlite3
from PIL import Image

#training hình ảnh nhận diện với Thư viện nhận diện khuôn mặt

    #Khuôn mặt ở đâu trên cam
face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
    #Khuôn mặt đấy là ai
recognizer = cv2.face.LBPHFaceRecognizer_create()

#Đối chiếu xem khuôn mặt nhận diện trên camera có trong tập dữ liệu đã được học hay không và nếu có thì là ai
recognizer.read(r"C:\Users\ADMIN\Desktop\Pythontime\Project 1 Opencv_FaceRecog\recognizer\trainingData.yml")

#Lấy thông tin bằng id từ database sqlite3
def getProfile(id):

    conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\Pythontime\Project 1 Opencv_FaceRecog\dataFace.db")
    query = "SELECT * FROM People WHERE ID=" +str(id)
    cursor = conn.execute(query)

    #Tạo profile để lưu giá trị lấy được từ database về
    profile = None
    for row in cursor:
        profile = row

    conn.close()
    return profile 

#Nhận diện khuôn mặt ở camera và kết hợp với dữ liệu xem người này là ai?
# Nếu có thì show tên, nếu không thì show Unknow

cap = cv2.VideoCapture(0)

fontface = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    #vẽ hình vuông:
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+ w, y+ h), (0,255,0), 2)

        roi_gray = gray[y: y+h, x: x+ w]

        id,confidence = recognizer.predict(roi_gray) #Nhận diện trên khuôn mặt là ai, có thì trả về ID

        if confidence< 40:
            profile = getProfile(id)
            if (profile != None):
                cv2.putText(frame,"" +str(profile[1]), (x+10, y+h +30), fontface, 1, (0,255,0), 2)

        else: 
            cv2.putText(frame,"Unknown", (x+10, y+h +30),fontface, 1, (0,0,255), 2)
    cv2.imshow('image',frame)

    #Sẽ không bị tắt liền khi mở lên, và chỉ bị ngắt khi dừng chương trình ở python hoặc nhấn "q"
    #Will not turn off immediately Unless you stop python or press "q"
    if(cv2.waitKey(1) == ord('q')):
        break; 

cap.release()
cv2.destroyAllWindows()