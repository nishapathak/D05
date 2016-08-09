#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
# def even_odd():
#     user_input = "Yes"
#     while user_input == "Yes":
#         try:
#             user_number = int(input("Give me a number: "))
#         except:
#             print("Please enter a number")
#         else:
#             if user_number % 2 == 0:
#                 print("even number")
#             else:
#                 print("odd number") 
  

    # """ Print even or odd:
    #     Takes one integer from user
    #         accepts only non-word numerals
    #         must validate
    #     Determines if even or odd
    #     Prints determination
    #     returns None
    # """
    #pass


# def ten_by_ten():
#     for x in range (1, 11):
#         for y in range (1, 11):
#             print ('{:3}' .format(x*y), end=' ')
#         print()

#     """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
#     pass


def find_average():
    number_list = []
    while True:
        user_number = input("Type number: ")
        if user_number == "done" :
            return sum(number_list)/len(number_list)

#     """ Takes numeric input (non-word numerals) from the user, one number
#     at a time. Once the user types 'done', returns the average.
#     """
#     pass


##############################################################################
def main():
#     """ Calls the following functions:
#         - even_odd()
#         - ten_by_ten()
#     Prints the following function:
#         - find_average()
#     """
#     even_odd()
    # ten_by_ten()
    find_average 

if __name__ == '__main__':
    main()
