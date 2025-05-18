# Em hãy viết chương trình xoá một nút trong danh sách liên kết đơn với tham chiếu Head và Tail.
#
# Input:
#
# Giá trị đầu tiên n: số phần tử của danh sách
# n giá trị tiếp theo: giá trị của phần tử cần thêm vào đầu danh sách
# Giá trị cuối cùng: giá trị cần tìm kiếm
# Output:
#
# các giá trị của danh sách được in theo thứ tự từ nút đầu đến nút cuối sau khi xoá nút
# inpout      output
# 3           4
# 5           5
# 4
# 7
# 7

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next= None

head = None

def insertFirst(head,data):
    NewNode = ListNode(data)
    NewNode.next=head
    head=NewNode
    return head
def delete(head, target):
    PreNode=None
    CurNode=head
    while CurNode is not None and CurNode.data!=target:
        PreNode=CurNode
        CurNode=CurNode.next
    if CurNode is not None:
        if CurNode is head:
            head=CurNode.next
        else:
            PreNode.next=CurNode.next
    return head
        
    

#print(a.next.next.data)
def travalList(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next
n=int(input())
for i in range(n):
    data=int(input())
    head=insertFirst(head,data)
target=int(input())
head=delete(head, target)
travalList(head)

# /* bài 2 Em hãy viết chương trình nhập vào n giá trị, mỗi giá trị nhập vào được chèn vào cuối danh sách liên kết (danh sách liên kết có tham chiếu Head và Tail) và in các giá trị của danh sách.
#
# Input:
#
# Giá trị đầu tiên: số phần tử của danh sách
# Các giá trị tiếp theo: giá trị của phần tử cần thêm vào cuối danh sách
# Output:
#
# các giá trị của danh sách được in theo thứ tự từ nút đầu đến nút cuối
# input       output
# 3            5
# 5            4
# 4            7
# 7
# */
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next= None

head = None

def insertLast(head,data):
    NewNode = ListNode(data)
    curNode=head
    if curNode==None:
        NewNode.next=head
        head=NewNode
    else:
        while curNode.next is not None:
            curNode=curNode.next
        curNode.next=NewNode
    return head
#print(a.next.next.data)
def travalList(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next
n=int(input())
for i in range(n):
    data=int(input())
    head=insertLast(head,data)
travalList(head)

# /* BÀI 3 Em hãy viết chương trình nhập vào n giá trị, mỗi giá trị nhập vào được chèn vào  danh sách liên kết sao cho danh sách liên kết luôn được sắp xếp tăng dần và in các giá trị của danh sách.
#
# Input:
#
# Giá trị đầu tiên: số phần tử của danh sách
# Các giá trị tiếp theo: giá trị của phần tử cần thêm vào đầu danh sách
# Output:
#
# các giá trị của danh sách được in theo thứ tự từ nút đầu đến nút cuối
# input     output
# 3          4
# 5          5
# 4          7
# 7
# */
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next= None

head = None


def insertLinkedListSorted(head, value):
    preNode=None
    curNode=head
    while curNode is not None and value>=curNode.data:
        preNode=curNode
        curNode=curNode.next
    newNode=ListNode(value)
    newNode.next=curNode
    if curNode is head:
        head=newNode
    else:
        preNode.next=newNode
    return head

    

#print(a.next.next.data)
def travalList(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next
n=int(input())
for i in range(n):
    data=int(input())
    head=insertLinkedListSorted(head,data)
travalList(head)

