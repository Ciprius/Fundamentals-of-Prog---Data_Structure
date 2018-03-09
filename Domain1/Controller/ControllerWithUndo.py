'''
Created on Dec 12, 2016

@author: Cipri
'''
from Domain1.Controller.Controller import PersonController,ActivityController
from Domain1.Controller.undoController1 import FunctionCall,Operation
from copy import deepcopy

class PersControllerUndo(PersonController):
    def __init__(self,person,undoController,acts):
        PersonController.__init__(self, person,acts)
        self._undocontroller=undoController
        self._acts=acts

    def addperson(self,arg1,arg2,arg3,arg4):
        PersonController.addperson(self, arg1, arg2, arg3, arg4)
        redo=FunctionCall(self.addperson,arg1,arg2,arg3,arg4)
        undo=FunctionCall(self.removeperson,arg1)
        self._undocontroller.add_operationList([Operation(undo,redo)])
        
        
    def removeperson(self, arg1):
        for i in PersonController.printperson(self):
            if int(i[0])==int(arg1):
                arg7=i[1],i[2],i[3]
        arg4=deepcopy(self._acts.get_activity())
        PersonController.removeperson(self, arg1)
        redo=FunctionCall(self.removeperson,arg1)
        undo=FunctionCall(self.addperson,arg1,arg7[0],arg7[1],arg7[2])
        op=Operation(undo,redo)
        oplist=[]
        oplist.append(op)
        redolist=FunctionCall(self._acts.setup,self._acts.get_activity())
        undolist=FunctionCall(self._acts.setup,arg4)
        newop=Operation(undolist,redolist)
        oplist.append(newop)
        self._undocontroller.add_operationList(oplist)
 
    def updateperson(self, arg1, arg2, arg3, arg4, arg5):
        for i in PersonController.printperson(self):
            if int(i[0])==int(arg1):
                arg=i[1],i[2],i[3]
        PersonController.updateperson(self, arg1, arg2, arg3, arg4, arg5)
        undo=FunctionCall(self.updateperson,arg1,arg[0],arg[1],arg[2],arg5)
        redo=FunctionCall(self.updateperson,arg1,arg2,arg3,arg4,arg5)
        self._undocontroller.add_operationList([Operation(undo,redo)])
        
        
class ActControllerUndo(ActivityController):
    def __init__(self,acts,undoController,person):
        ActivityController.__init__(self, acts,person)
        self._undocontroller=undoController
        self._pers=person
        
    def addactivity(self, arg1, arg2, arg3, arg4, arg5):
        ActivityController.addactivity(self, arg1, arg2, arg3, arg4, arg5)
        redo=FunctionCall(self.addactivity,arg1,arg2,arg3,arg4,arg5)
        undo=FunctionCall(self.removeactivity,arg1)
        self._undocontroller.add_operationList([Operation(undo,redo)])
        
    def set_Up(self, res):
        ActivityController.set_Up(self, res)    
        
    def removeactivity(self, arg1):
        arg5=deepcopy(ActivityController.printactivity(self))
        arg4=deepcopy(self._pers.get_person())
        ActivityController.removeactivity(self, arg1)
        redo=FunctionCall(self.set_Up,ActivityController.printactivity(self))
        undo=FunctionCall(self.set_Up,arg5)
        op=Operation(undo,redo)
        oplist=[]
        oplist.append(op)
        redolist=FunctionCall(self._pers.Setup,self._pers.get_person())
        undolist=FunctionCall(self._pers.Setup,arg4)
        newop=Operation(undolist,redolist)
        oplist.append(newop)
        self._undocontroller.add_operationList(oplist)
        
    def updateactivity(self, arg1, arg2, arg3, arg4, arg5, arg6):
        for i in ActivityController.printactivity(self):
            if int(i[0])==int(arg1):
                arg=i[1],i[2],i[3],i[4]
        ActivityController.updateactivity(self, arg1, arg2, arg3, arg4, arg5, arg6)
        undo=FunctionCall(self.updateactivity,arg1,arg[0],arg[1],arg[2],arg[3],arg6)
        redo=FunctionCall(self.updateactivity,arg1, arg2, arg3, arg4, arg5, arg6)
        self._undocontroller.add_operationList([Operation(undo,redo)])
        