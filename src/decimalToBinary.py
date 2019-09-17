def binary_to_decimal(in_num):
    # 因为这个函数本身只是在main内调用，所以并没有写类型判断 
    # i.e., if type(in_num) is not list...
    # Because I did not expect any usage of this function outside main.py
    # I did not add any if type(in_num) is not list... to check the type of input.
    
    index = 0
    out = -(2 ** (len(in_num) - 1)) * int(in_num[index])
    index += 1
    while index < len(in_num):
        out += (2 ** (len(in_num) - 1 - index)) * int(in_num[index])
        index += 1
    return out

def decimal_to_binary(in_num, bin_len=8):

    out_arr = ""
    for index in range(bin_len):
        quotient = int(in_num) // 2
        mod = int(in_num) - (2 * quotient)
        out_arr = str(mod) + out_arr
        in_num = quotient
    return(out_arr)
