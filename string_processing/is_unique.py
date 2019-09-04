# Determine if a given string has all unique characters

unique_str = 'AbCDefG'
non_unique_str = 'unique'

def is_unique(input_str):
  input_str = input_str.lower().replace(' ', '')

  d = dict()
  for letter in input_str:
    d[letter] = d.get(letter, 0) + 1

  return all(value == 1 for value in d.values())

print(is_unique(unique_str))
print(is_unique(non_unique_str))