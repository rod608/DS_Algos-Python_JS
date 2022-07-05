from data_structures.linked_list.singly_linked import SLinkedList


def test_creation(sll):
    """ Testing the Constructor. """
    assert isinstance(sll, SLinkedList)

    assert sll.is_empty()
    assert sll.head is None
    assert sll.size() == 0
    assert sll.__str__() == "SLL of size 0: "


def test_add_append(sll):
    """ Testing the 'append' & 'insert' functionality of the add() method. """
    sll.add(1)       # append  ; setting a new head
    sll.add(3)       # append
    sll.add(0, 0)    # prepend ; setting a new head
    sll.add(2, 2)    # insert

    assert not sll.is_empty()
    assert sll.head.data == 0
    assert sll.size() == 4
    assert sll.__str__() == "SLL of size 4: 0 -> 1 -> 2 -> 3"


def test_add_prepend(sll):
    """ Testing the 'prepend' & 'insert' functionality of the add() method. """
    sll.add(1, 0)  # prepend ; setting a new head
    sll.add(0, 0)  # prepend ; setting a new head
    sll.add(3)     # append
    sll.add(2, 2)  # insert

    assert not sll.is_empty()
    assert sll.head.data == 0
    assert sll.size() == 4
    assert sll.__str__() == "SLL of size 4: 0 -> 1 -> 2 -> 3"


def test_remove(sll):
    """ Testing the 'remove_first'/'remove_last' & 'remove' functionality of the remove() method. """
    # removing from empty sll
    sll.remove(0)
    assert sll.is_empty()

    # removing from sll of size 1
    sll.add(1)
    assert sll.size() == 1 and not sll.is_empty()
    sll.remove(0)
    assert sll.size() == 0 and sll.is_empty()

    # removing from sll of size 2
    sll.add(1)
    sll.add(2)
    assert sll.size() == 2 and not sll.is_empty()

    sll.remove(0)
    sll.remove(0)
    assert sll.size() == 0 and sll.is_empty()

    # removing from sll: 0 -> 1 -> 2 -> 3
    sll.add(1, 0)
    sll.add(0, 0)
    sll.add(3)
    sll.add(2, 2)

    sll.remove(0)  # rm 0
    sll.remove(2)  # rm 3
    assert sll.__str__() == "SLL of size 2: 1 -> 2"

    sll.remove(0)
    sll.remove(0)
    assert sll.size() == 0 and sll.is_empty()
