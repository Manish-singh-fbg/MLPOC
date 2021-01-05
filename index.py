import cv2
import numpy as np
import face_recognition

print("ayush")

img1 =face_recognition.load_image_file("photo/hrithik1.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 =face_recognition.load_image_file("photo/hrithik3.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

facelocimg1 = face_recognition.face_locations(img1)[0]
encodeimg1= face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1,(facelocimg1[3],facelocimg1[0]),(facelocimg1[1],facelocimg1[2]),(255,0,255),2)

facelocimg2 = face_recognition.face_locations(img2)[0]
encodeimg2= face_recognition.face_encodings(img2)[0]
cv2.rectangle(img2,(facelocimg2[3],facelocimg2[0]),(facelocimg2[1],facelocimg2[2]),(255,0,255),2)

results =face_recognition.compare_faces([encodeimg1],encodeimg2)
facedis = face_recognition.face_distance([encodeimg1],encodeimg2)
cv2.putText(img2,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
print(results,facedis)



cv2.imshow("fuckoff",img1)
cv2.imshow("fuckoff2",img2)
cv2.waitKey(0)