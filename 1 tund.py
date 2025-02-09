user_num_a = float(input('input lenght a >> '))
user_num_b = float(input('input lenght b >> '))
pi = 3.14

def c_calc(user_num_a,user_num_b):
    c = (user_num_a**2+user_num_b**2)**(1/2)
    print ("c_calc=",c)
    return c

def S_calc(user_num_a,user_num_b):
    S = 1/2*user_num_a*user_num_b
    print ("S_calc=",S)
    return S

def P_calc(user_num_a,user_num_b):
    c = c_calc(user_num_a,user_num_b)
    P = user_num_a + user_num_b + c
    print("P_calc=", P)
    return P

def r_calc(user_num_a,user_num_b):
    S = S_calc(user_num_a,user_num_b)
    P = P_calc(user_num_a,user_num_b)
    r = (2*S) / P
    print("r_calc=", r)
    return r

def Sr_calc(pi,r):
    Sr = pi*r**2
    print("Sr_calc=", Sr)
    return Sr

S = round(S_calc(user_num_a,user_num_b),2)
r = r_calc(user_num_a,user_num_b)
print("r= ",r)
Sr = round(Sr_calc(pi,r),2)

print ("Rounded rea of a triangle S= ",S)
print ("Rounded area of the inner circle Sr= ",Sr)
breakpoint