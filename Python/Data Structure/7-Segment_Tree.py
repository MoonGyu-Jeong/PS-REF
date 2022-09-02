def merge(left, right):
    return left + right

# stree: list contains segment tree's information
# node: node number which currently being explored
# left, right: range of node application
def build(stree, node, left, right):
    # leaf node
    if left == right:
        stree[node] = num_lst[left]
        return stree[node]

    mid = left + (right - left) // 2
    left_val = build(stree, 2*node, left, mid)
    right_val = build(stree, 2*node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]

if __name__ == '__main__':
    print('==segment tree==')
    num_lst = [1, 2, 5, 3, 9, 6, 5, 3, 2]
    print(f'num_lst: {num_lst}')

    # create segment tree
    stree = [0 for x in range(4*len(num_lst))]
    build(stree, 1, 0, len(num_lst)-1)
    print(stree)
    print(stree[1])
    print(stree[2], stree[3])
    print(stree[4], stree[5], stree[6], stree[7])
    print(stree[8], stree[9], stree[10], stree[11], stree[12], stree[13], stree[14], stree[15])
    print(stree[16], stree[17])
