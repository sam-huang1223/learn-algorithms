'''
Linked Lists
Pros:
1) Add/remove beginning is O(1), O(n) for arrays
Cons:
1) Add/remove end is O(n), O(1) for arrays if empty space
2) Access is O(n), O(1) for arrays
3) Extra space is required to deal with the links
'''

class LL_Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Singly_LL:
    def __init__(self, head=None):
        ''' Front is the head, back is the tail of nodes '''
        self.head = head

    def pushFront(self, value):
        self.head = LL_Node(value, self.head)

    def peekFront(self):
        return self.head

    def popFront(self):
        item = self.head.value
        self.head = self.head.next
        return item

    def pushBack(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = LL_Node(value)

    def peekBack(self):
        current = self.head
        while current.next:
            current = current.next
        return current.value

    def popBack(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def contains(self, value):
        ''' return boolean '''
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next


    def addAfter(self, given_value, add_value):
        current = self.head
        while current:
            if current.value == given_value:
                current.next = LL_Node(value=add_value, next=current.next)
                return

    def addBefore(self, given_value, add_value):
        if self.head.value == given_value:
            self.head = LL_Node(value=add_value, next=self.head)
            return  # not adding value more than once if duplicates exist

        current = self.head
        while current.next:
            if current.next.value == given_value:
                current.next = LL_Node(value=add_value, next=current.next)
                return
            current = current.next

    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

if __name__ == '__main__':
    LL = Singly_LL()
    LL.pushFront(5)
    LL.pushFront(7)
    LL.pushFront(9)
    LL.pushBack(11)
    LL.print_values()
    print(LL.peekBack())
    print(LL.contains(11))
    LL.popBack()
    LL.print_values()
    print(LL.contains(11))
    LL.remove(7)
    LL.print_values()
    LL.addAfter(9, 8)
    LL.print_values()
    print(LL.contains(8))
    LL.addBefore(5, 10)
    LL.print_values()
