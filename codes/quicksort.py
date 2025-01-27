def swap(mylist,index1,index2):
    mylist[index1],mylist[index2] = mylist[index2],mylist[index1]
def pivot(my_list,pivot_index,end_index):
    swap_index= pivot_index
    for i in range(pivot_index+1,end_index+1):
        if my_list[i]<my_list[pivot_index]:
            swap_index+=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index
def quciksort_helper(my_list,left,right):
    if left<right:
        pivot_index = pivot(my_list,left,right)
        quciksort_helper(my_list,left,pivot_index-1)
        quciksort_helper(my_list,pivot_index+1,right)
    return my_list
def quicksort(mylist):
    return quciksort_helper(my_list,0,len(mylist)-1)

my_list = [3,5,0,6,2,1,4]
quicksort(my_list)
print(my_list)

