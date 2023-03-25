from arr_fun import creat_unsorted_array
def partition(arr,s,e):
      #pivot is the last element in the array
      pivot=arr[e]
      # i is the index of the new position of the element that is smaller than the pivot
      i=s-1

      for j in range(s,e):
            # if the pivot is bigger than this elment in the arr the put it in the i || look up to see what is i
            if arr[j]<=pivot:
                  i+=1
                  arr[j],arr[i]=arr[i],arr[j]
      i+=1
      #after finshing get the pivot in the positon that all smaller elements in the right and bigger on the left
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

test=creat_unsorted_array(20)

quick_sort(test,0,len(test)-1)
print(test)
