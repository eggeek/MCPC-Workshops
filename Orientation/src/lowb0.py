def lowb(x):
  p = 0
  while x:
    if x & 1:
      return 1<<p # 2^p
    x >>= 1 # x = x / 2
    p += 1
  return 0
