def Selection_Sort(arr):
  for i in range(len(arr)):
    min=i
    for j in range(i,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
  print(arr)
Selection_Sort([5,3,8,6,7,2])
