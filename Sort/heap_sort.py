import math


def heapify(arr,n,i):

      l = i * 2 + 1
      r = i * 2 + 2
      largest = i
      
      if l < n and arr[l] > arr[i]:
            largest = l

      if r < n and arr[r] > arr[largest]:
            largest = r

      if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(arr, n, largest)



def heap_sort(arr):
      n = len(arr)

      for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

      for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            heapify(arr, i, 0)




arr=[21, 31, 4, 46, 57, 67, 79, 9, 57, 3, 1, 31, -2]

heap_sort(arr)
print(arr)
