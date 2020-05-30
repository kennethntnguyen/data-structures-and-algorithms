from typing import List

def bubbleSort(N: List) -> List:
  n = len(N)
  for i in reversed(range(0,n)):
    for j in range(0,i):
      if N[j+1] < N[j]:
        temp = N[j]
        N[j] = N[j+1]
        N[j+1] = temp
  return N

