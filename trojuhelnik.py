import math
def isTriangle(a:float, b:float, c:float):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def triangleArea(a:float, b:float, c:float):
    if isTriangle(a,b,c):
        s = (a+b+c) /2
        area = s*(s-a)*(s-b)*(s-c)
        return math.sqrt(area)
    else:
        return float("nan")

print(triangleArea(1000, 1, 1))
