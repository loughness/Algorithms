
to_sort = [13, 2, 63, 4, 18, 45, 37, 9]
def selection_sort(list):
    # the -1 is for when we only have 1 item left in the list,
    # we do not need to do a comparison on it, we just assume it is the highest value
    n = range(0, len(list)-1)
    h = 1

    for i in n:
        # assigning the first element to be the default min
        min_value = i

        # iterating through all element to the right of i
        for j in range(i+1, len(list)):
            # going through all elements and changing the min value if needed
            # powerful because we do not need to do a swap every time we find
            # the minimum value
            if list[j] < list[min_value]:
                min_value = j

            # if we find a value that is less than the default then we need to switch those
        if min_value != i:
            list[min_value], list[i] = list[i], list[min_value]
        print(f"Round {h} -> {list}")
        h += 1
    # return list

# print(selection_sort(to_sort))
selection_sort(to_sort)


def selection_sort2(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort2(to_sort))