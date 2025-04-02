def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def find_largest_number():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    print(f"The largest number is: {max(numbers)}")

def main():
    print("Temperature Converter: Celsius, Fahrenheit, Kelvin")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C/F/K): ").strip().upper()
    
    if unit == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F and {celsius_to_kelvin(temp):.2f}K")
    elif unit == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C and {fahrenheit_to_kelvin(temp):.2f}K")
    elif unit == 'K':
        print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C and {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("Invalid unit! Please enter C, F, or K.")
    
    find_largest_number()

if __name__ == "__main__":
    main()
