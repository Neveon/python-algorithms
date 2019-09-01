# A -> column 1
# B -> column 2
# Z -> column 26

# AA -> column 27
# AB -> column 28

input_str = 'AB'

def spreadsheet_encode_iterative(input_str):
  result = 0
  count = len(input_str) - 1 # exponent used
  # AA = (A*26^1) + (A*26^0) = 27
  for letter in input_str:
    result += 26**count * (ord(letter) - ord('A') + 1)
    count -= 1
  return result

def spreadsheet_encode_recursive(input_str, count = len(input_str) - 1):
  if len(input_str) > 1:
    return (26**count * (ord(input_str[0]) - ord('A') + 1)) + spreadsheet_encode_recursive(input_str[1:], count-1)
  else:
    return (26**count * (ord(input_str[0]) - ord('A') + 1))


print(spreadsheet_encode_recursive(input_str))