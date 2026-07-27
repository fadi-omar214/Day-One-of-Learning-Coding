def countWords(filename):
    try:
        with open(filename, "r") as file:
            words = file.read()
            print(len(words.split()))
    except FileNotFoundError as error:
        print(error)

while True:
    filename = input("What is your file? ")
    countWords(filename)