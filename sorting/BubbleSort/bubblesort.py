def sort(array):
    if len(array) == 1:
        return array

    if array == []:
        return []

    for inx in range(len(array)):
        for jnx in range(len(array) - 1):
            if array[jnx] > array[jnx + 1]:
                (array[jnx] , array[jnx + 1]) = (array[jnx + 1], array[jnx])

if __name__ == "__main__":
    array = [10, 2, 11, 5, 1]
    sort(array)
    print(array)