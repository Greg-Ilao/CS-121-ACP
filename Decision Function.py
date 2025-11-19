# 1.if
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")

# 2. if-else
num = int(input("\nEnter another number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 3. if-elif-else
age = int(input("\nEnter your age: "))
if age < 18:
    print("You are a minor")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

# 4. Nested if
x = int(input("\nEnter a number to check for sign and parity: "))
if x != 0:
    if x > 0:
        print("Positive", end=" ")
    else:
        print("Negative", end=" ")
    
    if x % 2 == 0:
        print("even number")
    else:
        print("odd number")
else:
    print("The number is zero")
