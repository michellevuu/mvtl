#introduce travel agent to user
print("Hello, I am your online travel bot.")
print("I will ask you some questions, and provide you with ...")

#identify values
vienna_flight = 997.93
vienna_hotel = 143.84

bali_flight = 849.93
bali_hotel = 235.35

#ask for names
name = input("\nWhat is your name? --> ")

#ask for age
age = int(input("\nHello " + name.capitalize() + ", what is your age? --> "))

#create senior discount based on age
senior_age = 64
senior_discount = 0
if (age > senior_age):
  senior_discount = age - senior_age
  print("You qualify for the senior discount of " + str(senior_discount) + "%!")

 # ask how many nights stayed
nights_stayed = input("\nFor how many nights would you like to stay? --> ")

#ask for culture and classical music 
print("\nDo you like culture and classical music?")
like_music = input("Please answer y/n. --> ").lower()

#ask if they like beaches and surfing
print("\nDo you like beaches and surfing")
like_beach = input("Please answer y/n. --> ").lower()

#create if, elif, and else based on answers to questions
if (like_music == "y" and like_beach == "n"):
  print("\nHow about a trip to Vienna?")
  print("Flight:", str(vienna_flight) + "$")
  print("Hotel:", str(vienna_hotel) + "$/night")
  print("Discount:", str(senior_discount) + "%")

  total_price = ( (vienna_flight + (vienna_hotel * int(nights_stayed))) * (100 - senior_discount) / 100 )

  print("Total for", str(nights_stayed), "nights (discount included):", str(total_price) + "$")
  
  elif (like_music == "n" and like_beach == "y"):
  print("\nHow about a trip to Bali?")

elif (like_music == "y" and like_beach == "y"):
  print("the more expensive trip")

else:
  print("\nI am sorry , we don’ t have any trips to offer at this point.")
