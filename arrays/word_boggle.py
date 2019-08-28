# https://practice.geeksforgeeks.org/problems/word-boggle/0

def generate_all_words(boggle, i, j, string, visited, M, N, dictionary, output):
    if (i < 0) or (i >= M) or (j < 0) or (j >= N) or (visited[i][j]):
        return
    
    visited[i][j] = 1
    string = string + boggle[i][j]
    if string in dictionary:
        output.add(string)

    generate_all_words(boggle, i + 1, j, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i - 1, j, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i, j + 1, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i, j - 1, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i + 1, j - 1, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i + 1, j + 1, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i - 1, j - 1, string, visited, M, N, dictionary, output)
    generate_all_words(boggle, i - 1, j + 1, string, visited, M, N, dictionary, output)
    visited[i][j] = 0

class Trie:
    def __init__(self):
        self.child = [None for i in range(26)]
        self.is_leaf = False

def create_trie(dictionary, root):
    for word in dictionary:
        kafka = root
        for index, char in enumerate(word):
            if not kafka.child[ord(char) - ord('a')]:
                kafka.child[ord(char) - ord('a')] = Trie()
            kafka = kafka.child[ord(char) - ord('a')]
            if index + 1 == len(word):
                kafka.is_leaf = True
    return root
    
def boggling_magic(boggle, root, visited, M, N, i, j, string):
    if (i < 0) or (i >= M) or (j < 0) or (j >= N) or (visited[i][j]):
        return
    visited[i][j] = 1
    
    if root.is_leaf:
        output.add(string)
    
    for index, child in enumerate(root.child):
        if child is None:
            continue
        ch = chr(index + ord('a'))
        if (j+1 < N) and (boggle[i][j+1] == ch):
            boggling_magic(boggle, child, visited, M, N, i, j+1, string + ch)
        if (j-1 >= 0) and (boggle[i][j-1] == ch):
            boggling_magic(boggle, child, visited, M, N, i, j-1, string + ch)
        if (i+1 < M) and (boggle[i+1][j] == ch):
            boggling_magic(boggle, child, visited, M, N, i+1, j, string + ch)
        if (i-1 >= 0) and (boggle[i-1][j] == ch):
            boggling_magic(boggle, child, visited, M, N, i-1, j, string + ch)
        if (i-1 >= 0) and (j+1 < N) and (boggle[i-1][j+1] == ch):
            boggling_magic(boggle, child, visited, M, N, i-1, j+1, string + ch)
        if (i-1 >= 0) and (j-1 >= 0)  and (boggle[i-1][j-1] == ch):
            boggling_magic(boggle, child, visited, M, N, i-1, j-1, string + ch)
        if (i+1 < M) and (j+1 < N) and  (boggle[i+1][j+1] == ch):
            boggling_magic(boggle, child, visited, M, N, i+1, j+1, string + ch)
        if (i+1 < M  ) and (j-1 >= 0) and  (boggle[i+1][j-1] == ch):
            boggling_magic(boggle, child, visited, M, N, i+1, j-1, string + ch)
    
    visited[i][j] = 0
        

def do_boggle_stuff(boggle, root, visited, m, n):
    if not root:
        return
    
    for i in range(m):
        for j in range(n):
            if root.child[ord(boggle[i][j]) - ord('a')]:
                boggling_magic(boggle, root.child[ord(boggle[i][j]) - ord('a')], visited, int(m), int(n), i, j, boggle[i][j])
    
for _ in range(t):
    no_of_words = int(input())
    dictionary = [i.lower() for i in input().split(' ')]
    m, n = input().split(' ')
    b_str = input().split(' ')
    boggle = [[0 for i in range(int(n))] for j in range(int(m))]
    visited = [[0 for i in range(int(n))] for j in range(int(m))]
    output = set([])
    
    k = 0
    for i in range(int(m)):
        for j in range(int(n)):
            boggle[i][j] = b_str[k].lower()
            k += 1
    call = Trie()
    call = create_trie(dictionary, call)
    
    do_boggle_stuff(boggle, call, visited, int(m), int(n))

    # for i in range(int(m)):
    #     for j in range(int(n)):
    #         generate_all_words(boggle, i, j, '', visited, int(m), int(n), dictionary, output)
    o = list(output)
    o.sort()
    for s in o:
        if b_str[0].isupper():
            s = s.upper()
        print(s, end=' ')
    if not len(o):
        print(-1, end=' ')
    
    print('')
