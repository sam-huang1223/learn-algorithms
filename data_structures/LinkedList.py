'''
Linked Lists
Pros:
1) Add/remove beginning is O(1), O(n) for arrays
2)
Cons:
1) Add/remove end is O(n), O(1) for arrays if empty space
2) Access is O(n), O(1) for arrays
'''

class LL_Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Singly_LL:
    def __init__(self):
        ''' Front is the head, back is the tail of nodes '''
        self.head = None

    def pushFront(self, value):
        ''' O(1) '''
        pass

    def peekFront(self):
        ''' O(1) '''
        pass

    def popFront(self):
        ''' O(1) '''
        # when removing element, use del [name] to remove from memory
        pass

    def pushBack(self, value):
        pass

    def peekBack(self):
        pass

    def popBack(self):
        pass

    def contains(self, value):
        ''' return boolean '''
        return True

    def remove(self, value):
        ''' find and remove value '''
        pass

    def addAfter(self, given_value, add_value):
        pass

    def addBefore(self, given_value, add_value):
        pass
