to_sort = [13, 2, 63, 4, 18, 45, 37, 9]

def insertion_sort(list):
    # the first item in the list is already in sorted list
    # therefore in the range we go from 1
    indexing_length = range(1, len(list))
    for i in indexing_length:
        value_to_sort = list[i]
        h = 1

        # if the value to the left of selected value is less than the selected value
        # python allows for negative indexing, this stops us from comparing the value
        # in our unsorted list; i.e: index = -1
        while list[i-1] > value_to_sort and i > 0:
            # swapping the values if need be
            list[i], list[i-1] = list[i-1], list[i]
            # incrementally stepping down the list using the i variable
            i = i-1
            print(list)


    return f"Sorted list -> {list}"

print(insertion_sort(to_sort))



