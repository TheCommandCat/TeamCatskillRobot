import cv2
import os
import sys
import math
from math import atan2, degrees, radians

# TODO: add comments for more readble code
# remember to change it to your own path!
img = cv2.imread(r"C:\Users\TheCommandCat\Desktop\TeamCatskillRobot\xyProject\board.png")
img = cv2.resize(img, (1920, 1080))

global counter
counter = 1

def draw_angled_rec(x0, y0, width, height, angle, img):

    _angle = angle * math.pi / 180.0
    b = math.cos(_angle) * 0.5
    a = math.sin(_angle) * 0.5
    pt0 = (int(x0 - a * height - b * width),
           int(y0 + b * height - a * width))
    pt1 = (int(x0 + a * height - b * width),
           int(y0 - b * height - a * width))
    pt2 = (int(2 * x0 - pt0[0]), int(2 * y0 - pt0[1]))
    pt3 = (int(2 * x0 - pt1[0]), int(2 * y0 - pt1[1]))

    cv2.line(img, pt0, pt1, (0, 255, 255), 10)
    cv2.line(img, pt1, pt2, (255, 0, 255), 10)
    cv2.line(img, pt2, pt3, (255, 255, 0), 10)
    cv2.line(img, pt3, pt0, (0, 0, 255), 10)

def drawRobot(x, y, angel):
    draw_angled_rec(x, y, 25, 25, angel ,img)

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def draw_circle(event, x, y, flags, param):
    global counter
    global loc
    match(counter):
        case 1:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 15, (0, 0, 0), -1)
                loc = [x,y]
                print("loc:", x, y)
                counter += 1
        case 2:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 15, (255, 0, 0), -1)
                cv2.line(img, [loc[0], y], [x, y], (255,0,0), 10)
                cv2.line(img, [x, y], loc, (0,255,0), 10)
                cv2.line(img, [loc[0], y], loc, (0,0,255), 10)
                angel = round(getAngle([loc[0], y], [x, y], loc))
                print("angle:", angel)
                drawRobot(loc[0], loc[1], angel)
                counter += 1
        case 3:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 15, (0, 255, 255), -1)
                target = [x, y]
                print("target:", target)
                counter += 1
    if event == cv2.EVENT_MBUTTONDOWN:
        sys.stdout.flush()
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

cv2.namedWindow(winname="Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_circle)

while cv2.waitKey(10) & 0xFF != 27:
    cv2.imshow("Title of Popup Window", img)

cv2.destroyAllWindows()

x = True
while  1:
    if x:
        DoSomthin()
    else: x = False