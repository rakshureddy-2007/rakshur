number = [10,40,50,30,20]
largest = number[0]
second_largest = number[0]
for i in number:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("second largest number is:",second_largest)