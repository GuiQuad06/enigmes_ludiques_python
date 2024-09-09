def bin2int_big_endian(bin):
    return bin2int_little_endian(bin[::-1])


def bin2int_little_endian(bin):
    num = 0
    for i in range(0, len(bin), 1):
        num += pow(2, i) * int(bin[i], 2)
    return num
