# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:38:35 2018
Functions for Jonathan Garber's Respitch

@author: jgarber
"""

#helpers run this before every tutorial
import itertools
import numpy as np
# import enchant
import pickle
from pathlib import Path
import requests
from io import BytesIO
def get_project_absolute_root_path():
    """Returns project root folder."""
    return Path(__file__).parent.parent
# import word list
with requests.get('https://github.com/sailngarbwm/Jgarber-respitch/blob/main/data/dictionary?raw=true') as file:
    word_lookup = set(pickle.load(BytesIO(file.content)))

import string
alphabet = string.ascii_letters
alphaset = set(alphabet)
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))
#printmd('**bold**')

### Here we make a function that tells us whether or not its an english word

def is_english_word(word):
    if word.lower() in word_lookup:
        print('"'+word + '" is a word')
        return
    else:
        return

def string_combos(string):
    #Function spits out every possible combination of letters ina  string
    num = len(string)
    ans = list()
    for t in range(0,num):
        num2 = num-t
        itr1 = itertools.permutations(string,num2)
        for itr in itr1:
            wrd = ''.join(itr)
            ans.append(wrd)
    return ans

def all_words(letters, alphaset=alphaset, num=9):
    #function takes the first two bits and prints out a list of all the possible combinations
    if type(letters) is list:
        letters = letters[0]
    if type(letters) is not str:
        printmd('<span style="color:red">**Woah there Mates!**, you have input something that is not a string!  \n **A Suggestion:** We should make sure that our input is text ok?</span>')
        return
    if any(char not in alphaset for char in letters) is True:
        printmd('<span style="color:red">**Woah there Mates!**, you have input some funky looking letters!  \n **A Suggestion:**  make sure you do not have any special characters or spaces in your input ok?</span>')
        return
    if len(letters) > num:
        printmd('<span style="color:red">**Woah there Mates!**, That string is a bit long  \n **A Suggestion:**  make sure you only have 9 letters ok?</span>')
        return
    l_comb = string_combos(letters)

    for comb in l_comb:
        is_english_word(comb)
        
def Toaster(X):
    #for toaster demonstration
    printmd('<img src="imbedded_pics\happytoast.jpg" alt="dr_evil" style="width:auto;height:60vh">')

    
    

    
