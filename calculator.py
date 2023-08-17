print("This is a simple calculator program")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("Please enter your choice of operations like 1 for + , 2 for - , 3 for *, 4 for / : ")

choice = int(input("Enter the operation you want to perform : "))

if choice == 1 :
    print("This is addition operation: " ,num1+num2)

elif choice == 2:
    print("This is subtraction operation: " ,num1-num2)

elif choice == 3:
    print("This is multiplication operation: " ,num1*num2)

elif choice == 4:
    print("This is division operation: " ,num1/num2)


