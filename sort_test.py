from typing import List
import random

def randomIntegers(lower_bound: int, upper_bound: int, n: int) -> List:
  return [random.randint(lower_bound, upper_bound) for i in range(n)]

# The sortCheck method is used to check the sortedness of a list passed to it
def sortCheck(A: List) -> bool:
  n = len(A)
  for i in range(1,n):
    if A[i] < A[i-1]:
      return False
  return True