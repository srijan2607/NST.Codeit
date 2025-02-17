# # House Robber
# def rob(nums):      
#     def loot(idx=0):
#         if idx >= len(nums):
#             return 0
#         # Loot
#         loot_curr = nums[idx] + loot(idx + 2)
#         # No Loot
#         loot_skip = 0 + loot(idx + 1)
#         # Return the maximum loot value between the two options  (current loot or no loot)  at the current index  idx  in the array nums  nums[idx]  + loot(idx + 2)  for loot  and  loot(idx + 1)  for no loot  to the next index  idx + 1  in the array nums  nums[idx + 1]  + loot(idx +
#         return max(loot_curr, loot_skip)
#     return loot()

n = int(input())
nums = list(map(int,input().split()))

def rob(nums): 
    def loot(idx=0):
        x = nums.pop()
        if idx >= len(nums):
            return 0
        # Loot
        loot_curr = nums[idx] + loot(idx + 2)
        # No Loot
        loot_skip = 0 + loot(idx + 1)
        return max(loot_curr, loot_skip)


    def loot2(idx = 0):
        x = nums.pop()
        nums.append(x)
        if idx >= len(nums):
            return 0
        # Loot
        loot_curr = nums[idx] + loot(idx + 2)
        # No Loot
        loot_skip = 0 + loot(idx + 1)
        return max(loot_curr, loot_skip)
    
    return max(loot(nums), loot2(nums))
print(rob(nums))