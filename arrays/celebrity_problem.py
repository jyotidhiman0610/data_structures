https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1

celeb = 0
for i in range(1, n):
    if m[celeb][i] == 1:
        celeb = i

for i in range(n):
    # Celebrity doesn't know himself
    if i == celeb:
        continue
    # Check if celebrity doesn't know anyone
    if m[celeb][i] != 0:
        return -1
    # Check if everyone knows celebrity    
    if m[i][celeb] != 1:
        return -1
