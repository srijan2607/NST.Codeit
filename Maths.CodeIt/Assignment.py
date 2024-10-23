"""Imagine a hallway with 100,000 doors, all initially closed, and a group of 100,000 people, each numbered from 1 to 100,000. The doors are also numbered from 1 to 100,000.
Here's how the process works:

Person 1 walks down the hallway and opens every door.
Person 2 walks down the hallway and closes every door that is a multiple of 2.
Person 3 walks down the hallway and toggles every door that is a multiple of 3 (if a door is open, they close it, and if it's closed, they open it).
Person 4 toggles every door that is a multiple of 4, and so on, with each person toggling the doors that are multiples of their own number.
This process continues until all 1,00,000 people have taken their turn.
Given a door numbered 
n
n, your task is to find out in how many ways you can choose two distinct people who both can switch the same Door 
n
n."""

n = int(input())
div = 0

for i in range(1,n+1):
    if n % i == 0:
        div += 1

print(div * (div - 1) // 2)