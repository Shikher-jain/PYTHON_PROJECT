print("Enter Two numbers in which you performs Calculation")
        # Performing num1 operation num2
num1=int(input("Enter first digit: "))
num2=int(input("Enter second digit: "))
op=int(input("\nEnter 1 for ADDITION\nEnter 2 for SUBTRACTION\nEnter 3 for MULTIPLICATION\nEnter 4 for FLOAT DIVISION\nEnter 5 for INTEGER DIVISION\nEnter 6 for MODULUS\nEnter 7 for EXPONENT\n"))
calculation={
    1:num1 + num2,
    2:num1 - num2,
    3:num1 * num2,
    4:num1 / num2,
    5:num1 // num2,
    6:num1 % num2,
    7:num1 ** num2
}
print("Ans: ",calculation[op])