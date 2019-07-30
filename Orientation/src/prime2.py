def primes(n):
  f = [0] * (n+1)
  p = []
  for i in range(2, n+1):   # is i a prime?
    if not f[i]:            # is not sieved by any value?
      p.append(i)           # yeah, it's a prime!

    for j in p:             # let j be a known prime
      if j * i > n: break
      f[j * i] = True       # sive j * i
      if i % j == 0: break  # guarantee j is the minimum divisor
  return p
