from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a list in ascending order
    Returns sort linked list

    - Recursively divide the linked list into sublists containing a single bode
    - Repeated merge the sublists to produce sorted sublists until one remains
    Takes 0(log n) time
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublist - left and right

    Runs in overall 0(k log n) time
    """
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid -1)
        left_half = linked_list
        right_half = LinkedList
        right_half.head = mid_node.next_node()
        mid_node.next_node = None


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall 0(n log n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i]) 
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n==1:
        return True
    
    return list[0] < list[1] and verify_sorted[list[1:]]

alist = [12,131,2,32,12,232,12,2,1,9]
print(merge_sort(alist))