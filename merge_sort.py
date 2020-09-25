def mergesort(list1):
     n=len(list1)
     if n > 1 :
          mid = n//2
          left_list = list1[:mid]
          right_list = list1[mid:]
          mergesort(left_list)
          mergesort(right_list)
     
          i=j=k=0
      
          while i < len(left_list) and j < len(right_list):
               if left_list[i] < right_list[j]:
                    list1[k]=left_list[i]
                    i=i+1
                    k=k+1
               else:
                    list1[k]=right_list[j]
                    j=j+1
                    k=k+1
          while i < len(left_list):
                list1[k]=left_list[i]
                i=i+1
                k=k+1

          while j < len(right_list):
                list1[k]=right_list[j]
                j=j+1
                k=k+1
     
     return list1
  
        
       

   

list2=[32,42,63,14,865,4527,264,2,91,93] 
 
print(mergesort(list2))