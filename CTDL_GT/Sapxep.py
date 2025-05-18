
#  sắp xếp dãy tăng dân theo giải thuật sắp xếp nổi bọt : 
def bubbleSort(theSep) : 
    n = len(theSep)
    for i in range(n-1): 
        for j in range(n-i-1):
            if theSep[j] > theSep[j+1]:
                tmp = theSep[j]
                theSep[j] = theSep[j+1] 
                theSep[j+1] = tmp 

#  sắp xếp dãy tăng dân theo giải thuật sắp xếp lựa chọn  : 
def selectionSort(theSep) : 
    n = len(theSep)
    for i in range(n-1): 
        # Giả sử phần tử nhỏ nhất là phần tử thứ i 
        smallNdx = i 
        # Xác định xem có phần tử nào khác chứa giá trị nhỏ hơn 
        for j in range(i + 1 , n):
            if theSep[j] < theSep[smallNdx]:
                smallNdx = j 
        #Hóa đổi giá trị phần tử tại ví trí thứ i và vị trí smallNdx 
        # chỉ khi giá trị nhỏ nhất không còn ở vị trí giả sử lúc đầu 
        if smallNdx != i :
            tmp = theSep[i]
            theSep[i] = theSep[smallNdx] 
            theSep[smallNdx] = tmp 
#  sắp xếp dãy tăng dân theo giải thuật sắp xếp chèn  :
def insertionSort(theSeq):
    n = len(theSeq)
    # Bắt đầu với phần tử đầu tiên được xem là một dãy đã được sắp xếp vì chỉ có duy nhất một phần tử
    for i in range(1, n):
        # Lưu giá trị của phần tử để tìm vị trí chỉ nó
        value = theSeq[i]
        # Tìm vị trí thích hợp cho value trong dãy đã được sắp xếp ở phần đầu dãy
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        # Đặt value vào vị trí đã tìm được
        theSeq[pos] = value
# danh sách trộn 
def mergeOrderedLists(ListA, ListB):
    newList = list()
    a = 0
    b = 0

    # Trộn 2 danh sách cùng nhau đến khi hết 1 danh sách
    while a < len(ListA) and b < len(ListB):
        if ListA[a] < ListB[b]:
            newList.append(ListA[a])
            a += 1
        else:
            newList.append(ListB[b])
            b += 1

    # Thêm phần tử còn lại của ListA vào newList
    while a < len(ListA):
        newList.append(ListA[a])
        a += 1

    # Thêm phần tử còn lại của ListB vào newList
    while b < len(ListB):
        newList.append(ListB[b])
        b += 1

    return newList

# Sắp xếp dãy tăng dần theo giải thuật sắp xếp trộn:
def pythonMergeSort(theList):
    # Kiểm tra trường hợp cơ sở - danh sách chứa 1 phần tử
    if len(theList) <= 1:
        return theList
    else:
        # Tính vị trí chính giữa
        mid = len(theList) // 2
        # Tách dãy và thực hiện các bước gọi đệ quy
        leftHalf = pythonMergeSort(theList[:mid])
        rightHalf = pythonMergeSort(theList[mid:])

        # Trộn hai phần tử đã xếp
        newList = mergeOrderedLists(leftHalf, rightHalf)
        return newList
# trộn nâng cao 

def recMergeSort(theSeq, first, last, tmpArray):
    if first < last:
        mid = (first + last) // 2
        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid + 1, last, tmpArray)
        mergeVirtualSeq(theSeq, first, mid, last, tmpArray)

def mergeVirtualSeq(theSeq, left, mid, right, tmpArray):
    a = left
    b = mid + 1
    m = 0
    while a <= mid and b <= right:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1
    while a <= mid:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1
    while b <= right:
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1
    for i in range(m):
        theSeq[left + i] = tmpArray[i]

def mergeSort(theSeq):
    n = len(theSeq)
    tmpArray = [None] * n
    recMergeSort(theSeq, 0, n - 1, tmpArray)

day = [1,5,4,2,3,8,9]
selectionSort(day)
print("Day sau khi sap xep theo kieu lua chon: ")
print(day)
bubbleSort(day)
print("Day sau khi sap xep theo kieu noi bot: ")
print(day)
insertionSort(day)
print("Dãy sau khi sắp xếp theo kiểu chèn:")
print(day)
sorted_day = pythonMergeSort(day)
print("Dãy sau khi sắp xếp theo kiểu trộn:")
print(sorted_day)
mergeSort(day)
print(day)
