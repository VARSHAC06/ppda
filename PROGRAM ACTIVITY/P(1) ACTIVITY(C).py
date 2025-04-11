def find_largest():
    print("Find the largest number")
    number = []
    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        number.append(num)
    largest = max(number)
    print(f"The largest number is: {largest}")
find_largest()
