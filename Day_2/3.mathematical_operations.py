print(3 + 5)
print(7 - 4)
print(3 * 2)
print(3 ** 2)
print(3 / 2)


print(3 * (3 + 3) / 3 - 3)

# Make BMI Calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

integer_height = float(height)
integer_weight = float(weight)

bmi = integer_weight / (integer_height ** 2)
print(int(bmi))
