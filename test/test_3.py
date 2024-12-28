import math
from ..src.cal import Calculations 

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11

def test_cal():
   calculation = Calculations(8, 2)
   assert calculation.get_sum() == 10
   assert calculation.get_difference() == 6