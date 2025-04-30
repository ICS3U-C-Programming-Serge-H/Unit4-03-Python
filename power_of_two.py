#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 28, 2025
# This program will ask the user for a whole number and then
# A for loop to calculate the square of every number leading up to user_num


def main():

    while True:
        try:
            user_input = int(input("Enter a whole number: "))
            if user_input > 0:
                break
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\nPowers of two from 0 to {user_input}:")
    counter = 0
    for counter in range(user_input + 1):
        power = 2**counter
        print(f"2^{counter} = {power}")


if __name__ == "__main__":
    main()
