def fibonacci(number,num1,num2):
    for num in range(number-2):
        fib = num1 + num2
        num1 = num2
        num2 = fib
        print(fib, end=" ")


number=int(input("enter the number :"))
num1=0
num2=1
print(num1,num2,end=" ")
fibonacci(number,num1,num2)
