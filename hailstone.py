"""
File: hailstone.py
Name: 姜譿允
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Find how many steps to make number reach 1
    number: int
    """
    print("This program computes Hailstone sequenced.")

    total = 0
    number = int(input("Enter a number: "))
    while True:

        if number % 2 == 1:
            new_number = int(number * 3 + 1)
            print(str(number) +"is odd, so I make 3n+1:"+str(new_number))
        elif number % 2 == 0:
            new_number = int(number / 2)
            print(str(number) +"is even, so I take half:" +str(new_number))
        if number == 1:
            break
        number = new_number
        total += 1
    print("It take" +str(total) +"steps to reach 1")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
