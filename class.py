distance=int(input("ether the distance:"))
unit=input('(m)metres or(cm)centimeters')

if unit.upper()=="m":
    distance1=distance*100
    print(f"the distance covered is{distance1} centimeters")
else:
    distance1=distance/100
    print(f"The distance is {distance1} meters")
