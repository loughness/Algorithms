to_sort = [13, 2, 63, 4, 18, 45, 37, 9]

def quickSort(sequence):
    length = len(sequence)
    # this allows us to skip over values with a sequence length of 1 or 0
    if length <= 1:
        return sequence
    else:
        # pop() will remove and return last element in sequence
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    # iterating through each item in sequence
    for item in sequence:
        # if the item we are iterating over is greater than pivot point
        if item > pivot:
            # add the item to the greater items list
            items_greater.append(item)
        # if the item is less than the pivot or equal
        else:
            # add it to the less than list
            items_lower.append(item)


    # the return will then apply this algorithm again to each of the items lower,
    # then add the pivot point in the center then we apply the algorithm again,
    # to the items greater
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


print(quickSort(to_sort))