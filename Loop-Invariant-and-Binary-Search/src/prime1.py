f = [0] * (n+1)           # set f[0]=0, f[1]=0, ... f[n]=0
p = []                    # empty prime list at beginning
for i in range(2, n+1):   # is i a prime?
  if not f[i]:            # not sieved by any value
    p.append(i)           # yeah, it's a prime!

  j = 2                   # sieve:
  while j*i <= n:         # 2*i,
    f[j*i] = True         # 3*i,
    j += 1                # ...
