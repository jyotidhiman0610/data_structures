#https://practice.geeksforgeeks.org/problems/special-keyboard/0

# Solution 1: Recursive 

t = int(input())

def find_max(n, can_copy, can_paste):
    if n <= 0:
        return 0
    x = 0
    y = 0
    z = 0
    x = find_max(n - 1, can_copy + 1, can_paste) + 1
    if n >= 3:
        if can_copy:
            y = find_max(n - 3, can_copy*2, can_copy) + can_copy
    if n > 0 & can_paste:
        z = find_max(n - 1, can_copy + can_paste, can_paste) + can_paste
    return max(x, y, z)
    
    
for _ in range(t):
    n = int(input())
    print(find_max(n, 0, 0))
    
    
