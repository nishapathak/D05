#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports


# Body
def more_than_20():
    with open("words.txt") as fin:
        for word in fin.readlines():
            if len(word.strip()) > 20:
                print(word.strip())


##############################################################################
def main():
    more_than_20()

if __name__ == '__main__':
    main()
