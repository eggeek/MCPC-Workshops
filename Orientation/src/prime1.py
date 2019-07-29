def primes(n):
  f = [0] * (n+1)
  p = []
  for i in range(2, n+1):
    if not f[i]:
      p.append(i)
    j = 2
    while j*i <= n:
      f[j*i] = True
      j += 1
  return p
