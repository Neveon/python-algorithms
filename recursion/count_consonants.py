# Given a string, cout the number of consonants

# Iterative
def count_iterative(input_str):
  vowels = 'aeiou'
  count = 0
  for letter in input_str:
    if letter.lower() not in vowels and letter.isalpha():
      count += 1
  return count

#print(count_iterative('INPut_STR'))




def count_recursive(input_str):
  vowels = 'aeiou'
  if input_str == '':
    return 0
  elif input_str[0].lower() not in vowels and input_str[0].isalpha():
    return 1 + count_recursive(input_str[1:])
  else:
    return count_recursive(input_str[1:])

print(count_recursive('INPuT StR'))