# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:45:16 2022

@author: shn99
"""

from tkinter import*
root=Tk()
root.title("Dictionary")
root.geometry("500x500")

dictionary = ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]



random_no=random.randint(0,7)

dictionary["color"][random_no]

root.mainloop()