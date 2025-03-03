def input_check (promt): # Base input check
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Value Error")

def season_check (user_num):
    seasons = ["Spring","Summer","Autumn","Winter"]
    if 3<=user_num<=5:
        return seasons[0]
    elif 6<=user_num<=8:
        return seasons[1]
    elif 9<=user_num<=11:
        return seasons[2]
    else:
        return seasons[3]

while True:
    user_num=input_check("Enter month >>")
    if 0<user_num<=12:
        print(season_check(user_num))
        break
    else:
        print("wrong month")
