# https://practice.geeksforgeeks.org/problems/finding-the-numbers/0
# Also for https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences/0
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(' ') if i!='']
    res = 0
    for element in a:
        res ^= element
    rightmost_set_bit = res & (~res + 1)
    first_no = 0
    second_no = 0
    for element in a:
        if element & rightmost_set_bit:
            first_no ^= element
        else:
            second_no ^= element
    if first_no < second_no:
        print(first_no, second_no)
    else:
        print(second_no, first_no)

    
