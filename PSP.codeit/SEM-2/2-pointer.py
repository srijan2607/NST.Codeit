nums = list(map(int, input().split()))
avg = set()
nums.sort()
l , r = 0 , len(nums)-1
while l < r:
    avg.add((nums[l]+nums[r])/2)
    l += 1
    r -= 1
print(len(avg))