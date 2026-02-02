


values = [1,2.23,5,4,2,30,15]
for x in values: 
    print(x)
print(values[0])
print(values[6])


number = int(input("Put a number"))
if number%2 == 0:
    print('even')
else:
    print('odd')

bill = int(input("how much was bill (please gimme tip)"))
service = input("how service (please say great i need this money)")
if service == "great" or "10/10":
    print(bill*1.25)
elif service == "good" :
    print(bill*1.2)
elif service == "okay" :
    print(bill*1.15)
elif service == "bad" :
    print(bill*1) 
elif service == "perfect" :
    print(bill*2)
else: 
    print("what the hell man no tip?")

number1 = int(input("number please"))
x = number1
factor = x
print(x)