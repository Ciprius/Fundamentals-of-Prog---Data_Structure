'''
Created on Dec 17, 2016

@author: Cipri
'''
from Domain1.Repository.Repository import ActivityRepository


class FileActivityRepository(ActivityRepository):
    def __init__(self,filename,pers):
        self._filename=filename
        ActivityRepository.__init__(self)
        self._pers_repo=pers
        self.__loadFromFile_a()
    
    def add_activity(self, arg1, arg2, arg3, arg4, arg5):
        ActivityRepository.add_activity(self, arg1, arg2, arg3, arg4, arg5)
        self.__storeToFile_a()
    
    def remove_activity(self, arg):
        ActivityRepository.remove_activity(self, arg)
        self.__storeToFile_a()
        
    def update_activity(self, arg1, arg2, arg3, arg4, arg5, arg6):
        ActivityRepository.update_activity(self, arg1, arg2, arg3, arg4, arg5, arg6)
        self.__storeToFile_a()
    
    def setup(self, res):
        ActivityRepository.setup(self, res)
        self.__storeToFile_a()
        
    def __loadFromFile_a(self):
        f=open(self._filename,"r")
        lista=f.readline().strip()
        while lista!="":
            acts=lista.split(",")
            per=list(acts[1].split(";"))
            ActivityRepository.add_activity(self, acts[0], per, acts[2], acts[3], acts[4])
            lista=f.readline().strip()
        f.close()
        
    def __storeToFile_a(self):
        f=open(self._filename,"w")
        lista_act=ActivityRepository.get_activity(self)
        for i in lista_act:
            activity=str(i[0])+","+str(i[1][0])
            j=1
            while j!=len(i[1]):
                activity=activity+";"+str(i[1][j])
                j=j+1
            activity=activity+","+str(i[2])+","+str(i[3])+","+str(i[4])+"\n"
            f.write(activity)
        f.close()
            
            
            
            