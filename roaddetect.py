import cv2 as cv
import numpy as np
import matplotlib.pylab as ptb

vid=cv.VideoCapture("D:\\Python Projects\\road3.mp4")
while True:
    istrue,img=vid.read()

    # img=cv.imread("D:\\Python Projects\\road.jpg")
    grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT)

    blank=np.zeros((img.shape[0],img.shape[1]),dtype="uint8")
    rgbimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    # ptb.imshow(img)
    # ptb.show()

    roi=np.array([[0,img.shape[0]],[img.shape[1],img.shape[0]],[0,(img.shape[0]//2)],[(img.shape[1]),(img.shape[0]//2)]],dtype=np.int32)
    roi = roi.reshape((-1, 1, 2))
    mask=cv.rectangle(blank,(0,(img.shape[0]//2)),(img.shape[1],img.shape[0]),255,-1)

    maskedimg=cv.bitwise_and(blur,blur,mask=mask) 
    canny=cv.Canny(maskedimg,100,150)
    contour,hie=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    for i,cnt in enumerate(contour):
        
        peri=cv.arcLength(cnt,False)
        if peri>200:
    # cv.drawContours(img,contour,-1,(100,50,60),thickness=2)

            cv.drawContours(img,cnt,-1,(31,21,239),thickness=2) 
    # lines=cv.HoughLinesP(canny,rho=6,theta=np.pi/60,threshold=110,lines=np.array([]),minLineLength=60)
    # for line in lines:
    #     for x1,y1,x2,y2 in line:
    #         cv.line(img,(x1,y1),(x2,y2),(234,156,134),thickness=1)


    cv.imshow("road",img)

    # cv.waitKey(0)





    if cv.waitKey(20) & 0xFF==ord("d"):
        break

vid.release()
cv.destroyAllWindows()









