import numpy as np
import matplotlib.pyplot as plt

def roll_dice(num_dice=2, sides=6):
    return np.random.randint(1, sides + 1, size=num_dice)

def batch_rolls(num_dice, sides, num_trials):
    return np.random.randint(1, sides + 1, size=(num_trials, num_dice))

def print_dice_ascii(rolls):
    DICE_ART = {
        1: ("┌─────────┐","│         │","│    ●    │","│         │","└─────────┘"),
        2: ("┌─────────┐","│ ●       │","│         │","│       ● │","└─────────┘"),
        3: ("┌─────────┐","│ ●       │","│    ●    │","│       ● │","└─────────┘"),
        4: ("┌─────────┐","│ ●     ● │","│         │","│ ●     ● │","└─────────┘"),
        5: ("┌─────────┐","│ ●     ● │","│    ●    │","│ ●     ● │","└─────────┘"),
        6: ("┌─────────┐","│ ●     ● │","│ ●     ● │","│ ●     ● │","└─────────┘"),
    }
    lines = [''] * 5
    for roll in rolls:
        art = DICE_ART.get(roll, DICE_ART[1])
        for i, line in enumerate(art):
            lines[i] += line + ' '
    print('\n'.join(lines))

def show_histogram(all_rolls, sides):
    plt.hist(all_rolls.flatten(), bins=range(1, sides + 2), align='left', rwidth=0.8)
    plt.xlabel('Result')
    plt.ylabel('Frequency')
    plt.title('Histogram of Dice Rolls')
    plt.xticks(range(1, sides + 1))
    plt.show()

if __name__ == "__main__":
    sides = int(input("Sides per die: "))
    num_dice = int(input("Number of dice: "))
    num_trials = int(input("Number of trials: "))
    all_rolls = batch_rolls(num_dice, sides, num_trials)
    print(f"\nSample rolls (first trial):")
    print_dice_ascii(all_rolls[0])
    show_histogram(all_rolls, sides)


