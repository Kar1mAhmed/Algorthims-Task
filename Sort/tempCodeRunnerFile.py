for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            heapify(arr, i, 0)