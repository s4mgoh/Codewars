"""
Description:
Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, 
n is the number of hotdogs a customer will buy, different numbers have different prices 
(refer to the following table), return how much money will the customer spend to buy that 
number of hotdogs.

number of hotdogs	price per unit (cents):
n < 5	100
n >= 5 and n < 10	95
n >= 10	90

You can use if..else or ternary operator to complete it.
"""

def sale_hotdogs(n):
  return 100*n if n<5 else 95*n if 5<=n<10 else 90*n
