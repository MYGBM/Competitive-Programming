def Insertion_Sort(arr)
 for i in range(1,len(arr)):
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
         arr[j+1]=arr[j]
         print(' '.join(map(str,arr))) # print each shift as a string of numbers
         j-=1
        arr[j+1]=curr 
    print(' '.join(map(str,arr)))    # print final array as a string of numbers
    
