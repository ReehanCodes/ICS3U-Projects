# ICS3U Python Submission
# Created by Reehan Chowdhury
# Unit 2


# Function Declarations
def Slope(x1, x2, y1, y2):
    if x1 == x2 == y1 == y2 :
        return ("No Slope")
    if y1 == y2:
        return ("Undefined Slope")
    answer =  (float)(y2-y1)/(x2-x1)
    return answer

def getYInt(x1, x2, y1, y2):
    if x1 == x2 and y1 == y2:
        return ("y=0")
    slope = Slope(x1, x2, y1, y2)
    yInt = -x1*slope+y1
    return (0, yInt)

def getXInt(x1, x2, y1, y2):
    if x1 == x2 == y1 == y2:
        return ("x=0")
    if y1 == y2:
        return("x=",getYInt(x1, x2, y1, y2))
    slope = Slope(x1, x2, y1, y2)
    xInt = -y1/slope+x1
    return (xInt, 0)
# 2
def pointY(x1, y1, yInt,):
    x2 = 0
    y2 = yInt
    slope = (float)(y2-y1)/(x2-x1)
    xInt = -y1/(slope+x1)
    print ("The Equation in y=mx+b format is:", "y =", slope, "x +", yInt)
    print ("The X Intercept: ", xInt)
# 3

def pointX(x1, y1, xInt):
    y2 = 0
    x2 = xInt
    slope = (float)(y2-y1)/(x2-x1)
    yInt = (slope*x1-y1)/1
    print ("The Equation in y=mx+b format is:", "y =", slope, "x +", yInt)
# 4
def pointSlope(x1, y1, slope):
    if slope == 0:
        print("No X-Intercept")
        yInt = y1
        print ("The Equation in y=mx+b format is:", "y =",yInt)
    else:
        yInt = (slope*x1 - y1)/-1
        xInt = -yInt/slope
        print ("The Equation in y=mx+b format is:", "y =", slope, "x +", yInt)
        print("The Y-Intercept is: ", yInt)
        print ("The X-Intercept is: ", xInt)

# 5
def twoPOI(b1, b2, slope1, slope2):
    if slope2 == slope1:
        print("Lines are parallel to each other")
    else:
        if  (1/slope2)*(-1) == slope1:
            print("Lines are perpendicular")
        xpoi = (b2-b1)/(slope1-slope2)
        ypoi = slope1*xpoi + b1
        print("The POI of those two lines are: ", (xpoi, ypoi))
        print("The Equation for Line 1 is: " "y = ", slope1, "x + ", b1)
        print("The Equation for Line 2 is: " "y = ", slope2, "x + ", b2)

#Query user for input
print("1: Two Points")
print("2: Point & Y-intercept")
print("3: Point & X-intercept")
print("4: Point & Slope")
print("5: POI Between 2 lines using y=mx+b")
print("Enter Input Here: ")
userInput = int(input())

if userInput == 1:
    x1Input = float(input("Enter First X Value: ")) 
    y1Input = float(input("Enter First Y Value: ")) 
    x2Input = float(input("Enter Second X Value: ")) 
    y2Input = float(input("Enter Second Y Value: ")) 
    print ("The Slope Is : ", Slope(x1Input, x2Input, y1Input, y2Input))
    print ("The Y Intercept Is : ", getYInt(x1Input, x2Input, y1Input, y2Input))
    print ("The X Intercept Is : ", getXInt(x1Input, x2Input, y1Input, y2Input))
    print("The answer in y=mx+b format is: " "y = ", Slope(x1Input, x2Input, y1Input, y2Input), "x +", getYInt(x1Input, x2Input, y1Input, y2Input))

if userInput == 2:
    x1Input = float(input("Enter X Value: "))
    y1Input = float(input("Enter Y Value: "))
    yIntInput = float(input("Enter Y-Intercept (b) Value: "))
    (pointY(x1Input, y1Input, yIntInput))

if userInput == 3:
    x1Input = float(input("Enter X Value: "))
    y1Input = float(input("Enter Y Value: "))
    xIntInput = float(input("Enter X-Intercept Value: "))
    (pointX(x1Input, y1Input, xIntInput))

if userInput == 4:
    x1Input = float(input("Enter X Value: "))
    y1Input = float(input("Enter Y Value: "))
    slopeInput = float(input("Enter Slope (m) Value: "))
    (pointSlope(x1Input, y1Input, slopeInput))

if userInput == 5:
    slopeInput1 = float(input("Enter Line 1 Slope (m) : ")) 
    yIntersection1 = float(input("Enter Line 1 Y-Intercept (b): ")) 
    slopeInput2 = float(input("Enter Line 2 Slope (m) : ")) 
    yIntersection2 = float(input("Enter Line 2 Y-Intercept (b): "))
    (twoPOI(yIntersection1, yIntersection2, slopeInput1, slopeInput2))
    








    
