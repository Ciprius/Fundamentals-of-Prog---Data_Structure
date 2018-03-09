'''
Created on Dec 15, 2016

@author: Cipri
'''
from Domain1.Repository.Repository import PersonRepository
import pickle

class FilePersonRepository(PersonRepository):
    def __init__(self,filename):
        self._filename=filename
        PersonRepository.__init__(self)
        self.__loadFromFile_p()
        
    def add_person(self, arg1, arg2, arg3, arg4):
        PersonRepository.add_person(self, arg1, arg2, arg3, arg4)
        self.__storeToFile_p()

    def remove_name(self, arg1):
        PersonRepository.remove_name(self, arg1)
        self.__storeToFile_p()

    def remove_person(self, arg1):
        PersonRepository.remove_person(self, arg1)
        self.__storeToFile_p()

    def update_person(self, arg1, arg2, arg3, arg4, arg5):
        PersonRepository.update_person(self, arg1, arg2, arg3, arg4, arg5)
        self.__storeToFile_p()
 
    def Setup(self, res):
        PersonRepository.Setup(self, res)
        self.__storeToFile_p()
       
    def __loadFromFile_p(self):
        f= open(self._filename,"r")
        #g=open("D:\Faculta\python projects\lab5-7\init_person_pi.pickle","wb")
        #res=[]
        person=f.readline().strip()
        while person!="":
            pers=person.split(",")
            #res.append(list(pers))
            PersonRepository.add_person(self, pers[0],pers[1],pers[2],pers[3])
            person=f.readline().strip()
        #pickle.dump(res,g)
        #g.close()
        f.close()    
     
    def __storeToFile_p(self):
        f=open(self._filename,"w")
        lista= PersonRepository.get_person(self)
        for i in lista:
            person=str(i[0])+","+str(i[1])+"," +str(i[2])+","+str(i[3])
            person=person +"\n"
            f.write(person)
            
        f.close()
       
    
