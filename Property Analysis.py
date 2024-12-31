#%%
import pandas as pd
import numpy as np
#%%
cellsDF=pd.read_excel('Monopoly Datasheet.xlsx')
propertyDF=cellsDF[cellsDF['Type']=='Property']
stationDF=cellsDF[cellsDF['Type']=='Station']
utilityDF=cellsDF[cellsDF['Type']=='Utility']
# propertyDF.head()
# stationDF.head()
utilityDF.head()
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
    def propertyROE(self,housenum:int,colourOwned=False):
        if housenum < 0 or housenum > 5:
            raise ValueError('Housenum should be between 0 and 6 excl')
        if housenum == 0:
            if colourOwned==True:
                return self.value/(self.baserent*2)
            else:
                return self.value/(self.baserent)
        else:
            upfront=self.housecost*housenum+self.value
            return upfront/self.houserent[housenum-1]
class Utility():
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value
        self.multiplier=[4,10]
    def utilityROE(self,utilityNum:int):
        if utilityNum <1 or utilityNum>2:
            raise ValueError('utilitynum should be 1 or 2')
        multiplier=self.multiplier[0]
        if utilityNum ==2:  
            multiplier=self.multiplier[1]
        return self.value/(multiplier*6) #expected return, not probability

class Station():
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value 
        self.rent=[50,100,200]   
    def stationROE(self,stationNum:int):
        if stationNum<1 or stationNum>3:
            raise ValueError('stationNum should be 1,2 or 3')
        rent=self.rent[0]
        if stationNum!=1:
            rent=self.rent[stationNum-1]
        return self.value/rent
# %%
