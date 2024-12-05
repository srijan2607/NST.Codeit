n = int(input())
stn = list(input().strip())
ff = len(stn)
count = 0
dict = {}
for x in stn :
    if x not in dict :
        dict[x] = 1
    else :
        dict[x] += 1
for x in range (1,ff,2):
    if x not in dict or dict[stn[x]] == 0  :
        count += 1
    else :
        dict[stn[x]] -= 1
print(count)

# n = int(input())
# stn = input().strip()
# keys = {}
# buy_counter = 0
 
# for i in range(len(stn)):
#     if i % 2 == 0:  
#         key = stn[i]
#         keys[key] = keys.get(key, 0) + 1
#     else:  
#         door = stn[i].lower()
#         if keys.get(door, 0) > 0: 
#             keys[door] -= 1  
#         else:
#             buy_counter += 1  
# print(buy_counter)
# print(keys)

n = int(input())
stn = input().strip()
keys = {}
buy_counter = 0

for i in range(len(stn)):
    if i % 2 == 0:  
        key = stn[i]
        if key in keys: 
            keys[key] += 1
        else:
            keys[key] = 1
    else:  
        door = stn[i].lower()
        if door in keys and keys[door] > 0: 
            keys[door] -= 1
        else:
            buy_counter += 1 

print(buy_counter)