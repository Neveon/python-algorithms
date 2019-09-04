"""
Given two strings, write a method to decide if one is a permutation of the other
"""

# Spaces may or may not be significant "God   "
is_permutation_1 = 'God' # must change to lowercase
is_permutation_2 = 'dog'

not_permutation_1 = 'Not'
not_permutation_2 = 'top'

# Time Complexity: O(n log n) - sorting is n log n
# Space Complexity: O(1)
def is_perm_1(str_1, str_2):
  str_1 = str_1.lower()
  str_2 = str_2.lower()

  # check the length of strings
  if len(str_1) != len(str_2):
    return False

  str_1 = ''.join(sorted(str_1)) # conveting sorted list of letters into a string
  str_2 = ''.join(sorted(str_2))

  n = len(str_1)

  for i in range(n):
    if str_1[i] != str_2[i]:
      return False
  
  return True


# Time Complexity: O(n)
# Space Complexity: O(n)

def is_perm_2(str_1, str_2):
  str_1 = str_1.lower()
  str_2 = str_2.lower()

  if len(str_1) != len(str_2):
    return False

  # hask table
  d = dict()
  for letter in str_1:
    d[letter] = d.get(letter, 0) + 1

  print(d)
  
  for letter in str_2:
    d[letter] = d.get(letter, 0) - 1

  print(d)

  # check if all values is equal to 0 in dictionary
  return all(value == 0 for value in d.values())



print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))