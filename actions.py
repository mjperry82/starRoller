from random import randrange

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

def skillClicked(button, display, character):
    diceRoll = rollDice(button.get('dice'))
    mainStat = character.get(button.get('buttonType')).get(button.get('mainStat'))
    statMod = button.get('statMod')
    diceModifier = int(display.get('diceModifier').get())
    #print("diceRoll: {} | mainStat: {} | statMod: {} | diceModifier: {}".format(diceRoll, mainStat, statMod, diceModifier))
    skillResult = diceRoll + mainStat + statMod + diceModifier
    if diceRoll == 20:
        display.get('critDisplay').configure(text='Nat 20')
    elif diceRoll == 1:
        display.get('critDisplay').configure(text='Nat 1')
    else:
        display.get('critDisplay').configure(text='')
    display.get('diceLabel').configure(text=button.get('displayLabel'))
    display.get('diceDisplay').configure(text=skillResult)

def savingClicked(button, display, character):
    diceRoll = rollDice(button.get('dice'))
    mainStat = character.get(button.get('buttonType')).get(button.get('mainStat'))
    statMod = button.get('statMod')
    diceModifier = int(display.get('diceModifier').get())
    #print("diceRoll: {} | mainStat: {} | statMod: {} | diceModifier: {}".format(diceRoll, mainStat, statMod, diceModifier))
    saveResult = diceRoll + mainStat + statMod + diceModifier
    if diceRoll == 20:
        display.get('critDisplay').configure(text='Nat 20')
    elif diceRoll == 1:
        display.get('critDisplay').configure(text='Nat 1')
    else:
        display.get('critDisplay').configure(text='')
    display.get('diceLabel').configure(text=button.get('displayLabel'))
    display.get('diceDisplay').configure(text=saveResult)
    

def attackClicked(button, display, character):
    diceRoll = rollDice(button.get('dice'))
    mainStat = character.get(button.get('buttonType')).get(button.get('mainStat'))
    statMod = button.get('statMod')    
    diceModifier = int(display.get('diceModifier').get())
    #print("diceRoll: {} | mainStat: {} | statMod: {} | diceModifier: {}".format(diceRoll, mainStat, statMod, diceModifier))
    attackResult = diceRoll + mainStat + statMod + diceModifier
    if diceRoll == 20:
        display.get('critDisplay').configure(text='Nat 20')
    elif diceRoll == 1:
        display.get('critDisplay').configure(text='Nat 1')
    else:
        display.get('critDisplay').configure(text='')
    display.get('diceLabel').configure(text=button.get('displayLabel'))
    display.get('diceDisplay').configure(text=attackResult)

def damageClicked(button, display, character):
    display.get('critDisplay').configure(text='')
    diceRoll = rollDice(button.get('dice'))
    statMod = button.get('statMod')
    diceModifier = int(display.get('diceModifier').get())
    damageResult = diceRoll + statMod + diceModifier
    display.get('diceLabel').configure(text=button.get('displayLabel'))
    display.get('diceDisplay').configure(text=damageResult)
