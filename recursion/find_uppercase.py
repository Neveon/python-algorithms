# Given input string, find first uppercase letter

# Iterative
def find_uppercase_iterative(input_str):
  for letter in input_str:
    if letter.isupper():
      return letter
  return "No uppercase character found"

# print(find_uppercase_iterative("heeelooo"))



# Recursive
def find_uppercase_recursive(input_str):
  if len(input_str) == 0:
    return "No uppercase character found"

  if input_str[0].isupper():
    return input_str[0]
  
  return find_uppercase_recursive(input_str[1:])

print(find_uppercase_recursive("helLlo"))