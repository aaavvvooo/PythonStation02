import random

def roll_dices()->list[int]:
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    dices = list([first, second])
    print(f'The sum of your dices is {first} + {second} = {first + second}')
    return dices

def game(sum: int):
    goal = 0
    if 4 <= sum <= 10 and sum != 7:
        goal = sum
        print(f"Your goal is {goal} now!\n")
        dices = roll_dices()
        while dices[0] + dices[1] != goal:
            if dices[0] + dices[1] == 7:
                print("You lost\n")
                return
            dices = roll_dices()
        print("You won\n")
    elif sum == 7 or sum == 11:
        print("You won\n")
    elif sum == 2 or sum == 3 or sum == 12:
        print("You lost\n")

def main():
    dices = roll_dices()
    sum = dices[0] + dices[1]
    game(sum)
        
if __name__ == "__main__":
    main()