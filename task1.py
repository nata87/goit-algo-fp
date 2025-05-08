class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self

    def bubble_sort(self):
        i = self.head
        while i and i.next:
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            i = i.next
        return self

def merge_sorted(l1, l2):
    res = LinkedList()
    cur1 = l1.head
    cur2 = l2.head

    while cur1 and cur2:
        if cur1.data < cur2.data:
            res.insert_at_end(cur1.data)
            cur1 = cur1.next
        else:
            res.insert_at_end(cur2.data)
            cur2 = cur2.next

    while cur1:
        res.insert_at_end(cur1.data)
        cur1 = cur1.next
    while cur2:
        res.insert_at_end(cur2.data)
        cur2 = cur2.next

    return res

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_beginning(42)
    llist.insert_at_beginning(8)
    llist.insert_at_beginning(13)
    llist.insert_at_end(27)
    llist.insert_at_end(3)

    print("Зв'язний список:")
    llist.print_list()

    reversed_list = llist.reverse_list()
    print("Reversed:")
    reversed_list.print_list()

    sorted_list = llist.bubble_sort()
    print("Sorted:")
    sorted_list.print_list()

    llist1 = LinkedList()
    llist1.insert_at_beginning(14)
    llist1.insert_at_beginning(9)
    llist1.insert_at_beginning(31)
    llist1.insert_at_end(5)
    llist1.insert_at_end(20)

    sorted1 = llist1.bubble_sort()
    print("Sorted1:")
    sorted1.print_list()

    print("Merged:")
    merged = merge_sorted(sorted_list, sorted1)
    merged.print_list()
