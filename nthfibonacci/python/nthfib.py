def nthFibOf(n):
   if n <= 2:
      return n - 1
   else:
      return nthFibOf(n - 1) + nthFibOf(n - 2)

n = 7
print(nthFibOf(n))
