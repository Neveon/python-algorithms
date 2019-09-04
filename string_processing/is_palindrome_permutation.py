# palindrome - word or phrase that is the same forwards or backwards
# 'racecar'
# permutation is a rearangement of the letters
# 'acecarr - racecar'

palin_perm = 'Tact coa' # taco cat
not_palin_perm = 'This is not a palindrome permutation'

# t a c o c a t - 1 2 3 (4) 3 2 1

# 0(n) Time Complexity - Linear
def is_palin_perm(input_str):
  input_str = input_str.replace(" ", "")
  input_str = input_str.lower()

  d = dict()

  for i in input_str:
    d[i] = d.get(i,0) + 1 # keeping count of each letter
  
  odd_count = 0 # There can only be none or one odd element count
  for k, v in d.items():
    if v % 2 != 0 and odd_count == 0:
      odd_count += 1
    elif v % 2 != 0 and odd_count != 0:
      return False
  
  return True

print(is_palin_perm(palin_perm))

print(is_palin_perm(not_palin_perm))