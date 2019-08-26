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

# import word list
with open('dictionary','rb') as file:
    word_lookup = set(pickle.load(file))

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

    
    
'''
This next portion will spit out the interactive drug use plots
'''

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



drug_use = pd.read_csv('https://raw.githubusercontent.com/resbaz/data/master/drug-use-by-age/drug-use-by-age.csv')

for column in list(drug_use.columns)[2:]:
    drug_use[column] = pd.to_numeric(drug_use[column],errors = 'coerce')

an_epic_party = ['alcohol',
                 'marijuana',
                 'cocaine',
                 'crack',
                 'heroin',
                 'hallucinogen',
                 'inhalant',
                 'pain-releiver',
                 'oxycontin',
                 'tranquilizer',
                 'stimulant',
                 'meth',
                 'sedative']

def load_drug_data():
    return drug_use, an_epic_party

def drug_plot(drug = 'alcohol', drug_use = drug_use):
    '''
    Plotting function to plot the frequency and use of one
    '''
    du = drug+'-use' # just creating the column names from the drug input
    df = drug+'-frequency'
    ax = drug_use.plot(kind = 'bar',x = 'age',y = [du,df],
              secondary_y= [df], figsize = (12,8))
    # Note these are movign the legends off the chart
    ax.legend(loc = (1.1,0.9))
    ax.right_ax.legend(loc=(1.1,0.8))
    ax.set_ylabel(du.replace('-',' ')+' metric')
    ax.right_ax.set_ylabel(df.replace('-',' ')+' metric')
    #plt.show()
    
def interact_drug_data():
    from ipywidgets import interact, fixed
    # all we need to do is specify here what function we are interacting with
    interact(drug_plot, drug = an_epic_party, drug_use = fixed(drug_use))
    