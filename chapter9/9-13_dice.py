from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

dice = Die()

dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()

dice_10 = Die(10)

dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()
dice_10.roll_die()

dice_20 = Die(20)

dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
dice_20.roll_die()
