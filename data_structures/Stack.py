from .LinkedList import Singly_LL

class Stack:
    def __init__(self):
        ''' create an empty stack (implemented using linked lists) '''
        self.data = Singly_LL()

    def push(self, string):
        ''' insert a new string onto the stack '''
        self.data.pushFront(string)

    def pop(self):
        ''' remove and return the string most recently added '''
        return self.data.popFront()

    def peek(self):
        ''' returns the top element of the stack '''
        return self.data.peekFront()

    def popat(self):
        ''' remove and return the string at a specific index (count starting from the top) '''
        # TODO implement
        pass

    def isempty(self):
        ''' returns boolean representing whether stack is empty '''
        if self.data.head is None:
            return True
        else:
            return False

    def get_size(self):
        ''' returns the size of the stack '''
        count = 0
        current = self.data.head
        while current:
            count += 1
            current = current.next
        return count

class ArrayStack:
    def __init__(self):
        pass


if __name__ == '__main__':
    stack = Stack()
    print(stack.isempty())
    stack.push('poop0')
    stack.push('poop1')
    stack.push('poop2')
    print(stack.isempty())
    print(stack.get_size())
    stack.pop()
    stack.data.print_values()
