https://practice.geeksforgeeks.org/problems/form-a-palindrome/0

t = int(input())

# Recursive approach
def min_change(string, l, h):
    if l > h:
        return 0
    if string[l] == string[h]:
        return min_change(string, l+1, h-1)
    else:
        return min(min_change(string, l+1, h), min_change(string, l, h-1)) + 1

# DP solution
for _ in range(t):
    input_str = input().strip()
    high = len(input_str) 
    low = 0
    
    m = [[0 for i in range(high)] for j in range(high)]
    
    for gap in range(1, high):
        l = 0
        h = l + gap
        while (h < high):
            if (input_str[l] == input_str[h]):
                m[l][h] = m[l+1][h-1]
            else:
                m[l][h] = min(m[l+1][h], m[l][h-1]) + 1
            l = l + 1
            h = l + gap
    print(m[0][high-1])
                
            
    
