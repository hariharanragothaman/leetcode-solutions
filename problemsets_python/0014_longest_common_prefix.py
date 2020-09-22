def longest_common_prefix(strs):
    op = ''
    for d in zip(*strs):
        if len(set(d)) == 1:
            op += d[0]
        else:
            break
    return op

