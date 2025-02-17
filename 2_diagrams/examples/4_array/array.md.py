def vvod2(n, m, A):
    A = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            A[i][j] = input()
    return A

print(vvod2(2, 3, []))