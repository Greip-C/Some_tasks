a=float(input("user number >> "))
def tabel_1 (a):
    print("Korrutustabel. Kordusega for i in range")
    for i in range (1, 11):
        print(f"{a} x {i} = {a*i}")
def tabel_2 (a):
    print("Korrutustabel. Kordusega While True")
    i=1
    while True:
        print(f"{a} x {i} = {a * i}")
        i += 1
        if i == 11:
            break
def tabel_3 (a):
    print("Korrutustabel. Kordusega While tingimus")
    i=1
    while i<= 10:
      print(f"{a} x {i} = {a * i}")
      i += 1
tabel_1(a)
tabel_2(a)
tabel_3(a)