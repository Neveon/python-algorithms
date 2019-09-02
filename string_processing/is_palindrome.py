# palindrome is a string that is the same front and back
# ignore casing, spacing, and special characters

palindrome = 'Was it a cat I saw?'
not_palindrome = 'Was it a cat I saw?'

def is_palindrome(s):
  # iterators
  i = 0
  j = len(s) - 1

  while i < j:
    # Check for alphanumeric 
    while not s[i].isalnum() and i < j:
      i += 1
    while not s[j].isalnum() and i < j:
      j -= 1
    if s[i].lower() != s[j].lower():
      return False
    
    i += 1
    j -= 1
  return True

print(is_palindrome(palindrome))
print(is_palindrome(not_palindrome))