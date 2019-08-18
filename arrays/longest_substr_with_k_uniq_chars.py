# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring/0
# It is an O(n) solution

t = int(input())

for _ in range(t):
    input_str = input()
    k = int(input())
    
    count = [0 for i in range(26)]
    u = 0
    start = 0
    
    for i, c in enumerate(input_str):
        if count[ord(c) - ord('a')] == 0:
            u += 1
        count[ord(c) - ord('a')] += 1
        if u > k:
            while count[ord(input_str[start]) - ord('a')] > 0: # amortised to O(1)
                count[ord(input_str[start]) - ord('a')] -= 1
                start += 1
                if start > i:
                    print('start=', start)
                    break
            u -= 1
        if u == k:
            print(input_str[start:i+1])
