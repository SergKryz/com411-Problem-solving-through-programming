print("What is your name?")
name = input()
print("What is your age?")
age = int(input())
print("What is uor bank balance?")
balance = float(input())

print("Welcome {}. You are said to be  {} years old. Your bank balance is {:.0f}." .format(name, age, balance))