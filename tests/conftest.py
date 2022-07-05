import pytest
from data_structures.linked_list.singly_linked import SLinkedList


# Singly-Linked List
@pytest.fixture()
def sll() -> SLinkedList:
    return SLinkedList()
