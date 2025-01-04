
#%%
from boardmaker import board
import numpy as np
print(board[0])
# %%
print(type(board[0]))
# %%
class MarkovNode:
    def __init__(self,
                 innerds=None,
                 tag=None,
                 outward=None):
        self.innerds=innerds
        self.tag=tag
        self.outward=outward
    def MarkovMatrix(markovNodeArray):
        output=np.zeros(len(markovNodeArray),len(markovNodeArray))
        