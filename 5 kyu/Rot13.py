"""
Description:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 
letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with ROT13. If there
are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, 
like in the original ROT13 "implementation". Please note that using ENCODE is considered cheating.
"""

def rot13(message):
  def shift_char(c):
    if c.islower():
      return chr(ord((c) - ord("a") + 13) % 26 + ord('a'))
    elif c.isupper():
      return chr(ord((c) - ord("A") + 13) % 26 + ord('A'))
    return c
  return "".join(map(shift_char, message))
