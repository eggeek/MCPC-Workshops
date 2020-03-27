f = [0] * (n+1)           # set f[0]=0, f[1]=0, ... f[n]=0
p = []                    # empty prime list at beginning
for i in range(2, n+1):   # is i a prime?
  if not f[i]:            # not sieved by any value
    p.append(i)           # yeah, it's a prime!

  for j in p:             # let j be a known prime
    if j * i > n: break   # reach the upper bound
    f[j * i] = True       # sieve j * i
    if i % j == 0: break  # guarantee j is the minimum divisor