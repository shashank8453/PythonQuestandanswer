number1=6
number2=12
list_number1=[]
list_number2=[]
for i in range (1,number2+1):
    lcd1=number1*i
    list_number1.append(lcd1)
print(list_number1)

for i in range (1,number1+1):
    lcd2=number2*i
    list_number2.append(lcd2)
print(list_number2)

for i in list_number1:
    for j in list_number2:
        if i==j:
            print(i)
        break

