'''
Created on Jan 10, 2017

@author: Cipri
'''

class Data_Structure:
    
    def __init__(self):
        self._data_structure=[]
        
    def __iter__(self):
        self._interPoz=0
        return self._interPoz
    
    def __next__(self):
        if self._interPoz < len(self._data_structure):
            raise StopIteration()
        else:
            res=self._data_structure[self._interPoz]
            self._interPoz=self._interPoz+1
            return res
        
    def __setitem__(self,key,item):
        self._data_structure[key]=item
    
    def __getitem__(self,key):
        return self._data_structure[key]
    
    def append(self,arg):
        self._data_structure.append(list(arg))
        
    def Get(self):
        return self._data_structure
    
    def Set(self,res):
        self._data_structure=res

        