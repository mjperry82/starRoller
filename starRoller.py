#!/usr/bin/python3

from tkinter import Tk, Label, Button, Spinbox, IntVar
from random import randrange
from json import loads
from buttons import createSkillButton, createDamageButton, createSavesButton, createAttackButton
from pathlib import Path

BTN_PDING=1

def loadCharacter():
    dir = Path(__file__).parent.absolute()
    file = dir / 'starRoller.json'
    with open(file, 'r') as f:
        char_json = f.read()
        
    return loads(char_json)

def rollDice(diceToRoll):
    ## Takes a tuple with dice to roll formated {'d4': #, 'd6': #, 'd8': #, 'fixed': #}
    ## Returns the total of rolled dice
    diceTotal = 0
    for dice in diceToRoll:
        if dice == 'fixed':
            diceTotal += diceToRoll.get(dice)
        else:
            count = 0
            while count < diceToRoll.get(dice):
                diceTotal += randrange(1, int(dice[1:])+1)
                count += 1 
    return diceTotal

def createDisplay(window):
    display = {}
    # create label to indicate what dice roll is being displayed
    diceLabel = Label(window, text='', font=('Arial', 20), padx=5)
    diceLabel.grid(column=0, row=0, columnspan=3)
    display.update({"diceLabel": diceLabel})

    # create label to display the rolled dice
    diceDisplay = Label(window, text="00", font=("Arial Bold", 50), padx=75)
    diceDisplay.grid(column=0, row=1, columnspan=3)
    display.update({"diceDisplay": diceDisplay})

    critDisplay = Label(window, text='', font=("Arial Bold", 10), fg='red', padx=1, pady=1)
    critDisplay.grid(column=1, row=2)
    display.update({"critDisplay": critDisplay})

    diceModLabel = Label(window, text="Dice Modifier:", font=("Arial", 10))
    diceModLabel.grid(column=2, row=2, sticky='w', padx=1, pady=1)
    display.update({"diceModLabel": diceModLabel})
    
    modDefault = IntVar()
    modDefault.set(0)
    diceModifier = Spinbox(window, from_=-10, to_=10, width=5, textvariable=modDefault)
    diceModifier.grid(column=2, row=2, sticky='e', padx=1, pady=1)
    display.update({"diceModifier": diceModifier})
    
    return display

def main():
    character = loadCharacter()
    # create base tkinter window
    window = Tk()
    if character.get('name') != None:
        window.title("starRoller - {}".format(character.get('name')))
    else:
        window.title("starRoller")
    
    display = createDisplay(window)
    
    column = 0
    row = 4
    buttons = []
    for buttonName in character.get('buttons'):
        button = character.get('buttons').get(buttonName)
        if button.get('buttonType') == 'skills':
            buttons.append(createSkillButton(button, character, window, display, column, row))
        elif button.get('buttonType') == 'damage':
            buttons.append(createDamageButton(button, character, window, display, column, row))
        elif button.get('buttonType') == 'saves':
            buttons.append(createSavesButton(button, character, window, display, column, row))
        elif button.get('buttonType') == 'attack bonus':
            buttons.append(createAttackButton(button, character, window, display, column, row))
        else:
            pass
        row += 1
        if row == 14:
            row = row - 10
            column += 1
    
    window.mainloop()



if __name__ == '__main__':
    main()




