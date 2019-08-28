# https://practice.geeksforgeeks.org/problems/interleaved-strings/1

def isInterleave(A, B, C):
    a = len(A)
    b = len(B)
    dp = [[0 for _ in range(b + 1)] for __ in range(a + 1)]
    dp[0][0] = 1
    
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 and j == 0:
                continue
            if C[i + j -1] == A[i-1] and C[i + j -1] == B[j-1]:
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif i > 0 and C[i + j -1] == A[i-1]:
                dp[i][j] = dp[i-1][j]
            elif j > 0 and (C[i + j -1] == B[j-1]):
                dp[i][j] = dp[i][j-1] 
            else:
                dp[i][j] = 0
    return (dp[a][b])
