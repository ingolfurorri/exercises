import random

class Dice:
    def __init__(self, faces):
        self.face_number = int(faces)
        self.face_up = self.face_number

    def roll(self):
        self.face_up = random.randint(1, self.face_number)

    def __add__(self, dice):
        dice3_faces = self.face_number + dice.face_number
        dice3 = Dice(dice3_faces)
        dice3.face_up = self.face_up + dice.face_up
        return dice3

    def __str__(self):
        return "{}".format(self.face_up)



#Main
def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()

        dice2.roll()

        sum_dice = dice1 + dice2

        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
#seed_number = int(input("Enter a seed: "))
random.seed(11)
run_dice_experiment()