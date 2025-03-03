import math

def input_check (promt):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Value Error")
def control (a,b,c):
    if (b+c>a and a+c>b and a+b>c):
        return True
    else:
        return False
def angels (a,b,c):
    alpha=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
    beta=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    gamma=180-alpha-beta
    return alpha,beta,gamma

while True:
    a=input_check("Lenght of side a >>")
    b=input_check("Lenght of side b >>")
    c=input_check("Lenght of side c >>")
    if a>0 and b>0 and c>0:
        break
    else:
        print("Sides can't be negative")
if control (a,b,c) == True:
    alpha,beta,gamma=angels(a,b,c)
    print (f"{round(alpha,2)}, {round(beta,2)}, {round(gamma,2)}")
else:
    print ("Triangle is impossible")