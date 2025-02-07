"""
Description:
Complete the solution so that the function will break up camel casing, using a space between words.

Example:
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    return "".join([(" " if letter.isupper() else "") + letter for letter in s])
