def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

choice = input("Do you have Celsius or Fahrenheit? (c / f)")

if choice == "c":
    # Convert Celsius to Fahrenheit
    celsius_input = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_input)
    print("Temperature in Fahrenheit:", round(fahrenheit_result))

if choice == "f":
    # Convert Fahrenheit to Celsius
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_input)
    print("Temperature in Celsius:", round(celsius_result))
