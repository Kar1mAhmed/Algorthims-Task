import arr_fun as fun
from arr_fun import creat_unsorted_array
from quick_sort import quick_sort
def binary_search(A,num):
      if fun.is_sorted(A):
            start=0
            end=len(A)
            while end > start:
                  mid=int((start+end)/2)

                  if A[mid]==num:
                        return(f"the index of the number is {mid}")
                  elif A[mid]>num:
                        end=mid-1
                  else:
                        start=mid+1

            return("number not found")
      else:
            print("array is not sorted")




A=creat_unsorted_array(500)
quick_sort(A,0,499)
print(binary_search(A,20))









