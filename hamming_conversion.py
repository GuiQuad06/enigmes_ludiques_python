
def bin2int_big_endian(bin):
    return bin2int_little_endian(bin[::-1])


def bin2int_little_endian(bin):
    num = 0
    for i in range(0, len(bin), 1):
        num += pow(2, i) * int(bin[i], 2)
    return num


def detect_err(data):
    test_c5 = (data[0] + data[1] + data[2]) % 2
    test_c6 = (data[0] + data[1] + data[3]) % 2
    test_c7 = (data[1] + data[2] + data[3]) % 2

    if test_c5 != data[4] and test_c6 != data[5] and test_c7 == data[6]:
        index_err = 0
    elif test_c5 != data[4] and test_c6 != data[5] and test_c7 != data[6]:
        index_err = 1
    elif test_c5 != data[4] and test_c6 == data[5] and test_c7 != data[6]:
        index_err = 2
    elif test_c5 == data[4] and test_c6 != data[5] and test_c7 != data[6]:
        index_err = 3
    elif test_c5 != data[4] and test_c6 == data[5] and test_c7 == data[6]:
        index_err = 4
    elif test_c5 == data[4] and test_c6 != data[5] and test_c7 == data[6]:
        index_err = 5
    elif test_c5 == data[4] and test_c6 == data[5] and test_c7 != data[6]:
        index_err = 6
    else:
        # No error
        index_err = -1
    return index_err

def correct_err(data, index):
    data[index] = data[index] ^ 1
    return data
