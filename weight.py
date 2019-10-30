weight=int(input("enter your weight"))
unit= input('(L) bs or(K)kg')
if unit.upper()=="L":
    convert=weight*0.45
    print(f"your weight is{convert} kilos")
else:
    convert=weigh//0.45
    print(f" your weight is {convert}pounds")
