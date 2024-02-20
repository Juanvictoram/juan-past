import cv2

video = cv2.VideoCapture(0)
#ip = "https://192.168.1.5:8080/video"
#video.open(ip) 
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_frontalface_default.xml')


while True:
  check,img = video.read()
  imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  objetos = classificador.detectMultiScale(imgGray,maxSize=(50,50),scaleFactor=1.5)
  #print (objetos)
  for x,y,l,a in objetos:
    cv2.rectangle(img,(x,y),(x+l,x+a),(255,0,0),2)
  
  cv2.imshow("video",img)
  
  cv2.waitKey(1)