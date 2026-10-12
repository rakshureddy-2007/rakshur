numbers = [20,30,40,50,60]
key = int(input("enter the key to search:"))
for index in range(len(numbers)):
    if numbers[index] ==key:
        print("key found at index",index)
        breake
    else:
        print("key not found")
