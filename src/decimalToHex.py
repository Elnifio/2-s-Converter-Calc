def num_hex_converter(in_num):
    if (in_num == 10):
        return 'A'
    elif (in_num == 11):
        return 'B'
    elif (in_num == 12):
        return 'C'
    elif (in_num == 13):
        return 'D'
    elif (in_num == 14):
        return 'E'
    elif (in_num == 15):
        return 'F'
    else:
        return str(in_num)

def hex_dec_converter(in_str):
    if (in_str == 'A') or (in_str == 'a'):
        return 10
    elif (in_str == 'B') or (in_str == 'b'):
        return 11
    elif (in_str == 'C') or (in_str == 'c'):
        return 12
    elif (in_str == 'D') or (in_str == 'd'):
        return 13
    elif (in_str == 'E') or (in_str == 'e'):
        return 14
    elif (in_str == 'F') or (in_str == 'f'):
        return 15
    else:
        return int(in_str)

def decimal_to_hex(in_num, hex_len=8):
    out_arr = ""
    for index in range(hex_len):
        quotient = in_num // 16
        mod = in_num - (16 * quotient)
        out_arr = num_hex_converter(mod) + out_arr
        in_num = quotient
    return(out_arr)

def hex_to_decimal(in_str):
    index = 0
    out = -(16 ** (len(in_str) - 1)) * hex_dec_converter(in_str[index])
    index += 1
    while index < len(in_str):
        out += (16 ** (len(in_str) - 1 - index)) * hex_dec_converter(in_str[index])
        index += 1
    return out
