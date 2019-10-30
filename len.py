name=input("Enter the name")
if len(name)<3:
    print("name must be more than three charactes")
elif len (name)>25:
    print("name must not exceed 25 characters")
else:
    print("word is the best match")