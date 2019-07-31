def lowb(x):
  p = 0
  while x:
    # if p-th digit is 1, return 2^p
    if x & 1: return 1<<p
    x >>= 1 # x = x / 2
    p += 1
  return 0
