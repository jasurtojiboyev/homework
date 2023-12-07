import random

number = random.randint(1, 100)
print("Men 1 dan 100 gacha son o'yladim. Topa olasizmi?")
while True:
    guess = int(input("Sizning taxminingiz: "))
    if guess < number:
        print("Xato. Men o'ylagan son bundan katta.")
    elif guess > number:
        print("Xato. Men o'ylagan son bundan kichik.")
    else:
        print(f"Tabriklayman! Men {number} sonini o'ylagan edim.")
        break