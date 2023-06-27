from typing import Collection
import math

"""
    For a collection to be a heap:

        * For node x, x >= x.clidreen (Max heap)
        By law of transitivity, root is the maximum element
        This type of heap is called max-heap
        
        * Heap is a complete tree, that is we insert a new element
        to left most empty spot.
"""


class Heap:
    """Defaults to min-heap
    To modify to max-heap: supply inOrderFunc lambda parent, child: parent < child

    """

    def __init__(self, inOrderFunc=None, collection: Collection = None) -> None:
        ## Defaults to max-heap
        ## Ensures that parent is greater than child
        if inOrderFunc is None:
            self.order = lambda parent, child: parent > child
        else:
            self.order = inOrderFunc

        if collection is not None:
            self.size = len(collection)
            self.items = [e for e in collection]
            self._heapify()
        else:
            self.size = 0
            self.items = []

    def add(self, val):
        # O(lg N)

        self.items.append(val)
        self.size += 1
        self._heapifyUp()

    def peek(self):
        # O(1)

        if not self:
            raise Exception("Heap is empty")

        return self.items[0]

    def pop(self):
        # O(lg N)
        if not self:
            raise Exception("Heap is empty")

        out = self.items[0]
        self.size -= 1

        ## If root was the only element just return
        if len(self) == 0:
            return out

        self.items[0] = self.items.pop()
        self._heapifyDown()
        return out

    def __len__(self):
        # O(1)
        return self.size

    def __bool__(self):
        # O(1)
        return len(self) != 0

    """
        Note that we use zero indexing
    """

    def _heapify(self):
        """Idea is to hapify smallest subtree, and build up from there"""
        parentOfLastNode = self._parent(len(self) - 1)
        for i in range(parentOfLastNode, -1, -1):
            self._heapifyDown(i)

    def _heapifyDown(self, index=0):
        # Called after root is popped and replace with last element

        parentIndex = index

        while self._hasLeftChild(parentIndex):
            ## Find the most parentish, child from left and right
            left = self._left(parentIndex)
            childIndex = self._leftIndex(parentIndex)

            if self._hasRightChild(parentIndex) and self.order(
                self._right(parentIndex), left
            ):
                childIndex = self._rigthIndex(parentIndex)

            ## Child is more parentish swap
            if self.order(self.items[childIndex], self.items[parentIndex]):
                self._swap(parentIndex, childIndex)
                parentIndex = childIndex
            else:
                break

    def _heapifyUp(self):
        # Called when new element is added
        # Newly added element is at the end

        childIndex = len(self) - 1

        ## Buble the child up, if child has parent and it is out of order
        while self._hasParent(childIndex) and self.order(
            self.items[childIndex], self._parent(childIndex)
        ):
            self._swap(childIndex, self._parentIndex(childIndex))
            childIndex = self._parentIndex(childIndex)

    def _leftIndex(self, index):
        return 2 * index + 1

    def _left(self, index):
        return self.items[self._leftIndex(index)]

    def _hasLeftChild(self, index):
        return self._leftIndex(index) < len(self)

    def _rigthIndex(self, index):
        return 2 * index + 2

    def _right(self, index):
        return self.items[self._rigthIndex(index)]

    def _hasRightChild(self, index):
        return self._rigthIndex(index) < len(self)

    def _parentIndex(self, index):
        return math.floor((index - 1) / 2)

    def _parent(self, index):
        return self.items[self._parentIndex(index)]

    def _hasParent(self, index):
        return self._parentIndex(index) >= 0

    def _swap(self, indexFirst, indexSecond):
        temp = self.items[indexFirst]
        self.items[indexFirst] = self.items[indexSecond]
        self.items[indexSecond] = temp
