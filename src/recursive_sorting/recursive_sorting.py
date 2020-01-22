# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            del arrA[0]
        else:
            merged_arr.append(arrB[0])
            del arrB[0]
    if len(arrA) > 0:
        merged_arr.extend(arrA)
    if len(arrB) > 0:
        merged_arr.extend(arrB)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if length is 1, stop
    if len(arr) > 1:
        # split in half
        newArr1 = arr[:len(arr)//2]
        newArr2 = arr[len(arr)//2:]

        return merge(merge_sort(newArr1), merge_sort(newArr2))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
