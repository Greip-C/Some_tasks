from math import sin,cos,pi
from sys import exit

def peaprogramm():

    def input_check_f (promt): # Base input check float
            while True:
                try:
                    return float(input(promt))
                except ValueError:
                    print("Sisestamise viga!")
                    exit()

    def input_check_i (promt): # Base input check int
            while True:
                try:
                    return int(input(promt))
                except ValueError:
                    print("Sisestamise viga!")
                    exit()

    def input_comparing_f (): # Input comparing a and b
        def input_check (promt): # Base input check
            while True:
                try:
                    return float(input(promt))
                except ValueError:
                    print("Sisestamise viga!")
                    exit()

        while True:
            Start = input_check("Sisesta vahemiku algus => ")
            End = input_check("Sisesta vahemiku lõpp => ")
            if Start < End:
                break
            else:
                print("Valed andmed")
                exit()
                continue
        return(Start,End)

    def variant_17_2(a, b, n, d): #CALCULATOR!!!

        def n_sort(a,b,n): #Point generator
            step = (b-a)/(n)

            points = tuple(a + i*step for i in range(n+1))

            return(points)
        
        def function_mat(points): #Funcion calculator
            y_output = tuple(
                3*cos((pi*i)/3) + 5*cos(pi*i) if i <= -2 else
                5*sin((pi*i)/2) - 3*sin((2*pi*i)/5) if -2< i < 2 else
                cos(pi*i)+((sin(i**2))/4)
                for i in points
            )
            #print(y_output)
            return(y_output)
        
        def tuple_round(a): #Make tuple rounded
            return tuple(round(i,2) for i in a)

        def d_comparing(t_input,d): #d comparing with Y(x)
            count =0
            for i in range(len(t_input)):
                if t_input[i] < d:
                    count = count+1
            return count


        points=n_sort(a,b,n)

        y_output=function_mat(points)

        r_points=tuple_round(points)
        r_y_output=tuple_round(y_output)

        for i in range(n+1):
            print(f"{r_points[i]} \t {r_y_output[i]}")
        
        if d_comparing(r_y_output,d) == 0:
            print("Vastus on tühi")
        else:
            print("Funktsiooni väärtuste arv, mis on arvust", d ,"väiksem, on", d_comparing(r_y_output,d))

    a,b=input_comparing_f()
    n=input_check_i("Sisesta jaotiste arv => ")
    d=input_check_f("Sisesta mingi reaalarv => ")

    variant_17_2(a,b,n,d)

peaprogramm()