def cmp(a, j, jmin):
    return a[j] < a[jmin]   # return True if new min found


def swap(a, i, jmin):
    temp = a[i]  # holding a[i] so it is not lost in the swap
    a[i] = a[jmin]  # swapping values
    a[jmin] = temp


def sort(a, cmp=cmp, swap=swap):
    # empty array case, inherently sorted
    if a == []:
        return a
    # length 1 case, inherently sorted
    if len(a) == 1:
        return a

    for i in range(len(a) - 1):  # iterate start of each successive partition
        jmin = i  # set default minimum index to start of partition
        for j in range(i + 1, len(a)):  # iterate through partition
            if cmp(a, j, jmin):  # current value less than value at min index?
                jmin = j  # update new minimum index
        swap(a, i, jmin)  # swap minimum to front of partition

    return a  # return sorted array
