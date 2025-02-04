# # lst1 = list(map(int,input().split()))
# lst1 = [1, 2, 3, 4, 5]
# def sum_of_the_list(i,lst1):
#     if i >= len(lst1):
#         return 0
#     else:
#         return lst1[i] + sum_of_the_list(i+1,lst1)


# def sum_of_no(i,string):
#     if i < len(string):
#         return 0
#     else:
#         return int(string[i]) + sum_of_no(i+1,string)


# print(sum_of_the_list(0,lst1))

# def maxArray(nums):
#     return maxof(0,nums)

# def maxof(index, nums):
#     maxx = nums[index]
#     if index >= len(nums):
#         return maxx
#     elif nums[index] > maxx:
#         maxx = nums[index]
#     return maxof(index+1, nums)
    

# num = int(input())

# def is_power_of_four(num):
#     if num != int(num) or (num < 4 and num < 1 ):
#         return False
#     if num == 4 or num == 1:
#         return True
#     else :
#         return is_power_of_four(num**0.5)

# print(is_power_of_four(num))






# def factorial(n):
#     if n == 0:
#         return 1
#     if n == 1 :
#         return 1
#     else :
#         return n * factorial(n-1)

def rangeSum(L, R):
   if L == R:
       return L
   else:
       return L + rangeSum(L+1, R)