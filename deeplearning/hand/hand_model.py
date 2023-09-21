from mediapipe import solutions
import numpy as np
import cv2
import math
from PIL import ImageFont, ImageDraw, Image
import random

'''


"""
2023-08  mediapipe를 이용한 opencv project


1) annaconda prompt : anaconda 2023.03.0

2) pip install opencv-python  -----> ok

3) python -m pip install mediapipe --user  --- ok
   !!!!   python -m pip install mediapipe --user
   인데 import에서  error 난다
4)  #######  install 후에 spyder를 리쎗하니 됬다


camera class를 이용  가위 바위 보 계산함 
cv2.flip 을 사용 하였는데 화면이 조금 안정된듯함 
!!!!!  재시작하는 방법 해야함 !!!!


"""



'''

index = [[6,8],[10,12],[14,16],[18,20]]
open = [False, False, False, False]
handModel=[[True, False, False, False], #  가위
       [True, True, False, False], #  가위
       [False, False, False, False],  #바위
       [True, True, True, True]   #보
       ];


name=["가위","가위",  "바위", "보"]
randomName=["가위","바위", "보"]
b,g,r,a = 255,255,255,0
fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 30)

mp_drawing = solutions.drawing_utils
mp_drawing_styles = solutions.drawing_styles
mp_hands = solutions.hands

def dist(x1, y1, x2, y2):  #손가락 마디에 거리측정으로  가위바위보 확인
    #print(math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2)))
    return math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))




def win(na, comp) :
    match na:
        case '가위' :
            if comp == '보' :
                return "이겼다"
            elif comp == '바위' :
                return "졌다"
            else :  return "비겼다"
        case '바위' :
            if comp == '보' :
                return "졌다"
            elif comp == '가위' :
                return "이겼다"
            else :  return "비겼다"
        case '보' :
            if comp == '가위' :
                return "졌다"
            elif comp == '바위' :
                return "이겼다"
            else :  return "비겼다"

            





class camera(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        #self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        #self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        self.cam.release()

    def get_frame(self):
        ret, frame = self.cam.read()
        return frame;
tempname=""
returnchk=False
# test
if __name__ == '__main__':
    cam = camera()
   
    while True:
        img = cam.get_frame()
         
        
        h,w,c = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = mp_hands.Hands().process(imgRGB)
    
        if results.multi_hand_landmarks:
                
                for hand_landmarks in results.multi_hand_landmarks:
                   
                    
                   
                    mp_drawing.draw_landmarks(
                        img,     #video image
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())    #손에 위치 표시
                        # kernel reset 이 된다
                   
                    for i in range(0, 4) :
                        open[i]=dist(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y,
                                     hand_landmarks.landmark[index[i][0]].x, hand_landmarks.landmark[index[i][0]].y) <  \
                                dist(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y,                           
                                     hand_landmarks.landmark[index[i][1]].x, hand_landmarks.landmark[index[i][1]].y)
                        #print(open)
    
                    text_x = (hand_landmarks.landmark[0].x*w)
                    text_y = (hand_landmarks.landmark[0].y*h)
                  
                    for i in range(0, 4) :  #len(handModel )  
                        #if (handModel[0][i] !=open[i] || handModel[1][i] !=open[i] || handModel[2][i] != open[i]) :
                        if (handModel[i]==open) :     #가위 바위보중 선택이되면
                            tempname=name[i]
                            img_pil = Image.fromarray(img)
                            draw = ImageDraw.Draw(img_pil)
                            draw.text((60, 70), "나:"+tempname, font=font, fill=(b,g,r,a))
                            img = np.array(img_pil)
                            #cv2.imshow('frame', img)
                            
                            if cv2.waitKey(1) & 0xFF == ord('a'):
                                    comp=randomName[random.randrange(0,3)]
                                    print("나",tempname)
                                    print("computer(random):"+comp)
                                    print("결과:"+win(tempname,comp))
                                    returnchk=True
                                    break
                            '''aaq
                            cv2.putText(img, handModel[i][5], (round(text_x)-50, round(text_y)-250),
                                        cv2.FONT_HERSHEY_PLAIN, 4,(0,0,0),4)
                            '''
                            
                            #print(handModel[i])
                               
        cv2.imshow('frame', img)
        
        if returnchk:
            break              
        if cv2.waitKey(1) & 0xFF == ord('q'):
                comp=randomName[random.randrange(0,3)]
                print("나",tempname)
                print("computer(random):"+comp)
                print("결과:"+win(tempname,comp))
                break

#   cv2.destroyAllWindows()


cv2.destroyAllWindows()
