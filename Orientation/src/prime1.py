def primes(n):
  f = [0] * (n+1)
  p = []
  for i in range(2, n+1):   # is i a prime?
    if not f[i]:            # is not sieved by any value?
      p.append(i)           # yeah, it's a prime!

    j = 2                   # sieve:
    while j*i <= n:         # 2*i,
      f[j*i] = True         # 3*i,
      j += 1                # ...
  return p
