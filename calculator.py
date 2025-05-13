#make calculator using elif
print("what are you want to perform")
print("""1. PRESS 1 FRO ADDITION
"2. PRESS 2 FOR  SUBSTRACTION 
"3. PRESS 3 FOR MULTIPLICATION
"4. PRESS 4 FOR DIVISION
"5. PRESS 5 FOR REMAINDER""")

choice = int(input("Enter  your choice "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    sum = num1 + num2
    print("sum will be:", sum)

elif choice == 2:
    sub = num1 - num2
    print("substraction will be:", sub)

elif choice == 3:
    mul = num1 * num2
    print("multiplication will be:", mul)

elif choice == 4:
    if num2 != 0:
        div = num1 / num2
        print("division will be:", div)
    else:
        print("Error: number Cannot divide by zero!")

else:
    print("Invalid input. Please enter 1, 2, 3, or 4.")