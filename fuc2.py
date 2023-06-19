def func2(nums, start, end):
    stack = [end, start]
    while stack:
        high = stack.pop()
        low = stack.pop()
        index = partition(nums, low, high)
        if low < index-1:
            stack.insert(0, low)
            stack.insert(0, index-1)
        if high > index+1:
            stack.insert(0, index+1)
            stack.insert(0, high)
    return nums
