import time, sys
start = time.time()
squares = [x ** 2 for x in range(1,1000001)]
end = time.time()
print("List comprehension time:",end - start)
print(sys.getsizeof(squares))
