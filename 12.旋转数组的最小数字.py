from exeTime import exeTime
@exeTime
def minNumberInRotateArray(rotateArray):
    p1,p2=0,len(rotateArray)-1
    while rotateArray[p1]>=rotateArray[p2]:
        if p1+1==p2:return rotateArray[p2]
        mid=int((p1+p2)/2)
        if rotateArray[p1]==rotateArray[mid] \
            and rotateArray[p2]==rotateArray[mid]:
            return minOrder(rotateArray)
        if rotateArray[mid]>=rotateArray[p1]:
            p1=mid
            continue
        if rotateArray[mid]<=rotateArray[p2]:
            p2=mid
            continue
    return rotateArray[p1]

def minOrder(n):
    mini=n[0]
    for i in range(len(n)):
        if n[i]<=mini:mini=n[i]
    return mini

@exeTime
def minNumberInRotateArray2(n):
    mini=n[0]
    for i in range(len(n)):
        if n[i]<=mini:mini=n[i]
    return mini

if __name__ == "__main__":
    n=[1,2,3,4,5]
    n=[9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8]
    #n=[1,0,1,1,1]

    print(minNumberInRotateArray(n))
    print(minNumberInRotateArray2(n))
    