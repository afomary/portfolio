# 5.2 Order a taco 

# SET UP
veggies = ["chili-fried tofu", "spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken"]
toppings = ["radishes", "pickled onion", "cilantro"]

print("Place your taco order:")

# INPUT / PROCESSING
# choose a tortilla

print("Tortilla options: corn  flour")

tortilla = input("Would you like a corn or flour tortilla?")

# vegetarian? / choose a protein or vegetarian protein

vegetarian = input("Are you a vegetarian? ( Y / N ): ")

if vegetarian == "N":
    count = 0
    for i in meats:
        count += 1
        print("Choose", count, "for", i)
        
    '''print("Choose 1 for ground beef")
    print("Choose 2 for pork carnitas")
    print("Choose 3 for spicy chicken")'''

    protein = input("Which protein would you like? ")
    if protein == 1:
        protein = "ground beef"
    elif protein == 2:
        protein = "pork carnitas"
    else:
        protein = "spicy chicken"
else:
    count = 0
    for i in veggies:
        count += 1
        print("Choose", count, "for", i)
        
    '''print("Choose 1 for chili-fried tofu")
    print("Choose 2 for spicy tempeh")
    print("Choose 3 for refried beans")'''
    
    protein = input("Which protein would you like? ")
    if protein == 1:
        protein = "chili-fried tofu"
    elif protein == 2:
        protein = "spicy tempeh"
    else:
        protein = "refried beans"

# choose a topping

print("Now choose a topping:")

count = 0
for i in toppings:
    count += 1
    print("Choose", count, "for", i)
    
'''print("Choose 1 for radishes")
print("Choose 2 for pickled onion")
print("Choose 3 for cilantro")'''

topping = input("Which would you like? ")

if topping == 1:
    topping = "radishes"
elif topping == 2:
    topping = "pickled onion"
else:
    topping = "cilantro"
    
# salsa?

want_salsa = input("Would you like spicy salsa on that? ")

if want_salsa == "Y":
    salsa = "with spicy salsa"
else:
    salsa = "without spicy salsa"

# OUTPUT
# display taco order

print("OK, that's one", protein, "taco on a", tortilla, "tortilla with", salsa, ", and", salsa, "!")

