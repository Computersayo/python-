balance=int(input("enter your balance "))
fixed_amount=200
if balance>100:
    amount=balance+fixed_amount
    print(amount)
else:
    amount=fixed_amount+ balance * 0.1
    print(amount)