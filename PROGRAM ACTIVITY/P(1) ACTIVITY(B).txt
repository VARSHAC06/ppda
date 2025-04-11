def temperature_converter():
    print("Temperature Converter")
    
    temp = float(input("Enter temperature: "))
    print("Convert from: 1. Celsius 2. Fahrenheit 3. Kelvin")
    from_unit = input("Choose (1/2/3): ")
    print("Convert to: 1. Celsius 2. Fahrenheit 3. Kelvin")
    to_unit = input("Choose (1/2/3): ")

    if from_unit == '1':  # Celsius
        if to_unit == '1': print(f"{temp}C = {temp}C")
        elif to_unit == '2': print(f"{temp}C = {(temp * 9/5) + 32}F")
        elif to_unit == '3': print(f"{temp}C = {temp + 273.15}K")
    
    elif from_unit == '2':  # Fahrenheit
        if to_unit == '1': print(f"{temp}F = {(temp - 32) * 5/9}C")
        elif to_unit == '2': print(f"{temp}F = {temp}F")
        elif to_unit == '3': print(f"{temp}F = {(temp - 32) * 5/9 + 273.15}K")
    
    elif from_unit == '3':  # Kelvin
        if to_unit == '1': print(f"{temp}K = {temp - 273.15}C")
        elif to_unit == '2': print(f"{temp}K = {(temp - 273.15) * 9/5 + 32}F")
        elif to_unit == '3': print(f"{temp}K = {temp}K")
    else:
        print("Invalid Input")

temperature_converter()
