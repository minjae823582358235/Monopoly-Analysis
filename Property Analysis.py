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
                 name:str,
                 loc:int, 
                 value:int, 
                 housecost:int, 
                 baserent:int,
                 h1:int,
                 h2:int,
                 h3:int,
                 h4:int,
                 hotel:int,
                 colour:str):
        self.name=name
        self.loc=loc
        self.value=value
        self.housecost=housecost
        self.baserent=baserent
        self.houserent=[h1,h2,h3,h4,hotel]
        self.colour=colour
        self.mortgageValue=value*0.5
        self.mortgageRepay=self.mortgageValue*1.1
    def __str__(self):
        return 'Property:',str(self.name)+',',str(self.colour)
class Utility():
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value
        self.mortgageValue=value*0.5
        self.mortgageRepay=self.mortgageValue*1.1
    def __str__(self):
        return  'Utility:',str(self.name)
class Station():
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value
        self.mortgageValue=value*0.5
        self.mortgageRepay=self.mortgageValue*1.1
    def __str__(self):
        return  'Station:',str(self.name)
    
# %%
