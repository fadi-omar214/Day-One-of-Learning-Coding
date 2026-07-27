def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32) * (5/9) + 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

def celsius_to_kelvin(celsius):
    return (celsius + 273.15)

def kelvin_to_celsius(kelvin):
    return (kelvin - 273.15)

def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15) * (9/5) + 32

while True:
    try:
        temperature = float(input("What is the temperature? "))
    except ValueError as error:
        print(error)
    else:
        initial_measurement = input("What is it in (C/F/K)? ").upper()
        final_measurement = input("What do you want it to be in (C/F/K)? ").upper()

        if (initial_measurement == "C"):
            if (final_measurement == "K"):
                final_temperature = celsius_to_kelvin(temperature)
                print(f"{temperature}°C is the same as {final_temperature}°K")
            elif (final_measurement == "F"):        
                final_temperature = celsius_to_fahrenheit(temperature)
                print(f"{temperature}°C is the same as {final_temperature}°F")    
            else:
                print("Error")
        elif (initial_measurement == "F"):
            if (final_measurement == "C"):
                final_temperature = fahrenheit_to_celsius(temperature)
                print(f"{temperature}°F is the same as {final_temperature}°C")
            elif (final_measurement == "K"):
                final_temperature = fahrenheit_to_kelvin(temperature)
                print(f"{temperature}°F is the same as {final_temperature}°K")
            else:
                print("Error")
        elif (initial_measurement == "K"):
            if (final_measurement == "C"):
                final_temperature = kelvin_to_celsius(temperature)
                print(f"{temperature}°K is the same as {final_temperature}°C")
            elif (final_measurement == "F"):
                final_temperature = kelvin_to_fahrenheit(temperature)
                print(f"{temperature}°K is the same as {final_temperature}°F")
            else:
                print("Error")
        else:
            print("Error")