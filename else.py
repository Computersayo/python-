amount=int(input("ENTER THE AMOUNT"))
if amount<1000:
     discount=amount*0.08
     print("DISCOUNT",discount)

elif amount<5000:
 discount=amount*0.10
 print("DISCOUNT",discount)
else:
  discount=amount*0.15
print("DISCOUNT",discount)
print("NET PAY",amount-discount)