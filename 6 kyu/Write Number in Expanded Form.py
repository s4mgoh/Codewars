"""
Description:
You will be given a number and you will need to return it as a string in Expanded Form. 

For example:
   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

Note: 
All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
  num_str = str(num)
  legnth = len(num_str)
  expanded = []
  for i in range(length):
    digit = int(num_str[i])
    if digit != 0:
      expanded.append(str(digit * (10 ** (length - 1 - i))))
    return " + ".join(expanded)
