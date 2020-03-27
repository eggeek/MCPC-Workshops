a.sort()
tot, i, j, n = 0, 0, 0, len(a)

while i < n:

    while j < n and a[j] - a[i] < k: j+=1

    cnt = 0
    while j < n and a[j] - a[i] == k:
        cnt += 1
        j += 1

    tot += cnt
    while i+1 < n and a[i+1] == a[i]:
        i += 1
        tot += cnt
    i += 1