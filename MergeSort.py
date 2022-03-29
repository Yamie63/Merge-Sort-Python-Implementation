def MergeSort(array):
    #if singular, no comparison needed
    if len(array) == 1:
        return array

    #find midpoint of array
    midpoint = int(len(array)/2)
    
    #split array into two
    left = array[:midpoint]
    right = array[midpoint:]

    #split each side of array again if not singular
    MergeSort(left)
    MergeSort(right)

    #index variables
    i = j = k = 0

    #iterate through left and right at the same tiem, if current left number < current right number, add left number to the new sorted array
    #else, add right number to the new sorted array. Increase count variables like one to progress and so on and so forth.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
        print(str(array))

    #If we've progressed onto this bit of code, we've reached the end of left or right and i or j now the length of their respective side
    #This leaves us with a series of sorted values in the unfinished side which we know are bigger than those in the sorted array
    #so just need to be added onto the end. Check if i or j is the incomplete side (check if value under length) then simply add 
    #all remaining values to the array.
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
        print(str(array))

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
        print(str(array))

toSort = [89, 7, 56, 60, 4, 9, 34, 27]
MergeSort(toSort)