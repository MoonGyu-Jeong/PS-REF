"""
Binary Indexed Tree(BIT) / Fenwick Tree
https://gist.github.com/rajatdiptabiswas/79fc1ce5cf410df4139b291f75bf0794
"""

def update(index, value, array, bi_tree):
    """
    Updates the binary indexed tree with the given value
    
    index: index at which the update is to be made
    value: the new element at the index
    array: the input array
    bi_tree: the array representation of the binary indexed tree
    return: void
    """

    while index < len(array):
        bi_tree[index] += value
        index += index & -index

def get_sum(index, bi_tree):

    """
    Calculates the sum of the elements from the beginning to the index

    index: index till which the sum is to be calculated
    bi_tree: the array representation of the binary indexed tree
    return: (integer) sum of the elements from beginning till index
    """

    ans = 0
    while index > 0:
        ans += bi_tree[index]
        index -= index & -index
    return ans

def get_range_sum(left, right, bi_tree):

    """
    Calculates the sum from the given range

    bi_tree: the array representation of the binary indexed tree
    left: left index of the range(1-indexed)
    right: right index of the range(1-indexed)
    return: (integer) sum of the elements in the range
    """

    ans = get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)
    return ans

def main():
    n = int(input('Enter the number of elements: '))
    arr = [int(x) for x in input(f'Enter the {n} elements of the array: ').split()]
    arr.insert(0, 0)
    bit = [0 for i in range(n+1)]

    for index in range(1, n+1):
        update(index, arr[index], arr, bit)

    l, r = map(int, input('Enter the left and right indices for the range sum: ').split())
    print(get_range_sum(l, r, bit))
    print(arr)
if __name__ == '__main__':
    main()