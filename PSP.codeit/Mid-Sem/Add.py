n = int(input())

# Upper part of the pattern
for i in range(1, n + 1):
    if i == 1:
        print("*" * (2 * n), end = " ")  # Full line of stars at the top
    else:
        for j in range(n - i):
            print("*", end=" ")
        for j in range(2 * i):
            print(" ", end=" ")
        for j in range(n - i):
            print("*", end=" ")
        print()

# Lower part of the pattern
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print("*", end=" ")
    for j in range(2 * i):
        print(" ", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()