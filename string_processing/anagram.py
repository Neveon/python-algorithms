s1 = 'fairy tales'
s2 = 'rail safety'

s1.replace(" ", "").lower()
s2.replace(" ", "").lower()

# # Requires n log n time since any comparison based sorting algorithm
# # requires at least n log n time to sort
# print(sorted(s1) == sorted(s2))

# My answer
# s1Count = dict()
# for letter in s1:
#   s1Count[letter] = s1Count.get(letter, 0) + 1

# s2Count = dict()
# for letter in s2:
#   s2Count[letter] = s2Count.get(letter, 0) + 1

# print(s1Count == s2Count)

def is_anagram(s1, s2):
  # hash table
  ht = dict()

  if len(s1) != len(s2):
    return False
  
  for i in s1:
    if i in ht:
      ht[i] += 1
    else :
      ht[i] = 1
  
  for i in s2:
    if i in ht:
      ht[i] -= 1
    else :
      ht[i] = 1
  
  for i in ht:
    if ht[i] != 0:
      return False
  
  return True

print(is_anagram(s1, s2))
