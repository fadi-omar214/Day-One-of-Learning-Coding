def fibonacci(end_number):
    a, b = 0, 1
    while a < end_number:
        print(a, end=" ")
        a, b = b, a + b

while True:
    end_number = int(input("Enter the end number for the Fibonacci sequence: "))
    fibonacci(end_number)