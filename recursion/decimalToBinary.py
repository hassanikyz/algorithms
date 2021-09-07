def decimalToBinary(num) :
  # Write your code here
  if num < 2:
    return str(num)
  
  return decimalToBinary(num//2) + decimalToBinary(num % 2)

num = 13
print(f"{num} binary rep is ", decimalToBinary(num))
num = 130
print(f"{num} binary rep is ", decimalToBinary(num))
num = 1
print(f"{num} binary rep is ", decimalToBinary(num))
num = 2
print(f"{num} binary rep is ", decimalToBinary(num))

### output ###
"""
13 binary rep is  1101
130 binary rep is  10000010
1 binary rep is  1
2 binary rep is  10

"""
