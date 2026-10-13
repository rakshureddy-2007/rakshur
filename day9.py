number = [1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0
for i in range(len(number)):
    if number[i] % 2 == 0:
        print("even number is:", number[i])
        even += 1
    else:
        odd += 1
        print("odd number is:", number[i])
print("Total even numbers:", even)
print("Total odd numbers:", odd)
