from __future__ import annotations

from typing import TYPE_CHECKING


class DoublyNode:
    def __init__(
        self,
        data: int,
        next_node: DoublyNode | None = None,
        previous_node: DoublyNode | None = None,
    ) -> None:
        self.data = data
        self.next = next_node
        self.previous = previous_node

    def __repr__(self) -> str:
        return f"<Node data={self.data}>"


class DoublyLinkedListIterator:
    def __init__(self, head: DoublyNode) -> None:
        self.current = head

    def __next__(self) -> int | None:
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


class DoublyLinkedList:
    def __init__(self, head: DoublyNode | None = None) -> None:
        self.head = head
        self.size = 0

    def __repr__(self) -> str:
        return f"<LinkedList size: {self.size}>"

    def is_empty(self) -> bool:
        return self.size == 0

    def add(self, data: int) -> None:
        """Adds a new node containing data at the head of the list."""
        new_node = DoublyNode(data, self.head)
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        self.size += 1

    def search(self, key: int) -> bool:
        """Searches for the first node containing data that matches the key."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def remove(self, key: int) -> None:
        """Removes the first occurrence of a node that contains the key."""
        current = self.head
        previous = None
        while current:
            if current.data == key:
                if previous:
                    previous.next = current.next
                    if current.next:
                        current.next.previous = previous
                else:
                    self.head = current.next
                    if current.next:
                        current.next.previous = None
                self.size -= 1
                return
            previous = current
            current = current.next

    def __iter__(self) -> DoublyLinkedListIterator:
        if self.head:
            return DoublyLinkedListIterator(self.head)

        raise StopIteration()

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index: int) -> DoublyNode | None:
        if index < 0 or index >= self.size:
            msg = "Index out of range"
            raise IndexError(msg)
        current = self.head
        for _ in range(index):
            if current:
                current = current.next
        return current

    def __setitem__(self, index: int, data: int) -> None:
        if index < 0 or index >= self.size:
            msg = "Index out of range"
            raise IndexError(msg)
        current = self.head
        for _ in range(index):
            if current:
                current = current.next

        if current:
            current.data = data

    def insert(self, index: int, data: int) -> None:
        """Inserts a new node containing data at the given
        index position."""

        if index < 0 or index > self.size:
            msg = "Index out of range"
            raise IndexError(msg)

        if index == 0:
            self.add(data)
            return

        current = self.head
        for _ in range(index - 1):
            if current:
                current = current.next

        if TYPE_CHECKING and current is None:
            # This is only for type checking purposes
            return

        new_node = DoublyNode(data, current.next, current)
        if current and current.next:
            current.next.previous = new_node

        if current:
            current.next = new_node
            self.size += 1

    def pop(self, index: int | None = None) -> int:
        """Removes the node at the given index position and returns its data.
        If no index is specified, removes and returns the last item in the list."""
        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            msg = "Index out of range"
            raise IndexError(msg)

        current = self.head
        for _ in range(index):
            if current:
                current = current.next

        if TYPE_CHECKING and current is None:
            # This is only for type checking purposes
            return 0

        data = current.data
        if current and current.previous:
            current.previous.next = current.next
        else:
            self.head = current.next
        if current and current.next:
            current.next.previous = current.previous
        self.size -= 1
        return data
