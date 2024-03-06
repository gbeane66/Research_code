# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/research_code.ipynb.

# %% auto 0
__all__ = ['exp_decay', 'foo']

# %% ../nbs/research_code.ipynb 3
import numpy as np

def exp_decay(x:np.ndarray, # Input array that contains the indpendent variable.
    Amplitude: float|int, # Prefactor of the exponential decay.
    tau: float|int, # Decay constant.
    x0: float|int, # Offset for the indpendent variable.
    ) -> np.ndarray: # A new float array containing the exponentially decaying function.

    decayOutput = A * np.exp(-(x-x0)/tau1)
    
    return decayOutput

# %% ../nbs/research_code.ipynb 5
def foo(): pass
