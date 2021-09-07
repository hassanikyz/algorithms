def decimalToBinary(num) :
  
  """
  ALGORITHM:
  When you divide say 2 by 2 you get 1 as the dividend and 0 as the remainder. Notice if you simply concatentate these two entities (dividend and remainder)
  you get your binary represenation "10". However when number is larger than 2 this process can be repeated for the dividend and the remainders.
  
  For example, take 13. 
  13 % 2 => "1" <=== this becomes part of the representation
  13 // 2 => 6
  
  repeating only for 6 we get
  6 % 2 => "0" <=== this becomes part of the representation
  6 // 2 => 3
  
  repeating only for 3 we get
  3 % 2 =>  "1"  <=== this becomes part of the representation
  3 // 2 => "1"  <=== this becomes part of the representation
  
  Process should terminate when number is below 2. Thus the representation is "1101" going from the most significant (bottom) to least significant (top)
  
  This shows problem can solved by recursion and results concatenated.
  
  """
  
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
