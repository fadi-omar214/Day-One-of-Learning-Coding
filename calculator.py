while True: 
    def multiplication(x, y, /): 
        return x * y
  
    def addition(x, y, /):
        return x + y

    def subtraction(x, y, /):
        return x - y

    def division(x, y, /):
        return x / y

    first_number = float(input("What is your first number? "))
    operation = input("Choose an operator: +, -, *, /: ")
    second_number = float(input("What is your second number? "))

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
            if second_number != 0:
                answer = division(first_number, second_number)
                print(f"{first_number} / {second_number} = {answer}")
            else:
                print("Invalid")
        case _:
            print("Invalid")