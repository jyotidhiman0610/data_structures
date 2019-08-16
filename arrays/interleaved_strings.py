# https://practice.geeksforgeeks.org/problems/interleaved-strings/1#ExpectOP
def inter_util(A, B, C):
    x = 0
    y = 0
    if (len(A) == 0) & (len(B) == 0) & (len(C) == 0):
        return 1
    if len(A) != 0:
        if (A[0] == C[0]):
            x = inter_util(A[1:], B, C[1:])
    if len(B) != 0:
        if (B[0] == C[0]):
            y = inter_util(A, B[1:], C[1:])
    return max(x, y)
    
def isInterleave(A, B, C):
    return inter_util(A, B, C)
