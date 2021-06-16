def partition(array, low, high): #[3, 2, 1]  # [1, 2, 3]
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


def quicksort(array, start, end):
    if start < end:
        p = partition(array, start, end)
        print(p)
        quicksort(array, start, p - 1)
        quicksort(array, p + 1, end)

def quicksort2(array):
    if array == []:
        return []

    if len(array) == 1:
        return array

    pivot, *rest = array
    smaller = [element for element in array if element < pivot]
    bigger = [element for element in array if element > pivot]
    return quicksort2(smaller) + [pivot] + quicksort2(bigger)

if __name__ == "__main__":
    #array = [10, 2, 7, 8, 3, 1]
    array = [1, 2]
    # array = [8, 7, 2, 1, 0, 9, 6]
    print(quicksort2(array))
