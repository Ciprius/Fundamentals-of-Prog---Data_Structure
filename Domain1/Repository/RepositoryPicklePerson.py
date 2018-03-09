'''
Created on Jan 7, 2017

@author: Cipri
'''
from Domain1.Repository.Repository import PersonRepository
import pickle

class PicklePersonRepository(PersonRepository):
    def __init__(self,filename):
        self._filename=filename
        PersonRepository.__init__(self)
        self.__loadFromFile_pickle()
        
    def add_person(self, arg1, arg2, arg3, arg4):
        PersonRepository.add_person(self, arg1, arg2, arg3, arg4)
        self.__storeToFile_pickle()

    def remove_name(self, arg1):
        PersonRepository.remove_name(self, arg1)
        self.__storeToFile_pickle()

    def remove_person(self, arg1):
        PersonRepository.remove_person(self, arg1)
        self.__storeToFile_pickle()

    def update_person(self, arg1, arg2, arg3, arg4, arg5):
        PersonRepository.update_person(self, arg1, arg2, arg3, arg4, arg5)
        self.__storeToFile_pickle()
 
    def Setup(self, res):
        PersonRepository.Setup(self, res)
        self.__storeToFile_pickle()
        
    def __loadFromFile_pickle(self):
        f=open(self._filename,"rb")
        arg=pickle.load(f)
        c=0
        for i in arg:
            arg[c][0]=int(i[0])
            c=c+1
            #print(i)
        self.Setup(arg)
        '''
        c=0
        for i in self.__data_person:
            self.__data_person[c][0]=int(i[0])
            c=c+1
            print(i)
        '''
        
    def __storeToFile_pickle(self):
        f=open(self._filename,"wb")
        arg=self.get_person()
        '''
        print("i")
        for i in arg:
            print(i)
            '''
        pickle.dump(arg,f)
        f.close()
        
        
        
        