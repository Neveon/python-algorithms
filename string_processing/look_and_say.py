# Given n, find the nth look and say sequence
# 1
# 1 1
# 2 1
# 1 2 1 1
# 1 1 1 2 2 1
# 3 1 2 2 1 1
# 1 3 1 1 2 2 2 1

def next_sequence(s):
  result = []
  i = 0
  while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]: # check next number in s
      i += 1 # index
      count += 1 # keeping count of same number
    result.append(str(count) + s[i])
    i += 1
  return ''.join(result)

s = '1'
n = 20
for i in range(n-1):
  s = next_sequence(s)
  print(s+'\n')
