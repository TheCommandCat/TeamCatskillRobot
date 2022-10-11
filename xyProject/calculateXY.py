import cv2
import os
import sys
import math
from math import atan2, degrees, radians


img = cv2.imread(r"C:\Users\Gilad\Desktop\TeamCatskillRobot-main\TeamCatskillRobot\xyProject\board.png")
img = cv2.resize(img, (960, 540))

global counter
counter = 1


def get_angle(point_1, point_2): #These can also be four parameters instead of two arrays
    angle = atan2(point_1[1] - point_2[1], point_1[0] - point_2[0])
    
    #Optional
    angle = degrees(angle)
    
    # OR
    angle = radians(angle)
    
    return angle

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
                print("counter:", counter)
        case 2:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 15, (255, 0, 0), -1)
                cv2.line(img, [loc[0], y], [x, y], (255,0,0), 10)
                cv2.line(img, [x, y], loc, (0,255,0), 10)
                cv2.line(img, [loc[0], y], loc, (0,0,255), 10)
                angelB = round(getAngle([loc[0], y], [x, y], loc))
                print("angleB:", angelB)
                drawRobot(x, y, angelB)
        case 3:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 15, (0, 255, 255), -1)
                target = [x, y]
                print("target:", x, y)
                counter += 1
    if event == cv2.EVENT_MBUTTONDOWN:
        sys.stdout.flush()
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

cv2.namedWindow(winname="Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_circle)

while cv2.waitKey(10) & 0xFF != 27:
    cv2.imshow("Title of Popup Window", img)

    # if cv2.waitKey(10) & 0xFF == 27:
    #     break

cv2.destroyAllWindows()