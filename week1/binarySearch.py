def binarySearch(a, key, left, right):
    if left <= right :
        mid = (left + right) // 2
        if key == a[mid] :
            return mid
        elif key < a[mid] :
            return binarySearch(a, key, left, mid-1)
        elif key > a[mid] :
            return binarySearch(a, key, mid+1, right)
    else : return -1