# -*- coding: utf-8 -*-

import numpy as np

class GaussianStateRepresentation:
    
    DIM = 0
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, val):
        arr = np.array(val)
        assert arr.shape == (self.DIM,)
        
        self._state = arr
    

    @property
    def cov(self):
        return self._cov
    
    @cov.setter
    def cov(self, arr):
        arr = np.array(arr)
        assert arr.shape == (self.DIM, self.DIM)
        
        diag = np.diag(arr)
        assert all(diag >= 0)
        
        self._cov = arr
    
    
    @property
    def eye(self):
        return np.eye(self.DIM)
        
    
    def __init__(self, *args, **kwargs):
        assert self.DIM > 0
        self._state = np.zeros(self.DIM, dtype=float)
        self._cov = np.zeros((self.DIM, self.DIM), dtype=float)
        
        
        
        
class Cart3StateRepresentation(GaussianStateRepresentation):
    
    DIM = 3
    
    IDX_R = 0
    IDX_AZ = 1
    IDX_EL = 2
    
    @property
    def r(self):
        return self._state[self.IDX_R]
    
    @r.setter
    def r(self, val):
        self._state[self.IDX_R] = val
    
    
    @property
    def az(self):
        return self._state[self.IDX_AZ]
    
    @az.setter
    def az(self, val):
        self._state[self.IDX_AZ] = val
        
    
    @property
    def el(self):
        return self._state[self.IDX_EL]
    
    @el.setter
    def el(self, val):
        self._state[self.IDX_EL] = val
    



#%%


cart_3 = Cart3StateRepresentation()