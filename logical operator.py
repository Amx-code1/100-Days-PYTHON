print("Welcome to rollercoster!")
height = int(input('what is your height in cm ?'))
bill = 0

if height >= 120:
    print("you can ride the rollercoster!")
    age = int(input("what is your age ? "))
    if age < 12:
        bill = 5
        print("please pay $5.")
    elif age <=18:
        bill = 7
        print("please pay $7.")
    elif age >=45 and age <= 55:
        print("you don't have to pay. Everything going to be ok") 
    else:
        bill = 12
        print("please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is {bill }")
else:
    print("sorry you have to grow taller before you can ride")