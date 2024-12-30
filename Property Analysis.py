#%%
import pandas as pd
import numpy as np
#%%
cellsDF=pd.read_excel('Monopoly Datasheet.xlsx')
propertyDF=cellsDF[cellsDF['Type']=='Property']
stationDF=cellsDF[cellsDF['Type']=='Station']
utilityDF=cellsDF[cellsDF['Type']=='Utility']
stationDF.head()
# %%
class Property():
    def __init__(self, 
                 name,
                 loc, 
                 value, 
                 housecost, 
                 baserent,
                 h1,
                 h2,
                 h3,
                 h4,
                 hotel,
                 colour):
        self.name=name
        self.loc=loc
        self.value=value
        self.housecost=housecost
        self.baserent=baserent
        self.houserent=[h1,h2,h3,h4,hotel]
        self.colour=colour
    def __str__(self):
        return 'Property:',str(self.name)+',',str(self.colour)
class Utility():
    def __init__(self,
                 name,
                 loc,
                 value):
        self.name=name
        self.loc=loc
        self.value=value
    def __str__(self):
        return  'Utility:',str(self.name)
class Station():
    def __init__(self,
                 name,
                 loc,
                 value):
        self.name=name
        self.loc=loc
        self.value=value
    def __str__(self):
        return  'Station:',str(self.name)