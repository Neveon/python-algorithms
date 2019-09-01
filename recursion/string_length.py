# Given a string, calculate the length of the strength

input_str = "hello"

# Iterative
def iterative_str_len(input_str):
  count = 0
  for letter in input_str:
    count += 1
  print(count)

# iterative_str_len(input_str)



# Recursive

# Initially feed function the entire string, each return
# will feed one less character

def recursive_str_len(input_str):
  if len(input_str) == 0:
    return 0
  return 1 + recursive_str_len(input_str[1:]) # excluding 0th

print(recursive_str_len(input_str))