amount=int(input("the amount "))
if amount<1000:
    discount=amount*0.05
    print("DISCOUNT",discount)
    print("NET PAYABLE:", amount - discount)
else:
    amount = amount + 100
    discount=amount*0.04
    print("DISCOUNT",discount)
    print("NET PAYABLE:",amount-discount)