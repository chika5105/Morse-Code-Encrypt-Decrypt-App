#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:17:22 2020

@author: jinanwachikafavour
"""
#pip install pillow
import PIL.ImageTk, PIL.Image
# import tkinter module 
from tkinter import *
#from IPython.display import Image

# import other necessery modules 
import random 
import time 
import datetime 

# creating root object 
root = Tk() 
# defining size of window 
root.geometry("1200x6000") 

class Window(Frame): 
    """Class object to wrap the image to use as a tkinter object"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = PIL.Image.open("logo.png")
        render = PIL.ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
app = Window(root)
# setting up the title of window 
root.title("Message Encryption and Decryption With Morse Code") 

Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700, 
							relief = SUNKEN) 
f1.pack(side = LEFT) 

# ============================================== 
#				 TIME 
# ============================================== 
localtime = time.asctime(time.localtime(time.time())) 

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
		text = "Chika's Secret Messaging App \n with Morse Code ", 
					fg = "Black", bd = 10, anchor='w') 
					
lblInfo.grid(row = 0, column = 0) 

lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
			text = localtime, fg = "red2", 
						bd = 10, anchor = 'w') 
						
lblInfo.grid(row = 1, column = 0) 

rand = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 

# exit function 
def qExit(): 
	root.destroy() 

# Function to reset the window 
def Reset(): 
	rand.set("") 
	Msg.set("") 
	key.set("") 
	mode.set("") 
	Result.set("") 


# reference 
lblReference = Label(f1, font = ('arial', 16, 'bold'), 
				text = "Name:", bd = 16, anchor = "w") 
				
lblReference.grid(row = 0, column = 0) 

txtReference = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = rand, bd = 1, insertwidth = 4, 
						bg = "deep sky blue", justify = 'right') 
						
txtReference.grid(row = 0, column = 1) 

# labels 
lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
		text = "MESSAGE", bd = 1, anchor = "w") 
		
lblMsg.grid(row = 1, column = 0) 

txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = Msg, bd = 1, insertwidth = 4, 
				bg = "deep sky blue", justify = 'right') 
				
txtMsg.grid(row = 1, column = 1) 


lblmode = Label(f1, font = ('arial', 16, 'bold'), 
		text = "MODE(e for encrypt, d for decrypt)", 
								bd = 1, anchor = "w") 
								
lblmode.grid(row = 2, column = 0) 

txtmode = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = mode, bd = 1, insertwidth = 4, 
				bg = "deep sky blue", justify = 'right') 
					
txtmode.grid(row = 2, column = 1) 

lblService = Label(f1, font = ('arial', 16, 'bold'), 
			text = "The Result-", bd = 1, anchor = "w") 
			
lblService.grid(row = 2, column = 2) 

txtService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Result, bd = 1, insertwidth = 4, 
					bg = "salmon", justify = 'right') 
						
txtService.grid(row = 2, column = 3) 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
    cipher = '' 
    message = message.upper()
    for letter in message:
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher 
  
# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
  
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher 


def Ref(): 
	print("Message= ", (Msg.get())) 

	clear = Msg.get() 
	m = mode.get() 

	if (m == 'e'): 
		Result.set(encrypt(clear)) 
	else: 
		Result.set(decrypt(clear)) 

# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('arial', 16, 'bold'), width = 10, 
					text = "Show Message", bg = "powder blue", 
						command = Ref).grid(row = 7, column = 1) 

# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Reset", bg = "green", 
				command = Reset).grid(row = 7, column = 2) 

# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Exit", bg = "red", 
				command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root.mainloop() 

