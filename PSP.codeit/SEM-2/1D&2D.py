lst = list(map(int, input("Enter Your List : ").split()))
target = int(input("Enter your Target :"))
l, r = 0, len(lst) - 1
while l < r:
    summ = lst[l] + lst[r]
    if summ == target:
        print(l, r)
        break
    elif summ < target:
        l += 1
    elif summ > target:
        r -= 1
    else:
        print("No pair found")