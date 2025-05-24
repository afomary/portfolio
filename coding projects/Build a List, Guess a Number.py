#PROBLEM ONE

grocery_list = []
while len(grocery_list) < 3:
    item = input("Add an item to the grocery list: ")
    grocery_list.append(item)

print("Your grocery list has 3 items:", grocery_list)

#PROBLEM TWO

print("Guess a Number Game v1")
number = 7
count = 0 

guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    
    if guess < number:
        print("Too low")
        guess = int(input("Please try again:"))
        count += 1
    
    elif guess > number:
        print("Too high")
        guess = int(input("Please try again:"))
        count += 1

print("You guessed it! It was", number, "it took you", count, "tries to get it right!")
    
