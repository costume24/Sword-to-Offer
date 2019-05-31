def frog(array,index):
    if not array or index<0:
        return 
    if index==0:return True
    index_3,index_4,index_5=-1,-1,-1
    if array[index]-3 in array:
        index_3=array.index(array[index]-3)
    if array[index]-4 in array:
        index_4=array.index(array[index]-4)
    if array[index]-5 in array:
        index_5=array.index(array[index]-5)
    return frog(array,index_3) or frog(array,index_4) or frog(array,index_5)

if __name__ == "__main__":
    array=[1]
    print(frog(array,len(array)-1))  


            
        