number = [10,20,30,40,50]
unique = list(set(number))
first = second = third = float('-inf')
for num in unique:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num
print("the third largest number is:", third)    