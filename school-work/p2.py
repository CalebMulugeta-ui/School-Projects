#1. a) Created a list that has the food names, price, quantity
menu = ["Ice Cream", 3.67, 2, "Donuts", 2.50, 6, "Roll", 7.89, 3, "Pizza", 13.45, 5, "Fish and Chips", 15.20, 23, "Poutine", 8.51, 13, "Tacos", 3.00, 19]

#2. a) Use slicing to create 3 seperate lists for food items, prices, and quantities
foodItems = menu[0:19:3]
price = menu[1:20:3]
quantities = menu[2:21:3]

#2. b) Calculate the mean length fo the food items names
length = len(foodItems)
mean = 50/length

#2. c) Create a list of new prices by multiplying the pirce by the quanity
newPrice = []
quan = 0
for p in price:
    newPrice.append(round(p * quantities[quan], 2))
    quan += 1

#2. d) Convert quantites into letters using chr()
quantitiesLetter = []
for q in quantities:
    quantitiesLetter.append(chr(q+64))

#3. Print result for mean length and  summary 
print(f"The mean length of the item names is: {int(mean)}")

print(f"Mean Order Summary: (Food Name: Price, Quantity)") #Print the header for the order summary

#Use for loops to display the results in propering formatting
foodPrint=[] 
overallIndex=0 # Where the index starts
for f in foodItems:
    foodPrint.append(print(f"{foodItems[overallIndex]}: {newPrice[overallIndex]}, {quantitiesLetter[overallIndex]}"))
    overallIndex += 1 #Increases the index by 1 each loop
    

