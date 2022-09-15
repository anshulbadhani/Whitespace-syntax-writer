"""
This program is written to convert text to whitespace esolang syntax

author -> anshulbadhani

https://github.com/anshulbadhani/Whitespace-syntax-writer
"""

import time
import pyautogui as pg


# def toBinary(char: str)-> str: # ASCII to BINARY
#     asciiCode = ord(char)
#     binary = bin(asciiCode)

#     n = binary[2::]
#     # x = [i for i in n]

#     return n

def debug(message: str | int) -> str | int:
    """
    Only for showing which print statement
    if for debugging :)
    """
    print(message)

toBinary = lambda a : str(bin(ord(a))) # 'string' datatype to BINARY


sentence = input("Enter the sentence : ")
charLis = [i for i in sentence]
# debug(toBinary(sentence))


print("ONLY 5 SECONDS LEFT AFTER 5 SECONDS PYTHON WILL START TYPING...")
time.sleep(5) # The program will wait for 5 seconds


# Syntax writing of whitespace and logic in python
pg.typewrite("<")
for chars in charLis:
    binCode = toBinary(chars)
    debug(binCode)
    bit = [bits for bits in binCode]
    # debug(bit)


    # printing value of each byte (for whitespaces)
    pg.typewrite("  ") # stack manupulation by pushing value in stack
    for j in bit:
        match j:
            case "0":
                print("SPACE")
                pg.typewrite(" ") # Binary Value -> 0
            case "1":
                print("TAB")
                pg.typewrite("\t") # Binary Value -> 1
    pg.typewrite("\n")
    pg.typewrite("\t\n  .")

pg.typewrite("\n\n\n")
pg.typewrite(">")