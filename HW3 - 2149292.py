print ("What is your age?")

Age = int( input("Your age: \t") )

if Age > 19:
    print ("You are an Adult")
if 10 < Age <= 19:
    print ("You are a Child")
    print ("You are an also Adolescent")
if 2 <= Age <= 10:
    print ("You are a Child")
if 0 < Age <= 1:
    print ("You are a Child")
    print ("You are an also Infant")
if Age < 0:
    print ("Age cannot be negative.")
    