to_sort = [13, 2, 63, 4, 18, 45, 37, 9]

def mergeSort(list):
    # if the length is less than 1, it can't do anything
    if len(list) > 1:
        # list divides - left -> beginning to the length divided by 2
        left_list = list[:len(list)//2]
        # list divided - right -> middle of list to end
        right_list = list[len(list)//2:]

        # recursion call
        # do the merge sort on both the left and right sides
        # resulting in correct order
        mergeSort(left_list)
        mergeSort(right_list)

        # merge step
        # comparing left most element on one array to the left most of other array
        # i to keep track of left side
        i = 0
        # j to keep track of right side
        j = 0
        # merged array index
        k = 0

        while i < len(left_list) and j < len(right_list):
            # comparing left at i to right at j
            if left_list[i] < right_list[j]:
                # saving value of left array inside the merged array
                list[k] = left_list[i]
                # increasing i
                i += 1
                print(to_sort)
            # since about is used for less than, 'else' will be used for greater than
            else:
                list[k] = right_list[j]
                j += 1
                print(to_sort)
            # increment k -> kept out of if else statement as they would both have to increment it anyway
            k += 1

        # still have elements to move from left array into merged array
        # check that we are not at the end of left array
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
            print(to_sort)
        # now we have some missing elements from right array
        # check that we are not at the end of right array
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
            print(to_sort)
        # this code will save the given list as the correct order

mergeSort(to_sort)

print(to_sort)





