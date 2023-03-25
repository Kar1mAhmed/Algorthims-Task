def merge_sort(arr):

      if len(arr)>1: # Base case

            mid=len(arr)//2

            L=arr[:mid] # the left part of the array
            R=arr[mid:] # the right part of the array

            merge_sort(L) # calling merge sort on the left part of the array 
            merge_sort(R) # calling merge sort on the right part of the array 
            merge_sort(R) 

            r=l=i=0

            while r < len(R) and l < len(L): #combining the two parts 

                  if R[r] > L[l]:
                        arr[i]=L[l]
                        l+=1
                  #using else instead of elif to avoid infinite loop in equal state
                  else :
                        arr[i]=R[r]
                        r+=1

                  i+=1

            while r < len(R): # in case if the left is empty and right still have some values
                  arr[i]=R[r]
                  r+=1
                  i+=1
            
            while l < len(L): # in case if the right is empty and left still have some values
                  arr[i]=L[l]
                  i+=1
                  l+=1




list= [2,3,6,21,3,6,8,90,22,1,5,7,3,9,11]

merge_sort(list)

print(list)