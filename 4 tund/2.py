import math

def input_check (promt): # Base input check
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Value Error")
def time_calc (user_input): #First version
    if user_input<=60 and user_input>=0:
        time = [00,00,user_input]
    else:
        min=user_input/60
        if len(str(min))==1:
            time =[00,min,00]
        elif isinstance(min,float) and min<=60 and min>=0:
            min= math.floor(user_input/60)
            sec= int(user_input-(min*60))
            time =[00,min,sec]
        elif min>60:
            hour=min/60
            if isinstance(hour,int):
                min= math.floor(user_input/60)-(hour*60)
                sec= int(user_input-(min*60)-(hour*60*60))
                time=[hour,min,sec]
            elif isinstance(hour,float):
                hour= math.floor(min/60)
                min= math.floor(user_input/60)-(hour*60)
                sec= int(user_input-(min*60)-(hour*60*60))
                time = [hour,min,sec]
    return time
def time_calc2 (user_input): #Second version
    if 0 <= user_input < 60:
        return [0, 0, int(user_input)]
    else:
        minutes = math.floor(user_input / 60)
        seconds = int(user_input % 60)

        if minutes < 60:
            return [0, minutes, seconds]
        else:
            hours = math.floor(minutes / 60)
            minutes = minutes % 60
            return [hours, minutes, seconds]

user_input= input_check("Enter sec >>")
time=time_calc(user_input)
print(f"{time[0]}:{time[1]:02}:{time[2]:02}")
