
from cv2 import cv2
import numpy as np 
import sqlite3
import os

# Insert or update Id, name
def insertOrUpdate(id, name):

    conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\Pythontime\Project 1 Opencv_FaceRecog\dataFace.db")

    query = "SELECT * FROM people WHERE ID="+ str(id)
    cursor = conn.execute(query) 

    isRecordExist = 0

    for row in cursor:
        isRecordExist = 1

    if(isRecordExist == 0):
        query = "INSERT INTO people(ID, Name) VALUES(" +str(id)+ ",'"+ str(name) +"')"
    else :
            query = "UPDATE people SET Name='"+str(name)+"' WHERE ID=" +str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

#Load thư viện opencv/ Load opencv

face_cascade = cv2.CascadeClassifier("C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #Truy cập camera

#Cho người dùng nhập từ bàn phím vào id và name, insert to Database/ Input id and name from keyboard
id = input("Enter your ID: ")
name = input("Enter your Name: ")
insertOrUpdate(id,name)

#Lấy dữ liệu từ camera / input data from your camera

sampleNum = 0

while(True):
    ret, frame = cap.read() 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Đổi màu từ RGB sang màu xám / Change color from RGB to Gray

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')
        
        sampleNum += 1 

        cv2.imwrite('dataSet/User.'+str(id) +'.' + str(sampleNum) +'.jpg', gray[y: y+h, x: x+w])

    cv2.imshow('frame', frame) #show ảnh lên / Show picture
    cv2.waitKey(1) #Bật lên không bị tắt luôn / Open the window and it will not turn off immediately

    if sampleNum > 100 :
        break

#Chụp ảnh xong tự đóng cửa sổ / Finish and turn off window
cap.release()
cv2.destroyAllWindows()