print("Enter the number of cars")
car_count = int(input())
workload1 = 0
workload2 = 0
workload3 = 0

for car in range(0, car_count):
    print(f"Enter the number of working hours for the car {car + 1}")
    job_hours = int(input())
    if job_hours <= 0:
        print("Error: Invalid job hours")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours #workload = workload3 + job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours

print("The nearest mechanic will be free within {} days"
      .format(int((min(workload1, workload2, workload3) +7) / 8)))

print("All mechanics will be free within {} days"
      .format(int((max(workload1, workload2, workload3) +7) / 8)))

#Task1
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Task2
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a >= b and a >= c:
    print("the largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

print(f"The largest number is: {max(a, b, c)}")

#Task3
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("The sum of numbers from 1 to", n, "is", total)

#Task4
sentence = input("Enter a sentence: ")

count = 0
for char in sentence:
    if char != " ":
        count += 1

print("Number of characters (without spaces):", count)

#Task5
import random
secret = random.randint(1, 10)
guess = None
while guess != secret:
    guess = int(input("Guess the number (1 - 10) "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it!")

#Homework

#1. First - ask about amount of packages

max_items = int(input("Provide the number of items to process"))


#1.5 if max_items <= 0:   wrong

#2. initialize variables
current_package_weight = 0
package_sent = 0
total_weight = 0
unused_capacity_per_package =[]
max_unused_package = None
max_unused_capacity = 0
item_count = 0



#3. if max_items is ok, then start main loop

while item_count < max_items:
    current_weight = int(input("Enter the weight of the item (1 - 10 kg), or 0 to quit"))

    #4. Check if quit the program
    if current_weight == 0:
        print("Terminating the program")
        break

    #5. Main condition
    #if 1 <= current_weight <= 10:


#6. If weight is ok, then start calculating


#7. Print the results