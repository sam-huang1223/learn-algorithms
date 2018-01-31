"""
Implementation of a max heap
"""
import numpy as np

def build_max_heap():
    ''' returns a max heap from an unordered array'''
    pass

    def max_heapify():
        ''' correct a single violation of the heap property in a subtree '''
        pass

build_max_heap()


class Max_Heap:
    def __init__(self):
        self.heap = []

    def peak(self):
        assert len(self.heap) != 0, "Heap is empty"
        return self.heap[0]

    def extract(self):
        extracted_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap = self.heap[:-1]
        self._trickle_down(idx=0)
        return extracted_val

    def insert(self, value):
        ''' heap is an ordered binary tree (max heap -> value of parent always > child) runs n times'''
        self.heap.append(value)
        self._bubble_up(idx=int(len(self.heap)-1))

    def _trickle_down(self, idx):
        ''' runs in O(logn) time, but called n-1 times in heapsort '''
        left_child = idx*2 + 1
        right_child = idx*2 + 2
        if left_child >= len(self.heap):
            return
        elif right_child >= len(self.heap):
            max_child = left_child
        else:
            max_child = left_child if self.heap[left_child] > self.heap[right_child] else right_child

        if self.heap[idx] < self.heap[max_child]:
            self.heap[idx], self.heap[max_child] = self.heap[max_child], self.heap[idx]
            return self._trickle_down(idx=max_child)

    def _bubble_up(self, idx):
        parent_idx = int(max(np.ceil((idx-2)/2), 0))
        if self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            return self._bubble_up(idx=parent_idx)

if __name__ == '__main__':
    # [10, 9, 7, 6, 3, 6, 5, 4]
    h = Max_Heap()
    h.insert(4)
    h.insert(5)
    h.insert(6)
    h.insert(6)
    h.insert(3)
    h.insert(7)
    h.insert(9)
    h.insert(10)
    print(h.heap)
    print(h.extract())
    print(h.heap)


