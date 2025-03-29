import sys
def variant_17_1():
    
    def input_comparing (): # Input comparing
        def input_check (promt): # Base input check
            while True:
                try:
                    return int(input(promt))
                except ValueError:
                    print("Sisestamise viga!")
                    sys.exit()

        while True:
            Start_Year = input_check("Sisestage vahemiku algus aasta => ")
            End_Year = input_check("Sisestage vahemiku lõpuaasta => ")
            if Start_Year <= End_Year and Start_Year!=0 and End_Year!=0:
                break
            else:
                print("Algus peab olema väiksem, kui lõpp!")
                sys.exit()
                continue
        return(Start_Year,End_Year)

    def Year_check(Start_Year,End_Year): #Year divide check
        Chosen_one= tuple(Year for Year in range(Start_Year, End_Year +1)
            if Year % 4 !=0)
        return Chosen_one

    Start_Year,End_Year = input_comparing()

    Chosen_one=Year_check(Start_Year,End_Year)
    print("Leitud aastad:",Chosen_one)
    print("Antud aastate vahemikus on",len(Chosen_one),"mitte liigaastat")

variant_17_1()