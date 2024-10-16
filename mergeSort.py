def mergeOrderedList(listA, listB):
    newList = list()
    a = b= 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList
def mergeSort(theList):
    if len(theList) <= 1:
        return theList
    else :
        mid = len(theList) // 2
        leftHalf = mergeSort(theList[:mid])
        rightHalf = mergeSort(theList[mid:])
        newList = mergeOrderedList(leftHalf,rightHalf)
        return newList
theList = [1,6,3,2,5,7,9,12,14,13]
print(mergeSort(theList))