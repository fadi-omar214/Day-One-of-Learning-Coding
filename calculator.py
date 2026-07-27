def multiplication(x, y, /): 
    return x * y
  
def addition(x, y, /):
    return x + y

def subtraction(x, y, /):
    return x - y

def division(x, y, /):
    return x / y

while True:
    try:
        first_number = float(input("What is your first number? "))
    except ValueError as error:
        print(error)
        continue
    else:
        operation = input("Choose an operator: +, -, *, /: ")
        
        try:
            second_number = float(input("What is your second number? "))
        except ValueError as error:
            print(error)
        else:
            match operation:
                case '+':
                    answer = addition(first_number, second_number)
                    print(f"{first_number} + {second_number} = {answer}")
                case '-':
                    answer = subtraction(first_number, second_number)
                    print(f"{first_number} - {second_number} = {answer}")
                case '*':
                    answer = multiplication(first_number, second_number)
                    print(f"{first_number} * {second_number} = {answer}")
                case '/':
                    try:
                        answer = division(first_number, second_number)
                        print(f"{first_number} / {second_number} = {answer}")
                    except ZeroDivisionError as error:
                        print(error)
                case _:
                    print("Invalid")