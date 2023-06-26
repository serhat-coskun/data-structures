
from typing import Collection

"""
    For a collection to be a heap:

        * For node x, x >= x.clidreen (Max heap)
        By law of transitivity, root is the maximum element
        This type of heap is called max-heap
        
        * Heap is a complete tree, that is we insert a new element
        to left most empty spot.
"""


class Heap:
    
    
    def __init__(self, collection: Collection = None, capacity = 10) -> None:
        if collection is not None:
            self.size = len(collection)
            self.capacity = self.size
            self.items = [e for e in collection]
            self.heapify()
        else:
            self.capacity = capacity
            self.size = 0
            self.items = [0 for _ in range(capacity)]
        
    def heapify(self, arr):
        pass
    
    def add(self, val):
        pass
    
    def peek(self):
        pass
    
    def pop(self):
        pass
    
    def __len__():
        pass

    def __bool__():
        pass
    
    
    """
        Note that we use zero indexing
    """
    def _leftIndex(self, index):
        return 2*index+1
    def _hasLeftChild(self, index):
        return self._leftIndex(index) < len(self)
    
    def _rigthIndex(self, index):
        return 2*index+2
    def _hasRightChild(self, index):
        return self._rigthIndex(index) < len(self)
    
    def _parentIndex(self, index):
        return (index - 2) / 2
    def _hasParent(self, index):
        return self._parentIndex >= 0