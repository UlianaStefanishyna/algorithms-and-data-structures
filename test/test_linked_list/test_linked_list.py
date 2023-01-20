from linked_list.linked_list import LinkedList, convert_arraylist_to_linked_list


def test_linked_list_fill_in_success():
    linked_list: LinkedList = convert_arraylist_to_linked_list([1, 2, 3, 4, 5, 6])
    assert linked_list.size() == 6


def test_linked_list_insert_at_position():
    linked_list: LinkedList = convert_arraylist_to_linked_list([1, 2, 3, 4, 5, 6])
    linked_list.insert_at_position(data=10, position=2)
    assert linked_list.size() == 7
    assert linked_list.get_at_position(position=2) == 10


def test_linked_list_remove_at_position():
    linked_list: LinkedList = convert_arraylist_to_linked_list([1, 2, 3, 4, 5, 6])
    linked_list.remove_at_position(position=2)
    assert linked_list.size() == 5
    assert linked_list.get_at_position(position=2) == 4
