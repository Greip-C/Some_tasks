a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
while a==0:
    print("a, can't be null")
    a=float(input("a="))
def dif_calc(a,b,c):
    dif=b**2-4*a*c
    return dif
def calc(dif,a,b,c):
    if dif==0:
        x1=(-b)/(2*a)
        return x1, None
    elif float(dif)>0:
        x1 = (-b + dif**0.5) / (2 * a)
        x2 = (-b - dif**0.5) / (2 * a)
        return x1,x2
    else:
        print ("Negative discriminant value")
        return None, None
dif=float(dif_calc(a,b,c))
print("dif:",dif)
ans1, ans2=calc(dif,a,b,c)
print("x1:",ans1)
print("x2:",ans2)