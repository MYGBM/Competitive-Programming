def Counting_Sort(arr):
    result=[0]*(max(arr)+1)
    ans=[]
    for i in arr:
        result[i]+=1
    #return result
    for i in range(len(result)):
        if result[i]!=0:
            ans.extend([i]*result[i])
    return ans
print(Counting_Sort([1,1,3,2,1]))
print(Counting_Sort([6,5,4,3,2,1]))
 
