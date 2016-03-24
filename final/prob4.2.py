def getSublists(L, n):
    if len(L) == n:
        return [L]

    return [L[:n]] + getSublists(L[1:], n)
    

def longestRun(L):
    lenL = len(L)
    for i in range(lenL,0,-1):
        for lst in getSublists(L,i):
            if lst == sorted(lst):
                return len(lst)
    return None



L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print longestRun(L)