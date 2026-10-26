import random

def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1, dice_2


dice_1, dice_2 = roll_dice()
total = dice_1 + dice_2

print(f"You rolled {dice_1} and a {dice_2}. Total: {total}")

if total in [7, 11]:
    print("You win!")

elif total in [2, 3, 12]:
    print("Casino wins!")

else:
    goal = total
    print(f"Now your goal number is: {goal}!" )

    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        total = dice_1 + dice_2

        print(f"You rolled {dice_1} and a {dice_2}. Total: {total}!")
        if total == goal:
            print("You win!")
            break

        elif total == 7:
            print("You lose!")
