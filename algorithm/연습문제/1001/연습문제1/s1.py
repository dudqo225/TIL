my_list = [11, 3, 6, 4, 12, 1, 2]

def selection_sort_recursion(arr):
    if len(arr) == 1:
        return arr
    else:
        min_val = min(arr)
        arr.remove(min_val)
        return [min_val] + selection_sort_recursion(arr)

print(selection_sort_recursion(my_list))