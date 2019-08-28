# https://practice.geeksforgeeks.org/viewSol.php?subId=19181744&pid=389&user=showmethecode
for _ in range(t):
    n = int(input())
    if n > 9:
        q = [i for i in range(0, 10)]
    else:
        q = [i for i in range(0, n+1)]
    
    while len(q):
        element = q.pop(0)
        if element > n:
            break
        print(element, end=' ')
        if element == 0:
            continue
        last_digit = element % 10
        if last_digit != 0:
            before = last_digit - 1
            q.append(element*10 + before)
        if last_digit != 9:
            after = last_digit + 1
            q.append(element*10 + after)
    
    print('')
