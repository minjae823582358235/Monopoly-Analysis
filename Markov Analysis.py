
#%%
from boardmaker import board
from collections.abc import Iterable
import numpy as np
print(board[0])
# %%
def diceroll(number:int):
    if number <2 or number>12:
        raise ValueError('number should be between 2 and 12')
    dicerollArr=[1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
    return dicerollArr[number-2]
# %%
class MarkovNode:
    def __init__(self,
                 innerds:Iterable,
                 outward:dict, #has to be in the shape of {tag:probability}
                 tag=None):
        self.innerds=innerds
        self.tag=tag
        self.outward=outward
def MarkovMonopolyMatrix(markovNodeArray): #assuming markovnode array is sorted with ascending location
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
    print('matrix created')
    return output
def MarkovMatrixSolve(InitialState,Matrix):
    if len(InitialState)!=len(Matrix):
        raise ValueError('Initial state and matrix should have the same length')
    if not np.allclose(np.sum(Matrix,axis=1),np.ones(len(Matrix))):
        raise ValueError('Matrix should be a stochastic matrix')
    output=InitialState
    for i in range(100):
        output=np.dot(output,Matrix)
    return output

def Board2MarkovArray(boardArray):
    output=[]
    for thing in boardArray:
        probabilitydict={}
        if thing.__class__.__name__=='Property' or thing.__class__.__name__=='Utility' or thing.__class__.__name__=='Station' or thing.__class__.__name__=='JailVisitng' or thing.__class__.__name__=='FreeParking' or thing.__class__.__name__=='Tax' or thing.__class__.__name__=='Go':
            for move in range(2,13):
                if move+thing.loc>40:
                    probabilitydict[move+thing.loc-40]=diceroll(move)
                if move+thing.loc==30:
                    probabilitydict[10.5]=diceroll(move)
                else:
                    probabilitydict[move+thing.loc]=diceroll(move)
            output.append(MarkovNode(innerds=thing,outward=probabilitydict,tag=thing.loc))
        elif thing.__class__.__name__=='Chance': 
            probabilitydict[0]=1/16
            probabilitydict[11]=1/16
            #need to add advance to nearest utility
            #need to add advance to nearest station
            #go back 3 spaces
            #kings cross station
        elif thing.__class__.__name__=='CommunityChest':
            probabilitydict[0]=1/16
            probabilitydict[10.5]=1/16
            probabilitydict[thing.loc]=14/16
        elif thing.__class__.__name__=='GoToJail':
            probabilitydict[10.5]=1
        elif thing.__class__.__name__=='InJail':
            doubleP=diceroll(2)
            doubleArr=[2,4,6,8,10,12]
            for move in doubleArr:
                probabilitydict[move+10]=doubleP
            probabilitydict[10.5]=1-doubleP*len(doubleArr)
        else:
            raise ValueError('Class not recognized')
#probabilities to consider:
# chance
# community chest
# go to jail
# while in jail 
# %%
