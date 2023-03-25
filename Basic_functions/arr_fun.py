
from random import Random, randrange


def is_sorted(A):
      for i in range(len(A)-1):
            if A[i]>A[i+1]:
                  return False
      return True



def creat_unsorted_array(array_size):
      arr=[]
      for i in range(array_size):
            arr.append(randrange(0,1001,1))

      return arr

