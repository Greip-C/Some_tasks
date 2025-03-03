def input_check (promt,i): # Base input check
    while True:
        try:
            return float(input(f"{i+1}. {promt}"))
        except ValueError:
            print("Value Error")

def create(promt):
    group =[]
    for i in range (0,3):
        group.append(input_check(promt,i))
    return group

group =create("Enter value >> ")
group.sort()
print(*group)