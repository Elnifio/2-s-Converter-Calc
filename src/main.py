import re
from decimalToHex import *
from decimalToBinary import *
from decimalToOctal import *

BINARY = {"Name": "BIN", "Code": r'^((0|1)+)$', "Base": 2, "Input_Options": ["bin", "binary", "bit", "bits", "b", "2", "two"], "To_Dec": binary_to_decimal, "Dec_To": decimal_to_binary}
OCTO = {"Name": "OCT", "Code": r'^0([0-7]*)$', "Base": 8, "Input_Options": ["oct", "octo", "octal", "o", "8", "eight"], "To_Dec": octal_to_decimal, "Dec_To": decimal_to_octal}
DECIMAL = {"Name": "DEC", "Code": r'^([0-9\-]*)$', "Base": 10, "Input_Options": ["dec", "decimal", "d", "10", "ten"], "To_Dec": lambda x: x, "Dec_To": lambda x: str(x)}
HEX = {"Name": "HEX", "Code": r'^0x([0-9A-Fa-f]+)$', "Base": 16, "Input_Options": ["hex", "hexadecimal", "h", "16", "sixteen"], "To_Dec": hex_to_decimal, "Dec_To": decimal_to_hex}
BASES = [BINARY, OCTO, DECIMAL, HEX]

def getType(input_text):
    input_text = input_text.lower()
    for item in BASES:
        for opts in item["Input_Options"]:
            if input_text == opts:
                return item
    return None

def main():

    print("Please enter the requirement for conversion, $SOURCE to $DESTINATION")
    in_str = input()
    in_str_list = re.match(r'([0-9A-Za-z]+)\s[tT][oO]\s([0-9A-Za-z]+)', in_str)

    if not (in_str_list):
        print("Illegal Input.")
        return 0

    in_type = getType(in_str_list.group(1))
    dest_type = getType(in_str_list.group(2))

    if (in_type is None) or (dest_type is None):
        print("Illegal Input.")
        return 0

    print("Please enter $INPUT number")
    in_num = re.match(in_type["Code"], input())
    
    if not (in_num):
        print("Illegal Input.")
        return 0
    
    in_number = in_type["To_Dec"](in_num.group(1))
    print("Result is: " + dest_type["Dec_To"](in_number))


main()
