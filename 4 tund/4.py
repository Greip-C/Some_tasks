def input_check (promt): # Base input check
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Value Error")

def year_check (user_num):
    if isinstance((user_num/4),int):
        return("Year divided by 4")
    else:
        return("Year can,t be divided by 4")

user_num= input_check("Input year >>")
print(year_check(user_num))