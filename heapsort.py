def swap(arg, i, j):
    temp = arg[i]
    arg[i] = arg[j]
    arg[j] = temp

def heapify(arg, parent, limit):
    swap_idx = parent
    left_child = int(2 * parent + 1)
    if left_child <= limit and arg[swap_idx] < arg[left_child]:
        swap_idx = left_child
    right_child = int(2 * parent + 2)
    if right_child <= limit and arg[swap_idx] < arg[right_child]:
        swap_idx = right_child
    if swap_idx != parent:
        swap(arg, swap_idx, parent)
        heapify(arg, swap_idx, limit)

def build_heap(arg, right_idx):
    last_parent = int((right_idx - 1) / 2)
    while last_parent >= 0:
        heapify(arg, last_parent, right_idx)
        last_parent -= 1

# Complexity: O( n * log(n) )
def heapsort(arg):
    print("Unsorted: " + str(arg))
    l = len(arg) - 1
    while l >= 1:
        build_heap(arg, l)
        swap(arg, 0, l)
        l -= 1
    print("Sorted: " + str(arg))


arg_array = [6, 5, 3, 1, 8, 7, 2, 4]
heapsort(arg_array)
