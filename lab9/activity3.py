def find_largest():
    # Prompt the user to enter five numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))
    num5 = float(input("Enter the fifth number: "))
    
    # Determine the largest number using if statements
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        largest = num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        largest = num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        largest = num3
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        largest = num4
    else:
        largest = num5
    
    # Display the result
    print(f"The largest number is: {largest}")

# Run the function
find_largest()

    
