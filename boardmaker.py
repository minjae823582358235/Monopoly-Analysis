#%%
import pandas as pd
import numpy as np
# %%
class Property:
    def __init__(self, 
                 name:str,
                 loc:int, 
                 value:int, 
                 housecost:int, 
                 baserent:int,
                 h1:int,h2:int,h3:int,h4:int,hotel:int,
                 colour:str):
        self.name=name
        self.loc=loc
        self.value=value
        self.housecost=housecost
        self.baserent=baserent
        self.houserent=[h1,h2,h3,h4,hotel]
        self.colour=colour
    def propertyROE(self,housenum:int,colourOwned=False): #Returns the number of hits to break even, adjusts for number of houses and completed set
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
class Utility:
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value
        self.multiplier=[4,10]
    def utilityROE(self,utilityNum:int): #Returns the number of hits to break even, adjusts for the multiplier
        if utilityNum <1 or utilityNum>2:
            raise ValueError('utilitynum should be 1 or 2')
        multiplier=self.multiplier[0]
        if utilityNum ==2:  
            multiplier=self.multiplier[1]
        return self.value/(multiplier*6) #expected return, not probability

class Station:
    def __init__(self,
                 name:str,
                 loc:int,
                 value:int):
        self.name=name
        self.loc=loc
        self.value=value 
        self.rent=[50,100,200]   
    def stationROE(self,stationNum:int): #Returns the number of hits to break even, adjusts for the number of stations
        if stationNum<1 or stationNum>3:
            raise ValueError('stationNum should be 1,2 or 3')
        rent=self.rent[0]
        if stationNum!=1:
            rent=self.rent[stationNum-1]
        return self.value/rent
class Go:
    def __init__(self):
        self.loc=0
        self.value=200
class Jail:
    def __init__(self):
        self.loc=10
class FreeParking:
    def __init__(self):
        self.loc=20
class GoToJail:
    def __init__(self):
        self.loc=30
class Tax:
    def __init__(self,name:str,loc:int,value:int):
        self.name=name
        self.loc=loc
        self.value=value
class CommunityChest:
    def __init__(self,loc:int):
        self.loc=loc
class Chance:
    def __init__(self,loc:int):
        self.loc=loc
def defineLocation(function,type):
    if type not in ['super','income','CC1','CC2','CC3','Chance1','Chance2','Chance3']:
        raise ValueError('type has to be either super or income')
    if not isinstance(function,Tax) and not isinstance(function,CommunityChest) and not isinstance(function,Chance):
        raise ValueError('variable is not the correct class')
    if isinstance(function,Tax):
        if type == 'super':
            function.loc=38
            function.value=100
        if type == 'income':
            function.loc=4
            function.value=200
    if isinstance(function,CommunityChest):
        if type == 'CC1':
            function.loc=2
        if type == 'CC2':
            function.loc=33
        if type == 'CC3':
            function.loc=17
    if isinstance(function,Chance):
        if type == 'Chance1':
            function.loc=7
        if type == 'Chance2':
            function.loc=22
        if type == 'Chance3':
            function.loc=36
# %%
# Create Property objects
#%%
cellsDF=pd.read_excel('Monopoly Datasheet.xlsx')
propertyDF=cellsDF[cellsDF['Type']=='Property']
stationDF=cellsDF[cellsDF['Type']=='Station']
utilityDF=cellsDF[cellsDF['Type']=='Utility']
# propertyDF.head()
# stationDF.head()
utilityDF.head()
properties = [Property(row['Name'], 
                       row['Location'], 
                       row['Property Value'], 
                       row['Cost per House'], 
                       row['Base'], 
                       row['House1'], row['House2'], row['House3'], row['House4'], row['Hotel'], 
                       row['Colour']) for index, row in propertyDF.iterrows()]

# Create Station objects
stations = [Station(row['Name'], row['Location'], row['Property Value']) for index, row in stationDF.iterrows()]

# Create Utility objects
utilities = [Utility(row['Name'], row['Location'], row['Property Value']) for index, row in utilityDF.iterrows()]

chance1=Chance(loc=0)
defineLocation(chance1,'Chance1')
chance2=Chance(loc=0)
defineLocation(chance2,'Chance2')
chance3=Chance(loc=0)
defineLocation(chance3,'Chance3')
cc1=CommunityChest(loc=0)
defineLocation(cc1,'CC1')
cc2=CommunityChest(loc=0)
defineLocation(cc2,'CC2')
cc3=CommunityChest(loc=0)
defineLocation(cc3,'CC3')
superTax=Tax(name='Super Tax',loc=0,value=100)
defineLocation(superTax,'super')
incomeTax=Tax(name='Income Tax',loc=0,value=200)
defineLocation(incomeTax,'income')

go=Go()
go2Jail=GoToJail()
Jail=Jail()
freeParking=FreeParking()
# Sort the list by location
board = properties + stations + utilities +[chance1,chance2,chance3,cc1,cc2,superTax,incomeTax,go,go2Jail,Jail,freeParking]
board = sorted(board, key=lambda x: x.loc)
# for cell in board:
#     print(type(cell), cell.loc)
# print(board)
# %%
