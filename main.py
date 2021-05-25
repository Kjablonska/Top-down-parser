from input_handler import input_handler
from parser import parser

def main():
    CFG, input_string = input_handler()
    parser(CFG, input_string)


main()