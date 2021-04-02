import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

import random
import sys
import random

def shuffle_fn(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

f = open('./anagram/word_list.txt').read().splitlines()
word_pre_scramble = random.choice(f)

word_post_scramble = shuffle_fn(word_pre_scramble)
print(word_pre_scramble)

root = Tk()
root.geometry('800x800')
root.title('anmraga')



e = Entry(root, font=('default', 40))
e.pack()
e.focus_set()


Label(root, text='The scrambled word is: ' + word_post_scramble, font=('default', 40)).pack()

def clear_text():
    global e
    e.delete(0, END)
    e.insert(0, "")

def check():
    global e
    print(e.get())
    if e.get() == word_pre_scramble:
        messagebox.showinfo('Congrats!', 'Hey you won, nice =D')
        sys.exit()
    else:
        messagebox.showinfo('Try again', 'That wasn\'t it, try again')

Button(root, text='Check', command=lambda:[check(), clear_text()], font=('default', 40), bg='white', fg='black').pack()






root.mainloop()
