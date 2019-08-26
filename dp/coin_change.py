t = int(input())

def calculate_change(arr, sum):
    n = len(arr)
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1
    for element in arr:
        for s in range(sum + 1):
            if element <= s:
                dp[s] +=  dp[s - element]
    
    return dp[sum]

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(' ') if i!='']
    sum = int(input())
    print(calculate_change(arr, sum))
