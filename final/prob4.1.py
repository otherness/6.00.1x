def getSublists(L, n):
    if len(L) == n:
        return [L]

    return [L[:n]] + getSublists(L[1:], n)
    

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4

print getSublists(L,n)prob4.1.py