
#%%
from boardmaker import board,Property,Station,Utility,Chance,CommunityChest,GoToJail,Go,Jail,FreeParking,Tax
import numpy as np
print(board[30])
# %%
print(type(board[0]))
def diceroll(number:int):
    if number <1 or number>12:
        raise ValueError('number should be between 1 and 12')
    dicerollArr=[1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
    return dicerollArr[number-1]
# %%
class MarkovNode:
    def __init__(self,
                 innerds=None,
                 tag=None,
                 outward=None):
        if isinstance(tag,int):
            self.innerds=innerds
            self.tag=tag
            self.outward=outward
        else:
            raise ValueError('tag should be an integer')
def MonopolyMarkovMatrix(markovNodeArray):
    output=np.zeros(len(markovNodeArray),len(markovNodeArray))
    for i in range(len(markovNodeArray)):
        outwardDict=markovNodeArray[i].outward
        outwardkeys=list(outwardDict.keys())
        outwardkeys.sort()
        insertIndex=np.array(outwardkeys)-np.ones(len(outwardkeys))*outwardkeys[0] #i cooked
        insert=np.zeros(insertIndex[-1]+1) #array that is going to be inserted in output
        for index in insertIndex:
            insert[index]=outwardDict[index+outwardkeys[0]]
        output[i,outwardkeys[0]:outwardkeys[-1]]=insert
    return output
def MonopolyMarkovNodeArray(board):
    monopolyMarkovNodeArray=[]
    for thing in board:
        kwargs={
            'innerds':thing,
            'tag':thing.loc
        }
        if isinstance(thing,GoToJail):
            kwargs['outward']={10:1}
            monopolyMarkovNodeArray.append(MarkovNode(**kwargs))
            continue
        if isinstance(thing,Chance):
            continue
        if isinstance(thing,CommunityChest):
            continue
        kwargdict={}
        