p = []                    # empty prime list at beginning
for i in range(2,n+1):    # is i a prime?
  f = False
  for j in range(2, i):   # any divisor in [2, i-1]?
    if i % j == 0:
      f = True
      break
  if not f:               # no divisor
    p.append(i)           # yeah, it's a prime!