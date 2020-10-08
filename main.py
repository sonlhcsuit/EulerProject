def collazt(threshold=int(1e6)):
    """
    using this function to calculate number of collazt sequence elements starting at k (k is from 0 to threshold)
    using dymanic programing to store number of collazt-sequence-elements starting at k (caching)
    :param threshold:
    :return:
    """
    counting = [-1 for _ in range(threshold)]

    for i in range(1,threshold):
        collazt_number = i
        count = 0
        # print('---------------------')
        # print('{} is processing'.format(i))
        while collazt_number != 1:
            # print(collazt_number)
            collazt_number = collazt_number//2 if collazt_number% 2 ==0 else collazt_number*3 + 1
            if collazt_number < threshold and collazt_number < i:
                if counting[collazt_number] != -1:
                    # print('sub',collazt_number)
                    count = counting[collazt_number] + count
                    break
            count+=1
        count+=1
        # print('counting {} is {}'.format(i,count))
        counting[i] = count
    return counting

answ = collazt()
print('finding complete')
print(answ.index(max(answ)))