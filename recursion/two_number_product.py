# Given two numbers, find their product using recursion

y = 3000
x = 500

def product_recursion(x, y):
  # Cut down on total number of recursive calls
  if x < y:
    return product_recursion(y,x)
  if y == 0:
    return 0
  else:
    return x + product_recursion(x, y-1)

print(product_recursion(y,x))