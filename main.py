import linkedlist


def test_append(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    print("APPEND TEST")
    print(f"Starting value: {test_list[:1]}")
    print(f"Appending {test_list[1:]}")
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("v Result v")
    new_list.print_list()


def test_prepend(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    print("PREPEND TEST")
    print(f"Starting value: {test_list[:1]}")
    print(f"Prepending {test_list[1:]}")
    for i in range(1, len(test_list)):
        new_list.prepend(test_list[i])
    print("v Result v")
    new_list.print_list()


def test_pop_one_elem(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    print("POP WITH ONE ELEM TEST")
    print(f"Starting value: {test_list[:1]}")
    new_list.pop()
    print("v Result v")
    new_list.print_list()


def pop_test(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("POP LAST ELEM FULL LIST")
    print("Starting list:", end=" ")
    print(new_list.print_list())
    new_list.pop()
    print("v Result v")
    new_list.print_list()


def pop_front(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("POP FIRST ELEM FULL LIST")
    print("Starting list:", end=" ")
    print(new_list.print_list())
    new_list.pop_front()
    print("v Result v")
    new_list.print_list()


def test_get(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("Test Get Value")
    print("Index to get: 2")
    print(f"Value Should Be: {test_list[2]} ")
    print("v Result v")
    print(new_list.get(2))


def test_change_value(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("Test Change Value")
    print(f"Change Value of {test_list[2]} to 75")
    new_list.set_value(2, 75)
    print("v Result v")
    new_list.print_list()


def test_insert(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("Test Insert")
    print(f"Insert 51 at index 2")
    print("Current list:", *test_list)
    new_list.insert(51, 2)
    print("v Result v")
    new_list.print_list()


def test_remove(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("Test Remove")
    print("Remove at index 2")
    print("Current list:", *test_list)
    new_list.remove(2)
    print("v Result v")
    new_list.print_list()


def test_reverse(test_list: []):
    new_list = linkedlist.LinkedList(test_list[0])
    for i in range(1, len(test_list)):
        new_list.append(test_list[i])
    print("Test Reverse")
    print("Current list:", *test_list)
    new_list.reverse()
    print("v Result v")
    new_list.print_list()


if __name__ == "__main__":
    test_list = [5, 25, 30, 40, 10]
    print("================")
    test_append(test_list)
    print("================")
    test_pop_one_elem(test_list)
    print("================")
    pop_test(test_list)
    print("================")
    test_prepend(test_list)
    print("================")
    pop_front(test_list)
    print("================")
    test_get(test_list)
    print("================")
    test_change_value(test_list)
    print("================")
    test_insert(test_list)
    print("================")
    test_remove(test_list)
    print("================")
    test_reverse(test_list)
