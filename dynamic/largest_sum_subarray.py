def find_max_sum_sub_array(A):
  
  if A is None: 
    return None
  if len(A) == 1:
    return A[0]

  max_sum = A[0]  
  current_sum = A[0]
  for x in range(1, len(A)):
    if current_sum < 0:
      current_sum = A[x]
    else:
      current_sum += A[x]

    max_sum = max(max_sum, current_sum)
  return max_sum


print(find_max_sum_sub_array([1, 10, -1, 11, 5, -30, -7, 20, 25, -35]))
print(find_max_sum_sub_array([-15, -14, -10, -19, -5, -21, -10]))

### output ###
# 45
# -5
