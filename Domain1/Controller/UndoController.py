'''
Created on Dec 12, 2016

@author: Cipri
'''
class UndoController:
    def __init__(self,person,activity,pers_undo,acts_undo):
        self._person=person
        self._activity=activity
        self.undo_list_person=[]
        self.undo_list_person.append(list(pers_undo))
        self.undo_list_activity=[]
        self.undo_list_activity.append(list(acts_undo))
        self.redo_person=[]
        self.redo_activity=[]
   
    def add_undo_person(self,res,res1):
        self.undo_list_person.append(list(res))
        self.undo_list_activity.append(list(res1))
        
    def remove_undo_person(self,res1,res):
        self.undo_list_person.append(list(res1))
        self.undo_list_activity.append(list(res))
        
    def update_undo_person(self,res,res1):
        self.undo_list_person.append(list(res))
        self.undo_list_activity.append(list(res1))
        
    def add_undo_activity(self,res,res1):
        self.undo_list_activity.append(list(res))
        self.undo_list_person.append(list(res1))
        
    def remove_undo_activity(self,res,res1):
        self.undo_list_activity.append(list(res))
        self.undo_list_person.append(list(res1))

    def update_undo_activity(self,res,res1):
        self.undo_list_activity.append(list(res))
        self.undo_list_person.append(list(res1))
        
    def Undo(self):
        per=[]
        res=[]
        if len(self.undo_list_activity)!=0 and len(self.undo_list_person)!=0:
            
            if len(self.undo_list_person)!=1:
                    self.undo_list_person.reverse()
                    pp=self.undo_list_person[1]
                    res=pp
                    self.redo_person.append(self.undo_list_person[0])
                    self.undo_list_person.pop(0)
                    self.undo_list_person.reverse()
            elif len(self.undo_list_person)==1:
                self.redo_person.append(self.undo_list_person)
                self.undo_list_person.pop(0)

            if len(self.undo_list_activity)!=1:
                self.undo_list_activity.reverse()
                pp=self.undo_list_activity[1]
                per=pp
                self.redo_activity.append(self.undo_list_activity[0])
                self.undo_list_activity.pop(0)
                self.undo_list_activity.reverse()
            elif len(self.undo_list_activity)==1:
                self.redo_activity.append(self.undo_list_activity)
                self.undo_list_activity.pop(0)
        return res,per
    
    def Redo(self):
        res=[]
        per=[]
        
        if len(self.redo_person)!=0 and len(self.redo_activity)!=0:
            if len(self.redo_person)!=1:
                self.redo_person.reverse()
                pp=self.redo_person[0]
                res=pp
                self.redo_person.pop(0)
                self.redo_person.reverse()
            elif len(self.redo_person)==1:
                res=self.redo_person[0]
                self.redo_person.pop()
                
            if len(self.redo_activity)!=1:
                self.redo_activity.reverse()
                pp=self.redo_activity[0]
                per=pp
                self.redo_activity.pop(0)
                self.redo_activity.reverse()
            elif len(self.redo_activity)==1:
                per=self.redo_activity[0]
                self.redo_activity.pop()
        return res,per
