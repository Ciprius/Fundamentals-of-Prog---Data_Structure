'''
Created on Nov 20, 2016

@author: Cipri
'''
from Domain1.Controller.ControllerException import ControllerException
import datetime
import time

class PersonController:
    
    def __init__(self, person,acts):
        self.__person=person
        self.__activtiy=acts
    
    def addperson(self,arg1,arg2,arg3,arg4):
        '''
        This function calls add_person from Repository to add a person
        '''
        self.__person.add_person(arg1,arg2,arg3,arg4)
    
    def set_up(self,res):
        self.__person.Setup(res)    
        
    def removeperson(self,arg1):
        '''
        This function calls remove_person from Repository to remove a person
        '''
        k=0
        self.__person.remove_person(arg1)
        for i in self.__activtiy.get_activity():
            c=self.__person.find(i[1],arg1)
            if c > -1:
                self.__activtiy.get_activity()[k][1].pop(c)
            k=k+1
        self.__activtiy.setup(self.__activtiy.get_activity())

    def removename(self,arg1):
        '''
        This function calls remove_name from Repository to remove a person
        '''
        k=0
        res=self.__person.find_id(arg1)
        self.__person.remove_name(arg1)
        for i in self.__activtiy.get_activity():
            c=self.__person.find(i[1],res)
            if c > -1:
                self.__activtiy.get_activity()[k][1].pop(c)
            k=k+1
        self.__activtiy.setup(self.__activtiy.get_activity())
        
    def updateperson(self,arg1,arg2,arg3,arg4,arg5):
        '''
        This function calls update_person from Repository to update a person
        '''
        self.__person.update_person(arg1,arg2,arg3,arg4,arg5)

    def printperson(self):
        '''
        This function calls get_person from Repository to list the person list
        '''
        return self.__person.get_person()
    
    def searchname(self,arg1):
        '''
        Returns all the elements which have the same first or second name
        '''
        return self.__person.search_name(arg1)
    
    def searchphone(self,arg1):
        '''
        Returns all the elements which have the same phone_number
        '''
        return self.__person.search_phone(arg1)
    
    def stats4(self,arg1):
        '''
        This function build a new list which contains the sum of the activities to which a person participates
        Input:arg1-the list of actitivities
        Output:res a new list which contains the person_id,name,the sum of the activity attended
        '''
        res=[]
        for i in self.__person.get_person():
            res.append(list(self.__person.stat_4(int(i[0]),i[1],arg1)))
        return res
        
    def test_type(self,arg):
        if arg.isdigit() == False:
            raise ControllerException("Wrong type")

    def test_find(self,arg):
        for i in self.__person.get_person():
            if i[0]==int(arg):
                raise ControllerException("The id already exist")
            
    def test_exist(self,arg):
        c=0
        try:
            int(arg)
            for i in self.__person.get_person():
                if i[0]==int(arg):
                    c=c+1
        except ValueError:
            for i in self.__person.get_person():
                if i[1]==arg:
                    c=c+1
        if c==0:
            raise ControllerException("The number does not exist in the list")
    
    def test_phone(self,arg):
        try:
            int(arg)
            if len(arg)==10:
                c=0
                for i in self.__person.printperson():
                    if i[2]==arg:
                        c=c+1
                if c==0:
                    raise ControllerException("The phone number doesn't exist")
            else:
                raise ControllerException("The phone number doesn't have 10 digits")
        except ValueError:
            raise ControllerException("The phone number contains characters")
    
    
class ActivityController:
    
    def __init__(self,activity,person):
        self.__activity=activity
        self.__pers=person
    
    def addactivity(self,arg1,arg2,arg3,arg4,arg5):
        '''
        This function calls add_activity from Repository to add an activity
        '''
        self.__activity.add_activity(arg1,arg2,arg3,arg4,arg5)
        
    def removeactivity(self,arg1):
        '''
        This function calls remove_activity from Repository to remove an activity
        '''
        res=self.__activity.find_act(arg1)
        self.__activity.remove_activity(arg1)
        for i in res:
            self.__pers.remove_person(i)
            k=0
            for j in self.__activity.get_activity():
                c= self.__pers.find(j[1],i)
                if c > -1:
                    self.__activity.get_activity()[k][1].pop(c)
                k=k+1
        
    def set_Up(self,res):
        self.__activity.setup(res)
        
    def updateactivity(self,arg1,arg2,arg3,arg4,arg5,arg6):
        '''
        This function calls update_activity from Repository to update an activity
        '''
        self.__activity.update_activity(arg1,list(arg2),arg3,arg4,arg5,arg6)
        
    def printactivity(self):
        '''
        This function calls get_activity from Repository to list activity list
        '''
        return self.__activity.get_activity()
    
    def searchdate(self,arg1):
        '''
        Returns all the elements which have the same year or day or month
        '''
        return self.__activity.search_date(arg1)
    
    def searchtime(self,arg1):
        '''
        Returns all the elements which have the same hour or minutes
        '''
        return self.__activity.search_time(arg1)
    
    def searchdescription(self,arg1):
        '''
        Returns all the elements which have the same description
        '''
        return self.__activity.search_description(arg1)
        
    def stats1(self,arg1):
        '''
        This function search in the list a specific day
        Input:arg1- the day to search
        Output:res a new list containing the elements with the same day as arg1
        '''
        res=[]
        for i in self.__activity.get_activity():
            d=i[2].split("-")
            if d[2]==arg1:
                res.append(list(self.__activity.stat_1(i[0],i[1],i[2],i[3],i[4])))
        return res
        
        
    def stats3(self,arg1):
        '''
        This function search in the list a specific person_id
        Input:arg1- the person_id to search
        Output:res a new list containing the activity to which arg1 participates
        '''    
        res=[]
        for i in self.__activity.get_activity():
            if self.__activity.stat_3(i[1],arg1)==True:
                res.append(i)
        return res
    
    def stats2(self):
        '''
        This function build a new list which contains the days and the total number of activities
        Output:res a new list containing the days and the activities
        '''
        res=[]
        app=[0 for x in range(0,31)]
        for i in self.__activity.get_activity():
            d=i[2].split("-")
            app[int(d[2])]+=1
            if app[int(d[2])]==1:
                res.append(list(self.__activity.stat_2(d[2])))
        return res
        
    def test_Type(self,arg):
        if arg.isdigit()==False:
            raise ControllerException("The id must be an integer")
        
    def test_Find(self,arg):
        c=0
        for i in self.__activity.get_activity():
            if i[0]==int(arg):
                c=c+1
                raise ControllerException("The number already exist")
        if c==0:
            raise ControllerException("The number doesn't exist") 
            
    def test_date(self,arg):
        try:
            datetime.datetime.strptime(arg, '%Y-%m-%d')
            return True
        except ValueError:
            raise ControllerException("Wrong date format")
        
    def test_time(self,arg):
        try:
            time.strptime(arg, '%H:%M')
            return True
        except ValueError:
            raise ControllerException("Wrong time format")
    
    def test_day(self,arg):
        c=0
        for i in self.__activity.get_activity():
            d=i[2].split("-")
            if d[1]==int(arg):
                c=c+1
        if c==0:
            raise ControllerException("The day doesn't exist")