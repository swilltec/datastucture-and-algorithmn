
array = [4, 23, 32, 12, 31, 50]

def insertion_sort(array):
    for i in range(1, len(array)):
        element_to_sort = array[i]

        while array[i-1] > element_to_sort and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
   
    return array

print(insertion_sort(array))
