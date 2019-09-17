def octal_to_decimal(in_num):
    index = 0
    out = -(8 ** (len(in_num) - 1)) * int(in_num[index])
    index += 1
    while index < len(in_num):
        out += (8 ** (len(in_num) - 1 - index)) * int(in_num[index])
        index += 1
    return out

def decimal_to_octal(in_num, bin_len=8):

    out_arr = ""
    for index in range(bin_len):
        quotient = int(in_num) // 8
        mod = int(in_num) - (8 * quotient)
        out_arr = str(mod) + out_arr
        in_num = quotient
    return(out_arr)