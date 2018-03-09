'''
Created on Jan 7, 2017

@author: Cipri
'''
from Domain1.Repository.Repository import ActivityRepository
import pickle

class PickleActivityRepository(ActivityRepository):
    def __init__(self,filename,pers):
        self._filename=filename
        ActivityRepository.__init__(self)
        self._pers_repo=pers
        self.__loadFromFile_apickle()
    
    def add_activity(self, arg1, arg2, arg3, arg4, arg5):
        ActivityRepository.add_activity(self, arg1, arg2, arg3, arg4, arg5)
        self.__storeToFile_apickle()
    
    def remove_activity(self, arg):
        ActivityRepository.remove_activity(self, arg)
        self.__storeToFile_apickle()
        
    def update_activity(self, arg1, arg2, arg3, arg4, arg5, arg6):
        ActivityRepository.update_activity(self, arg1, arg2, arg3, arg4, arg5, arg6)
        self.__storeToFile_apickle()
    
    def setup(self, res):
        ActivityRepository.setup(self, res)
        self.__storeToFile_apickle()
        
    def __loadFromFile_apickle(self):
        f=open(self._filename,"rb")
        arg1=pickle.load(f)
        c=0
        print()
        for i in arg1:
            arg=i[1]
            arg1[c][0]=int(i[0])
            arg1[c][1]=[int(x) for x in arg]
            c=c+1
        #for i in arg1:
            #print(i)
        self.setup(arg1)
   
    def __storeToFile_apickle(self):
        f=open(self._filename,"wb")
        arg=self.get_activity()
        pickle.dump(arg,f)
        f.close()