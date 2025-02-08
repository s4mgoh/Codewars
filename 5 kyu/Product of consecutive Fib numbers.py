"""
Description:
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such that:
F(0) = 1
F(1) = 1
F(n) = F(n-1) + F(n-2)

Given a number, prod (for product), we search for 2 Fibonacci numbers F(n) & F(n+1) verifying:
F(n) * F(n+1) = prod
Your function takes an integer (prod) and returns an array/tuple 
(check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:
F(n), F(n+1), true
if you do not find consecutive F(n) verifying F(n) * F(n+1) = prod:
F(n), F(n+1), false

where F(n) is the smallest one such as F(n) * F(n+1) > prod.

Examples:
714 ---> (21, 34, True)
--> since F(8) = 21, F(9) = 34 and 714 = 21 * 34
800 --->  (34, 55, False)
--> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
"""

def product_fib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    
    if a * b == prod:
        return [a, b, True]
    else:
        return [a, b, False]
  
