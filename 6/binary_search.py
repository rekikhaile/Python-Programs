
def binary_search_helper(a, left, right, x):
    if left >= right:
        return -1

    mid = (right + left) // 2
    # print('middle index is now {}'.format(mid))
    # print('the middle element is {}'.format(a[mid]))
    
    if a[mid] == x:
        return mid

    elif a[mid] > x:
        # print('Traversing on {}'.format(a[left:mid]))
        return binary_search_helper(a, left, mid, x)
              
    # print('Traversing on {}'.format(a[mid+1:right]))
    return binary_search_helper(a, mid+1, right, x)

def binary_search(a, x):
    left, right = 0, len(a)
    return binary_search_helper(a, left, right, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

