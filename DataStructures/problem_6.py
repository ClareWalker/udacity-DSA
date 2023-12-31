class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_set = set()
    if llist_1 is not None:
        node = llist_1.head
        while node:
            union_set.add(node.value)
            node = node.next

    if llist_2 is not None:
        node = llist_2.head
        while node:
            union_set.add(node.value)
            node = node.next

    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)

    return union_list


def intersection(llist_1, llist_2):
    set_1 = set()
    if llist_1 is not None:
        node = llist_1.head
        while node:
            set_1.add(node.value)
            node = node.next

    set_2 = set()
    if llist_2 is not None:
        node = llist_2.head
        while node:
            set_2.add(node.value)
            node = node.next

    intersection_set = set_1.intersection(set_2)

    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list



## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3, linked_list_4))
print (intersection(linked_list_3, linked_list_4))

## Test Case 3: Empty Lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))  # Expected: Empty Linked List
print(intersection(linked_list_5, linked_list_6))  # Expected: Empty Linked List

## Test Case 4: Null Lists
linked_list_7 = None

print(union(linked_list_7, linked_list_4))  # Expected: Linked List 4
print(intersection(linked_list_7, linked_list_4))  # Expected: Empty Linked List

## Test Case 5: Large Lists
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

# Creating large linked lists with random values
element_1 = [i for i in range(100)]
element_2 = [i for i in range(100, 200)]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))  # Expected: Linked List with values from 0 to 199
print(intersection(linked_list_9, linked_list_10))  # Expected: Empty Linked List
