a = [10,20,30,40,50]
target = int(input("enter the elements for search:"))
found = False
for i in range(len(a)):
    if target ==a[i]:
        print("found at index:",i)
        found = True
        break
    if found ==False:
        print("not found")