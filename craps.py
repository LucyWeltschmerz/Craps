import random


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def game_of_cramps():
    dice_a, dice_b = roll_dice()
    sum_of_ab = dice_a + dice_b
    print(f'The sum of dice is {dice_a} + {dice_b} = {sum_of_ab}')

    if sum_of_ab in (7, 11):
        print('You won')
    elif sum_of_ab in (2, 3, 12):
        print('Cramps, You Lost!')
    else:
        goal_number = sum_of_ab
        print(f'Your goal number is {goal_number} ')
        while True: 
            dice_a, dice_b = roll_dice()
            new_sum = dice_a + dice_b
            print(f'The sum of rolled dice is {dice_a} + {dice_b} = {new_sum}')
            if new_sum == goal_number:
                print('You won')
                break
            elif new_sum == 7:
                print('You rolled a 7 You Lost!')
                break


if __name__ == '__main__':

    game_of_cramps()
