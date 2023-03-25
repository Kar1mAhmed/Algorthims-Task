from arr_fun import creat_unsorted_array


def bubble_sort(arr):
      for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                  if arr[j]<arr[j+1]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]

s=creat_unsorted_array(20)


bubble_sort(s)

print(s)