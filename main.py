# GUI imports
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

# Other imports
import random
import sys
import random

# This function shuffles the word
def shuffle_fn(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

# Opens the file with the list of words
f = open('./anagram/word_list.txt').read().splitlines()

# Runs the function with the chosen word as the argument
word_pre_scramble = random.choice(f)
word_post_scramble = shuffle_fn(word_pre_scramble)

# Creating the window
root = Tk()
root.geometry('800x800')
root.title('anmraga')

# Getting the user input
e = Entry(root, font=('default', 40))
e.pack()
e.focus_set()

# This shows the scrambled word
Label(root, text='The scrambled word is: ' + word_post_scramble, font=('default', 40)).pack()

# This function clears the entry box
def clear_text():
    global e
    e.delete(0, END)
    e.insert(0, "")

# This function check to see if the inputted text matches the pre-scrambled word
def check():
    global e
    print(e.get())
    if e.get() == word_pre_scramble:
        messagebox.showinfo('Congrats!', 'Hey you won, nice =D')
        sys.exit()
    else:
        messagebox.showinfo('Try again', 'That wasn\'t it, try again')

# Button runs both functions above
Button(root, text='Check', command=lambda:[check(), clear_text()], font=('default', 40), bg='white', fg='black').pack()

# Runs UI
root.mainloop()
