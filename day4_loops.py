# Day 4 - Python Loops

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# 2. Print even numbers from 1 to 50
for i in range(2, 51, 2):
    print(i)


# 3. Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


# 4. Sum of numbers from 1 to n
num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    total += i

print(f"Sum = {total}")


# 5. Factorial
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial = {factorial}")


# 6. While loop - print 10 to 1
i = 10

while i >= 1:
    print(i)
    i -= 1


# 7. Mini Challenge - Find factors
num = int(input("Enter a number: "))

print("Factors:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
