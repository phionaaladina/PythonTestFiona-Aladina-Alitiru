# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.








# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

def odd_numbers():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

odd_numbers()

