
#%%
from boardmaker import board
from collections.abc import Iterable
import numpy as np
print(board[0])
# %%
def diceroll(number:int):
    if number <1 or number>12:
        raise ValueError('number should be between 1 and 12')
    dicerollArr=[1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
    return dicerollArr[number-1]
# %%
class MarkovNode:
    def __init__(self,
                 innerds:Iterable,
                 outward:dict, #has to be in the shape of {tag:probability}
                 tag=None):
        self.innerds=innerds
        self.tag=tag
        self.outward=outward
def MarkovMonopolyMatrix(markovNodeArray):
    output=np.zeros(len(markovNodeArray),len(markovNodeArray))
    counter=0
    for node in markovNodeArray:
        arrowdict=node.outward
        arrowlocsTagDict=arrowdict.keys() 
        inputsdict={}
        for TagDict in arrowlocsTagDict:
            xindex=next(i for i,v in enumerate(markovNodeArray) if v.tag==TagDict)
            inputsdict[xindex]=arrowdict[TagDict]
        maxindex=np.max(inputsdict.keys())
        minindex=np.min(inputsdict.keys())
        inputlist=np.zeros(maxindex-minindex+1)
        for index in inputsdict.keys():
            inputlist[index]=inputsdict[index]
        output[counter][minindex:maxindex+1]=inputlist
        counter+=1
    print(output.shape)

#probabilities to consider:
# chance
# community chest
# go to jail
# while in jail 
# %%
