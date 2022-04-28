
to_sort = [13, 2, 63, 4, 18, 45, 37, 9]
def bubbleSort(list):
    n = len(list)
    h = 1
    for i in range(n-1):
        flag = 0
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(f"Round {h} -> {list}")
            h += 1
        if flag == 0:
            break
    return list

def bubble(list):
    # need to get the length of what we will be comparing
    # the -1 is because we cannot perform a comparison on the last item of the list : index out of range
    n = len(list) - 1
    # This will be used to break us out of the loop when list is sorted
    sorted = False
    # for round counting
    h = 1

    while not sorted:
        #
        sorted = True
        for i in range(0,n):
            # after sorting all items, this if statement won't activate
            # so the sorted variable will remain true as stated above
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
                print(f"Round {h} -> {list}")
                h += 1


# bubbleSort(to_sort)
bubble(to_sort)