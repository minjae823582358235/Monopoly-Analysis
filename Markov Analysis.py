
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
        self.innerds=innerds
        self.tag=tag
        self.outward=outward
def MarkovMonopolyMatrix(markovNodeArray):
    output=np.zeros(len(markovNodeArray),len(markovNodeArray))
    for i in range(len(markovNodeArray)):
        if isinstance(markovNodeArray[i].innerds,GoToJail):
            continue
        if isinstance(markovNodeArray[i].innerds,Chance):
            continue
        if isinstance(markovNodeArray[i].innerds,CommunityChest):
            continue
        