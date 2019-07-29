def primes(n):
  p = []
  for i in range(2,n+1):
    f = False
    for j in range(2, i):
      if i % j == 0:
        f = True
        break
    if not f:
      p.append(i)
  return p
