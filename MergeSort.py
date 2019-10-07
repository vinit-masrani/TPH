def merge_asc(left,right):
        result=[]
        i,j=0,0
        while i<length(left) and j<length(right):
                if left[i]<right[j]:
                        result.append(left[i])
                        i+=1
                else:   
                        result.append(right[j])
                        j+=1      
        result+=left[i:]     
        result+=right[j:]       
        return result

def merge_desc(left,right):
        result=[]
        i,j=0,0
        while i<length(left) and j<length(right):
                if left[i]>right[j]:
                        result.append(left[i])
                        i+=1
                else:   
                        result.append(right[j])
                        j+=1      
        result+=left[i:]     
        result+=right[j:]       
        return result    
        
def merge_sort(arr):
    if(length(arr)<=1):return arr
    mid=int(length(arr)/2)
    if style is 'Asc' : return merge_asc(merge_sort(arr[:mid]),merge_sort(arr[mid:]))
    if style is 'Desc': return merge_desc(merge_sort(arr[:mid]),merge_sort(arr[mid:]))
