from datetime import date

def input_check (promt,promt_var,i): # Base input check
    while True:
        try:
            return int(input(str(promt+" "+promt_var[i])))
        except ValueError:
            print("Value Error")

def create_list(promt):
    user_date =[]
    promt_var=["Day >>","Month >>","Year >>"]
    for i in range (0,3):
        user_date.append(input_check(promt,promt_var,i))
    return user_date

def date_check (user_date):
    dates = [31,28,21,20,21,30,31,31,30,30,31]
    if 1> user_date[0] <12:
        print("Wrong day")
        return False
    elif 1>user_date[2]:
        print("Wrong year")
        return False
    try: 
        dates[user_date[1]-1]
        print("Correct Date")
        return True
    except IndexError:
        print("Wrong Month")
        return False

def age_calc(birth_date):
    today=date.today()
    age=today.year-birth_date[2]
    return age

promt =("Enter")
Date_status=False

while Date_status == False:
    user_date =create_list(promt)
    Date_status =date_check (user_date)
age =age_calc(user_date)
print(age)
