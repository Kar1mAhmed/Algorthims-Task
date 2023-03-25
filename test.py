from time import time
from Basic_functions import creat_unsorted_array
def partition(arr,s,e):
      #pivot is the last element in the array
      pivot=arr[e]
      # i is the index of the new position of the element that is smaller than the pivot
      i=s-1

      for j in range(s,e):
            # if the pivot is bigger than this element in the arr the put it in the i || look up to see what is i
            if arr[j]<=pivot:
                  i+=1
                  arr[j],arr[i]=arr[i],arr[j]
      i+=1
      #after finishing get the pivot in the position that all smaller elements in the right and bigger on the left
      arr[e],arr[i]=arr[i],arr[e]
      return(i)


def quick_sort(arr,s,e):
      #in a random version we swap the last element in the array with a random element of the array before the start of every inner iteration
      if s<e:
            #get the right index of the pivot
            pv=(partition(arr,s,e))
            #sort the right half of the pivot
            quick_sort(arr,s,pv-1)
            #sort the left half of the pivot
            quick_sort(arr,pv+1,e)





def insertion_sort(arr):
      # we start with the second element to compare with first one if [1]>[2] we swap
      for j in range(1,len(arr)):
            # key is the number we want to find the right index for 
            key=arr[j]
            # i is the index of the number we compare with
            i=j-1
            while i>0 and arr[i]>key:
                  arr[i+1]=arr[i]
                  i=i-1
            arr[i+1]=key


test=creat_unsorted_array(199999)
test2=test
start_t=time()

insertion_sort(test)
end_t=time()

print("quick sort time is = " + str(end_t-start_t))

start_t=time()

quick_sort(test2,0,199998)
end_t=time()

print("insertion sort time is = " + str(end_t-start_t))

