print(""" 
-------------------------------
WELCOME TO CALCULATOR IN PYTHON
-------------------------------\n
""")


print("Enter your First Number:")
input_number = input()
print("Enter your Second Number:")
input_number2 = input()

selcted_number = input("Select your operator: +, -, *, /, %: ")

if selcted_number == "+":
    print("Ÿour Sum Result is")
    result_number = int(input_number) + int(input_number2)
    print(result_number)

if selcted_number == "-":
    print("Ÿour Subtract Result is")
    result_number = int(input_number) - int(input_number2)
    print(result_number)

if selcted_number == "/":
    print("Ÿour Divide Result is")
    result_number = int(input_number) / int(input_number2)
    print(result_number)

if selcted_number == "*":
    print("Ÿour Multiply Result is")
    result_number = int(input_number) * int(input_number2)
    print(result_number)

if selcted_number == "%":
    print("Ÿour Reminder Result is")
    result_number = int(input_number) % int(input_number2)
    print(result_number)