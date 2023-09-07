def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fact_rec(n-1)

n = 4
result = fact_rec(n)
print('The factorial of',n,'is',result)