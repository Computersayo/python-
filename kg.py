weight=int(input("enter your mass"))
unit=input('(K)kgs or (g)')
if unit.upper()=="K":
    mass=weight*1000
    print(f"your mass is{mass}grams")
else:
    mass=weight/1000
print(f"your mass is{mass}kilos")