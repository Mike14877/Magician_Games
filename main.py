# Magician_Game
import random
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter
r an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


# def back():
#     answer = input("Do you wanna continue ? 'Yes' Or 'No' : ")
#     get_answer = answer.lower()
#     if get_answer == "yes" or get_answer == "y":
#         return magician_number()
#     else:
#         back_to_compare = input("Enter 'PLAY' to return the function ")
#         if back_to_compare == "PLAY":
#             return magician_number()
#         else:
#             return back()
#     # print((get_answer))


random_number = random.randint(1, 100)
# print(random_number)


def magician_number():
    keep_going = True
    while keep_going:
        guess_number = int(input(" Guess a number (1 to 100) : "))
        if guess_number != random_number:
            print("Ha ha! You're  stuck in my loop!")
        else:
            print("Well done, muggle! You are free now.")
            keep_going = False

magician_number()