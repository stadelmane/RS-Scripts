"""Trailblazer Scripts: Various Scripts for the Trailblazer League."""

import MovementController
tries = 0

Scripts = [
    "VarrockAgilityTB"
]

def VarrockAgilityTB() -> None:
    """Run the varrock agility course. Face North, hold up, zoom second dot from right."""
    tries = 0
    movement = MovementController.MovementController()
    screenshots = [
        ('TB-Screenshots\VarrockAgility\StartG.PNG',8),
        ('TB-Screenshots\VarrockAgility\Roof1G.PNG', 8.5),
        ('TB-Screenshots\VarrockAgility\Roof2G.PNG', 8),
        ('TB-Screenshots\VarrockAgility\Roof3G.PNG', 12),
        ('TB-Screenshots\VarrockAgility\Roof4G.PNG', 5),
        ('TB-Screenshots\VarrockAgility\Roof5G.PNG', 8),
        ('TB-Screenshots\VarrockAgility\Roof6G.PNG', 6.5),
        ('TB-Screenshots\VarrockAgility\Roof7G.PNG', 6),
        ('TB-Screenshots\VarrockAgility\Roof8G.PNG', 5),
        ('TB-Screenshots\VarrockAgility\StartingTile.PNG', 4)
    ]
    for i in range(int(input('Please enter how many cycles:'))):
        for j in range(len(screenshots)):
            print(tries)
            movement.moveToCenter(screenshots[j][0], waitTime=screenshots[j][1])
            tries+=1
            
def main():
    """Contains various options to run."""
    choice = input("What Script do you want to run? \n [" + " \n".join(Scripts) + "]")
    if choice == "VarrockAgilityTB":
        VarrockAgilityTB()

if __name__ == '__main__':
    main()