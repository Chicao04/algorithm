class _BSTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Phương thức tìm kiếm đệ quy cho một khóa đích

class BSTree :
    def __init__ (self):
        self.root = None 
        self.size = 0 
    
    def __len__(self):
        return self.size 
    

    def _bstSearch(self,subtree, target): 
        if subtree is None:
            return None
        elif target < subtree.key : 
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key :
            return self._bstSearch(subtree.right, target)
        else: 
            return subtree
    # Phương thức tìm nút chứa giá trị khóa nhỏ nhất. 
    def _bstMininum(self, subtree):
        if subtree is None :
            return None 
        elif subtree is None :
            return subtree
        else : 
            return self._bstMininum(subtree.left)
    
    # thêm một phần tử mới vào cây 
    def add(self , key): 
        # tìm vị trí đặt nút mới chứa khóa key 
        node = self._bstSearch(key) 
        # nếu khóa key đã có trong cây thì trả về false 
        if node is not None:
            return False
        # Ngược lại , thêm một nút mới. 
        else : 
            self._root = self._bstInsert(self._root,key)
            self.size += 1 
            return True 
    
    # Phương thức chèn một nút mới vào cây theo cách đệ quy 
    def _bstInsert(self,subtree,key): 
        if subtree is None: 
            subtree = _BSTreeNode(key)
        elif key < subtree.key : 
            subtree.left = self._bstInsert (self.left, key)
        elif key > subtree.key: 
            subtree.right = self._bstInsert(self.right, key)
        return subtree 
