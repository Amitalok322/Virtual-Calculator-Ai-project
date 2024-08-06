import cv2
from cvzone.HandTrackingModule import HandDetector  # Changed the import here

class Button:
    def __init__(self,pos,width,height,value):
        
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value
    def draw(self,img):   
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (225,225,225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (50,50,50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40,self.pos[1]+ 60),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)

    
        
        
    

# Initialize HandDetector

# Webcam setup
cap = cv2.VideoCapture(0) # Fixed the method name here
cap.set(3,1280) #width
cap.set(4,720) #height
detector = HandDetector()

# creating Button
Buttonlistvalues=[['7','8','9','*'],
                  ['4','5','6','-'],
                  ['1','2','3','+'],
                  ['8','/',',','=']]

Buttonlist =[]
for x in range(4):
    for y in range(4):
        xpos=x*100 +800
        ypos=y*100 +150
        Buttonlist.append(Button((xpos, ypos),100,100,Buttonlistvalues[y][x]))
        
# variables
myequation='10+5'
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # 0 means vertically and 1 means horizontally

    # Detect hands
    hands, img = detector.findHands(img)  # Use HandDetector to find hands
    # draw all buttons
    cv2.rectangle(img, (800, 50), (800 + 400, 70 +100), (225,225,225), cv2.FILLED)
    cv2.rectangle(img, (800,50), (800 + 400, 70 +100), (50,50,50), 3)
    for button in Buttonlist:
        button.draw(img)
    
    #check for hands
    if hands:
        lmList =hands[0]['lmList']
        length, info, _, _ = detector.findDistance(lmList[8], lmList[12], img)





    
    #display thr equation/result
    cv2.putText(img, myequation, (810, 120),cv2.FONT_HERSHEY_PLAIN,3,(50,50,50),3) 
   
    # Display the image
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Corrected waitKey and added exit condition
        break

cap.release()
cv2.destroyAllWindows()
