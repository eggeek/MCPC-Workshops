def primes(n):
  f = [0] * (n+1)
  p = []
  for i in range(2, n+1):
    if not f[i]:
      p.append(i)
    for j in p:
      if j * i > n: break
      f[j * i] = True
      if i % j == 0: break
  return p
