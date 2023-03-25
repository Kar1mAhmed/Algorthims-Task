def insertion_sort(arr):
      # we start with the second element to compare with first one if arr[0] > arr[1] we swap
      for j in range(1,len(arr)):
            # key is the number we want to find the right index for 
            key = arr[j]
            # i is the index of the number we compare with
            i = j - 1
            while i >= 0 and arr[i] > key:      
                  arr[i+1] = arr[i]
                  i -= 1
            arr[i+1] = key


list= [2,3,6,21,3,6,8,90,22,1,5,7,3,9,11]

insertion_sort(list)

print(list)