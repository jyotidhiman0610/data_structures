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

# Above solution has overlapping problems and the same has been handled in below code
def inter_util(A, B, C, aa, bb, cc, a, b, c):
    x = 0
    y = 0
    if (aa == a) & (bb == b) & (cc == c):
        return 1
    if aa < a:
        if (A[aa] == C[cc]):
            x = inter_util(A, B, C, aa+1, bb, cc+1, a, b ,c)
    if (x == 0) & (bb < b):
        if (B[bb] == C[cc]):
            y = inter_util(A, B, C, aa, bb + 1, cc + 1, a, b, c)
    return max(x, y)
    
def isInterleave(A, B, C):
    a = len(A)
    b = len(B)
    c = len(C)
    return inter_util(A, B, C, 0, 0, 0, a, b, c)
