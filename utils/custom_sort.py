def custom_sort(arr,sort_col_num=-1):
    '''
    :param arr:   [[1,2,3],[3,2,1]]
    :param sort_col_num:  排序的列，默认为最后一列
    :return:  [{},{}]
    '''
    length = len(arr)
    for index in range(length):
        flag = True
        for j in range(1,length - index):
            if arr[j-1][sort_col_num] > arr[j][sort_col_num]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                flag = False
        if flag:
            return arr
    return arr


