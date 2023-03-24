"""
This program is written to convert text to whitespace esolang syntax

author -> anshulbadhani

https://github.com/anshulbadhani/Whitespace-syntax-writer
"""
# Imports 
import time
import pyautogui as pg

# Functions
def debug(message: str | int) -> str | int:
    """
    Only for showing which print statement
    if for debugging :)
    """
    print(message)

toBinary = lambda a : str(bin(ord(a))) # 'string' datatype to BINARY

# Main program starts here
# Taking input

sentence = input("""Enter the sentence : """)
charLis = [i for i in sentence]
# debug(toBinary(sentence))

# Warning Message
print("""ONLY 5 SECONDS LEFT AFTER 5 SECONDS PYTHON WILL START TYPING...
SWITCH TO TEXT AREA WHERE YOU HAVE TO TYPE THE MESSAGE...""")
time.sleep(5) # The program will wait for 5 seconds


# Syntax writing of whitespace and logic in python
pg.typewrite("<")
for chars in charLis:
    binCode = toBinary(chars)
    debug(binCode)
    bit = [bits for bits in binCode]
    # debug(bit)

    # printing value of each byte (for whitespaces)
    pg.typewrite("  ") # Pushing value into stack via stack manupulation
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

pg.typewrite("\n\n\n") # Marks the end of the program (Whitespace formatting convention)
pg.typewrite(">") # To make the invisible code visible

# ----- END ----- #
