from tkinter import Button
from actions import damageClicked, skillClicked, savingClicked, attackClicked

BTN_PDING = 1

def createSkillButton(button, character, window, display, column, row):
    b = Button(window, text=button.get('buttonLabel'), 
               command=lambda button=button: skillClicked(button, display, character))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)    
    return b

def createDamageButton(button, character, window, display, column, row):
    b = Button(window, text=button.get('buttonLabel'), 
               command=lambda button=button: damageClicked(button, display, character))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)    
    return b

def createSavesButton(button, character, window, display, column, row):
    b = Button(window, text=button.get('buttonLabel'), 
               command=lambda button=button: savingClicked(button, display, character))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)    
    return b

def createAttackButton(button, character, window, display, column, row):
    b = Button(window, text=button.get('buttonLabel'), 
               command=lambda button=button: attackClicked(button, display, character))
    b.grid(column=column, row=row, sticky='nsew', padx=BTN_PDING, pady=BTN_PDING)    
    return b
