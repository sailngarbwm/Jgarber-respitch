
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
