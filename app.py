

#even or odd
""" number = int(input("Put a number "))
if number%2 == 0:
    print('even')
else:
    print('odd')
#tip calc
bill = int(input("how much was bill (please gimme tip) "))
service = input("how service (please say great i need this money) ")
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
x = int(input("number please "))
y= int(input("second number please"))
gcf = 0
for i in range(1,x+1):
    if x%i == 0 :
        for s in range(1, y+1):
            if y%s == 0:
                if i == s:
                    gcf = i
                    print(gcf)

#discount
def discount(age, isMember, isResident):
        if (age>=65 or age<12) and (isMember == True or isResident == True) :
            print("This person qualify for the discount.")
        else:
            print("This person does not qualify for the discount.")

print(discount(65, False, True)) """
#gcf/
x = int(input("number please "))
y= int(input("second number please "))
factors = []
for i in range(1,x+1) and range(1,y+1):
    if x%i == 0 and y%i == 0:
       factors.append(i)
       
print(f"GCF is {max(factors)}")