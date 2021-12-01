#To check the type of data

print(type(22))
print(str(22) + " number")

# F string
score = 1
height = 1.8
is_winning = True

print(f"your score is {score}, and height is {height}, the fact you are winning is {is_winning}")

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
print(first_number + second_number)



