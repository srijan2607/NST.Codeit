# # Bubble Sort 

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1): # n-i-1 is for ignoring the last element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))



# selection sort 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+i,n):
            if arr[j]<arr[min_idx]:
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))
