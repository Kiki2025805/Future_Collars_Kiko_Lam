# Personalized Birthday Card Program

#Ask user for details
recipient_name = input("Please provide the recipient's name: ")
birth_year = int(input("Please peovide the year of birth: "))
personal_message = input("Write a short birthday message: ")
sender_name = input("Please provider the sender's name: " )


#Caculate age based on current year
current_year=2024
age = current_year - birth_year

#Display formatted birthday card
print("========================================")
print(f"{recipient_name}, let's celebrate your {age} years of awesome!")
print(f"wishing you a day filled with joy and laughter as your turn {age}!")
print()
print(personal_message)
print()
print("With love and best wishes, ")
print(sender_name)
print("=======================================")

