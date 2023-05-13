def Quicksort(arr):
    qshelper(arr, 0, len(arr) - 1)
    return arr


def qshelper(arr, start, end):
    # --------for pivot at end--------------#

    # pivot = end
    # left = start
    # right = end-1

    # --------------for pivot at start-----------------#

    pivot = start
    left = start + 1
    right = end

    # ----------for pivot at mid-----------#

    # pivot = len(arr) // 2
    # left = pivot + 1
    # right = end

    if start >= end:
        return

    while left <= right:

        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1

    # -------------for pivot at end-------------#
    # arr[left], arr[pivot] = arr[pivot], arr[left]

    # ------------for pivot at mid or start-------------#
    arr[right], arr[pivot] = arr[pivot], arr[right]

    qshelper(arr, right + 1, end)
    qshelper(arr, start, right - 1)


arr = list(map(int, input("Enter the elements(space separated):\n").split()))
# arr = [1,4,7,2]
print(Quicksort(arr))
