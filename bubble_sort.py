
array = [4, 23, 32, 12, 31, 50]


def bubble_sort(array):
    indexing_length = len(array) - 1
    sorted = False

    while not sorted:
        sorted =True
        for i in range(indexing_length):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    return array

# def bubble_sort2(array):
#     last_element_idx = len(array) - 1
#     for passes in range (last_element_idx, 0, -1):
#         for idx in range(passes):
#             if array[idx] > array[idx +1]:


print(bubble_sort(array))