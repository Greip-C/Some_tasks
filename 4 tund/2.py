import math

def input_check (promt):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Value Error")

user_input= input_check("Enter sec >>")

def time_calc (user_input):
    if user_input<=60 and user_input>=0:
        time = list[00,00,user_input]
    else:
        min=user_input/60
        if len(str(min))==1:
            time =list[00,min,00]
        elif isinstance(min,float) and min<=60 and min>=0:
            min= math.floor(user_input/60)
            sec= int(user_input-(min*60))
            time =list[00,min,sec]
        elif min>60:
            hour=min/60
            if isinstance(hour,int):
                min= math.floor(user_input/60)-(hour*60)
                sec= int(user_input-(min*60)-(hour*60*60))
                time=list[hour,min,sec]
            elif isinstance(hour,float):
                hour= math.floor(min/60)
                min= math.floor(user_input/60)-(hour*60)
                sec= int(user_input-(min*60)-(hour*60*60))
                time = list[hour,min,sec]
    return time

print(time_calc(user_input))


