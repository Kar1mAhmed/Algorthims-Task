import imp
from arr_fun import creat_unsorted_array
def selction_sort(A):

      for i in range(len(A)):
            smallest=float("inf")
            index=0

            #loop through all unsorted elemnts and  get the biggest (inner)
            for j in range(i,len(A)):
                  if A[j] < smallest:
                        smallest=A[j]
                        index=j

            #putting the biggest elemnt in the right position
            A[i],A[index]=A[index],A[i]

A=creat_unsorted_array(30)
selction_sort(A)
print(A)



      
