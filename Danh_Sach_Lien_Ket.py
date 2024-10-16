# Lớp
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    # Triển khai kiểu dữ liệu trừu tượng Bag bằng một danh sách được liên kết đơn 


class Bag:
    # Khoi tạo Bang rỗng 
    def __init__(self):
        self._head = None
        self._size = 0

        # Trả lại số lượng

    def __len__(self):
        return self._size

        # Xác định xem một vật có trong Bag không 

    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

        # Thêm 1 vật vào Bag 

    def add(self, item):
        newNode = ListNode(item)
        newNode.next = self._head
        self._head = newNode
        self.size += 1

        # Loại bỏ một đồ vật ra khỏi bag 

    def remove(self, item, head=None):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

            # Đồ vật phải nằm trong Bag để loại bỏ 
        assert curNode is not None, "item phải nằm trong túi"

        # Hủy liên kết nút và trả lại đồ 

        self.size -= 1
        if curNode is head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item


a = ListNode(15)
b = ListNode(63)
