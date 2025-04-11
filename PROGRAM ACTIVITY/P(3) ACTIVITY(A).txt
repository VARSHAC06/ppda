Def list_operations():
list = []
while True:
print (""" List operations:""")
print ("1. Insert an element:")
print ("2. Delete an element:")
print ("3. Find an element:")
print ("4. Display the list:")
print ("5. Sort the list:")
print ("6. Reverse the list:")
print ("7. Exit:")
choice = int(input("Enter your choice:"))
if choice == 1:
element = int(input("Enter the element to insert:"))
list.append(element)
print(f"element '{element}' inserted.")
elif choice == 2:
element = int(input("Enter the element to delete:"))
if element in list:
list.remove(element)
print(f"element '{element}' deleted.")
else:
print(f"element '{element}' not found.")
elif choice == 3:
element = int(input("Enter the element to find if element"))
if element in list:
print(f"element '{element}' found.")
else:
print(f"element '{element}' not found.")
elif choice == 4:
print("List elements:", list)
elif choice == 5:
list.sort()
print("List sorted.")
elif choice == 6:
list.reverse()
print("List reversed.")
elif choice == 7:
break
else:
print("Invalid choice.")
close()
