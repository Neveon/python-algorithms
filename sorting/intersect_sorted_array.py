A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# General solution - not optimal if A and B are already sorted
# set() does not include duplicate values
# .intersection() returns the matched values
#print(set(A).intersection(B))

def intersect_sorted_array(A, B):
  # two iterations, list A and list B - taking advantage of sorted lists
  i = 0
  j = 0
  intersection = []

  while i < len(A) and j < len(B):
    if A[i] == B[j]:
      if i == 0 or A[i] != A[i-1]:
        intersection.append(A[i])
      i += 1
      j += 1
    elif A[i] < B[j]:
      i += 1
    else: # A[i] > B[j]
      j += 1

  return intersection

print(intersect_sorted_array(A, B))