class Node:
    """ A Node created for singly-linked lists. Contains Data and a Reference to the next node. """

    def __init__(self, data=None):
        """ Constructor. Called when instantiating nodes. """
        self.data = data  # Supply w/ data passed as the argument.
        self.next = None  # The node at end of the Singly-Linked List will always point to None.


class SLinkedList:  # Space Complexity: O(n)
    """
    - A class that represents Singly-Linked Lists; A Sequence of elements that are connected together by links.
    - It's comprised of its head, nodes w/ pointers, and tail.
    Operations: add(E), add(pos, E), remove(pos), get(E), contains(E), size(), isEmpty()
    """

    def __init__(self):
        """ Constructor. Initializes an empty linked list of size 0, meaning the head node is currently nothing. """
        self.head: Node = None  # The Node at the front! Initially non-existent.
        self._size: int = 0     # Keep track of the size as we add and delete nodes.

    def add(self, data, pos=-1) -> None:  # O(n)
        """ Add Method. Creates a Node w/ the data argument. Will be treated as 'append' if no position is supplied. """
        # Prepend Edge Case: pos == 0
        if pos == 0:
            self._add_first(data)

        # Exception Edge Case: pos Out Of Bounds
        elif pos >= self._size or pos < -1:
            return

        # Append Edge Case: pos not given
        elif pos == -1:
            self._add_last(data)  # Helper Method
            return

        # Otherwise, Insert the New Node
        else:
            # Create a Traversal Pointer that ends up at the index (pos - 1)
            cur_node = self.head
            cur_idx = 0
            while cur_idx != pos - 1:
                cur_node = cur_node.next
                cur_idx += 1

            # Insert the new_node. Set new_node.next to the node at index pos, and update cur_node.next to new_node.
            new_node = Node(data)
            new_node.next = cur_node.next
            cur_node.next = new_node

            # Don't forget to increment the size!
            self._size += 1

    def _add_first(self, data) -> None:
        """ Prepend Method. Creates a node w/ the data supplied as an argument and inserts it into the 1st position. """
        new_node = Node(data)

        # Edge Case: The head doesn't exist yet. Set the new node as the head instantly.
        if self.head is None:  # Could use isEmpty() as condition instead.
            self.head = new_node

        # Otherwise, Prepend. Point the new_node to a copy of head and set the new_node as the new head.
        else:
            head_copy = Node(self.head.data)
            head_copy.next = self.head.next
            self.head = new_node
            self.head.next = head_copy

        # No matter what, update the size
        self._size += 1

    def _add_last(self, data) -> None:
        """ Append Method. Create a Node w/ the data argument and add on to the end of the Singly-Linked List. """
        new_node = Node(data)

        # Edge Case: The head doesn't exist yet. Set the new node as the head instantly.
        if self.head is None:  # Could use isEmpty() as condition instead.
            self.head = new_node

        # Traverse the Singly-Linked List until the end and append the new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

        # No matter what, update the size
        self._size += 1

    def remove(self, pos) -> None:
        """ Remove Method. Remove the Node at the index: (pos). """
        # Shift Edge Case: pos == 0
        if pos == 0:
            self._remove_first()
            return

        # Exception Edge Case: pos Out Of Bounds
        elif pos < 0 or pos >= self._size:
            return

        # Pop Edge Case: pos == size() - 1
        elif pos == self._size - 1:
            self._remove_last()
            return

        # Normal Removal Case: 0 < pos < (size() -1)
        else:
            next_node = self.head
            cur_idx = 0
            while cur_idx != pos + 1:
                next_node = next_node.next
                cur_idx += 1

            prev_node = self.head
            cur_idx = 0
            while cur_idx != pos - 1:
                prev_node = prev_node.next
                cur_idx += 1

            del prev_node.next
            prev_node.next = next_node

    def _remove_first(self) -> None:
        """ Shift Method. Removes the Node at the first index. """
        # Exception Edge Case: Empty SLL
        if self.is_empty():
            return

        # Edge Case: Only one element remains.
        elif self.size() == 1:
            self.head: Node = None

        # Since we're removing the current head, we need to set a new one.
        else:
            self.head = self.head.next

        # No matter what, decrement the size().
        self._size -= 1

    def _remove_last(self) -> None:
        """ Pop Method. Removes the Node at the last index. """
        # Traverse the SLL until the removal target is reached.
        cur_node = self.head
        cur_idx = 0
        while cur_idx < self._size - 2:
            cur_node = cur_node.next
            cur_idx += 1

        del cur_node.next
        cur_node.next = None

        # Decrement the size.
        self._size -= 1

    def set(self, data, pos) -> None:  # O(n)
        """ Set Method. Sets the value of an existing Node to another one. """
        # Out of Bounds Edge Case: pos < 0 or pos >= size()
        if pos < 0 or pos >= self._size:
            return

        # Traverse to the node at the given index (pos)
        else:
            cur_node = self.head
            cur_idx = 0
            while cur_idx != pos:
                cur_node = cur_node.next
                cur_idx += 1

            # Set its data value to the data argument.
            cur_node.data = data

    def get(self, pos):  # O(n)
        """ Get Method. Returns the data within the node at the given index. """
        # Out of Bounds Edge Case: pos < 0 or pos >= size()
        if pos < 0 or pos >= self._size:
            return

        # Traverse to the node at the given index (pos)
        cur_node = self.head
        cur_idx = 0
        while cur_idx != pos:
            cur_node = cur_node.next
            cur_idx += 1

        # Return cur_node as it is now == sll[pos]
        return cur_node.data

    # Not Necessary, but Useful Methods Below!

    def size(self) -> int:  # O(1)
        """ Size Method: Get the current # of elements in the Linked List. """
        return self._size

    def is_empty(self) -> bool:  # O(1)
        """ isEmpty Method: Returns the List's status in terms of emptiness. """
        return True if self.head is None else False

    def __str__(self) -> str:  # O(n)
        """ toString Method: Provides a visual representation of the SLL as a String. """
        rtn_list: list[str] = []

        cur_node = self.head
        while cur_node is not None:
            rtn_list.append(f"{cur_node.data}")
            cur_node = cur_node.next

        rtn_str = f"SLL of size {self._size}: " + " -> ".join(rtn_list)
        return rtn_str
