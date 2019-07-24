#!/usr/bin/python3

from tkinter import Tk, Label, Button, Spinbox, IntVar
from random import randrange
from json import loads

#load charachter properties from json file and decode them to char
with open('starRoller.json', 'r') as f:
    char_json = f.read()

char = loads(char_json)

skills = char.get('skills')
abilities = char.get('abilities')
damage = char.get('damage')
saves = char.get('saves')

BTN_PDING=1

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

# create base tkinter window
window = Tk()
window.title("starRoller")

# create label to indicate what dice roll is being displayed
diceLabel = Label(window, text='', font=('Arial', 20), padx=5)
diceLabel.grid(column=0, row=0, columnspan=3)

# create label to display the rolled dice
diceDisplay = Label(window, text="00", font=("Arial Bold", 50), padx=75)
diceDisplay.grid(column=0, row=1, columnspan=3)

critDisplay = Label(window, text='', font=("Arial Bold", 10), fg='red', padx=1, pady=1)
critDisplay.grid(column=1, row=2)

var = IntVar()
var.set(0)
diceModifier = Spinbox(window, from_=-10, to_=10, width=3, textvariable=var)
diceModifier.grid(column=2, row=2, padx=1, pady=1)

### SKILLS buttons and function to roll skill checks

#define skills action
def skillRoller(skill):
    diceRoll = randrange(1, 21)
    skillResult = diceRoll + skills.get(skill) + int(diceModifier.get())
    if diceRoll == 20:
        critDisplay.configure(text='Nat 20')
    elif diceRoll == 1:
        critDisplay.configure(text='Nat 1')
    else:
        critDisplay.configure(text='')
    diceLabel.configure(text=skill.capitalize())
    diceDisplay.configure(text=skillResult)

# create skill buttons from skill list in json file
skillButtons = []
rowCount = 3
for skill in skills:
    if rowCount < 13:
        column = 0
        row = rowCount
    else:
        column = 1
        row = rowCount - 10
    rowCount += 1
    b = Button(window, text='Roll {}'.format(skill.capitalize()), 
               command=lambda skill=skill: skillRoller(skill))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)
    skillButtons.append(b)

### Attack Buttons

def rollTAStealthClicked():
    diceRoll = rollDice({'d20': 1})
    taStealthRoll = diceRoll + skills.get('stealth') + 4 + int(diceModifier.get())
    if diceRoll == 20:
        critDisplay.configure(text='Nat 20')
    elif diceRoll == 1:
        critDisplay.configure(text='Nat 1')
    else:
        critDisplay.configure(text='')
    diceLabel.configure(text='Trick Attack Stealth Roll')
    diceDisplay.configure(text=taStealthRoll)

taStealthButton = Button(window, text="Trick Attack Stealth", command=rollTAStealthClicked)
taStealthButton.grid(column=2, row=3, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)

def rollAttackClicked():
    diceRoll = randrange(1, 21)
    attackRoll = diceRoll + char.get('attack bonus') + int(diceModifier.get())
    if diceRoll == 20:
        critDisplay.configure(text='Nat 20')
    elif diceRoll == 1:
        critDisplay.configure(text='Nat 1')
    else:
        critDisplay.configure(text='')
    diceLabel.configure(text='Attack Roll')
    diceDisplay.configure(text=attackRoll)

attackButton = Button(window, text="Attack Roll", command=rollAttackClicked)
attackButton.grid(column=2, row=4, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)

# Damage Calculator Buttons
def damageClicked(damageType):
    damageRoll = rollDice(damage.get(damageType)) + int(diceModifier.get())
    diceLabel.configure(text='{}'.format(damageType.capitalize()))
    diceDisplay.configure(text=damageRoll)

rowCount = 5
damageButtons = []
for dType in damage:
    column = 2
    row = rowCount
    rowCount += 1
    b = Button(window, text='{}'.format(dType.capitalize()), 
               command=lambda dType=dType: damageClicked(dType))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)
    damageButtons.append(b)

# Saving Rolls
def savingClicked(save):
    diceRoll = randrange(1, 21)
    saveResult = diceRoll + saves.get(save) + int(diceModifier.get())
    if diceRoll == 20:
        critDisplay.configure(text='Nat 20')
    elif diceRoll == 1:
        critDisplay.configure(text='Nat 1')
    else:
        critDisplay.configure(text='')
    diceLabel.configure(text='{} Save'.format(save.capitalize()))
    diceDisplay.configure(text=saveResult)

savingButtons = []
for save in saves:
    column = 2
    row = rowCount
    rowCount +=1
    b = Button(window, text='{} Save'.format(save.capitalize()), 
               command=lambda save=save: savingClicked(save))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)
    savingButtons.append(b)

window.mainloop()
