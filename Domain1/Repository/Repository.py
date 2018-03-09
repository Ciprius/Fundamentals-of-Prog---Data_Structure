'''
Created on Nov 20, 2016

@author: Cipri
'''
from Domain1.Data_Structure.Data_Structure import Data_Structure


class PersonRepository:
    def __init__(self):
        self.__data_person=Data_Structure()
        
    def add_person(self,arg1,arg2,arg3,arg4):
        '''
        Add a person to the person list
        '''   
        pers=arg1,arg2,arg3,arg4
        self.__data_person.append(pers)
            
    def get_person(self):
        return self.__data_person.Get()
    
    def Setup(self,res):
        self.__data_person.Set(res)
        
    def remove_name(self,arg1):
        '''
        This Controller remove all the elements which have the same name with a given one 
        arg - The name to remove 
        '''
        res=[x for x in self.get_person() if x[1]!=arg1]
        self.Setup(res)
        
    def find_id(self,arg1):
        for i in self.get_person():
            if i[1]==arg1:
                return i[0]
        
    def find(self,arg1,arg2):
        c=0
        for i in arg1:
            if i==int(arg2):
                return c
            else:
                c=c+1
        return -1
                        
    def remove_person(self,arg1):
        '''
        This Controller remove the person_id together with all it's elements
        arg - The person_id to remove
        '''
        res=[x for x in self.get_person() if int(x[0])!=int(arg1)]
        self.Setup(res)
                        
    def update_person(self,arg1,arg2,arg3,arg4,arg5):
        '''
        This Controller update the person list with something else
        arg1 - the person_id on which we apply the update
        arg(2,3,4) - the parameters to update 
        '''
        for i in arg5:
            if int(i[0])==int(arg1):
                i[1]=arg2
                i[2]=arg3
                i[3]=arg4
        self.Setup(arg5)
       
    def search_name(self,arg1):
        '''
        This function search in the list a specific name
        Input:arg1- the name to search
        Output:res a new list containing only the elements with the same name as arg1
        '''
        e=arg1.split(" ")
        arg=self.get_person()
        res=filterF(filter_name,arg,e,1)
        return res

    
    def search_phone(self,arg1):
        '''
        This function search in the list a specitic phone number
        Input:arg1 - the phone number to search
        Output:res a new list containing only the elements with the same phone number as arg1 
        '''
        arg=self.get_person()
        res=filterF(filter_phone,arg,arg1,2)
        return res
    
    def act_sum(self,arg1,arg2):
        '''
        This function checks if a person_id exist in the current activity
        Input:arg1-the activity list which contains the person_ids, arg2-the person_id
        Output:1 if the arg2 exist in the list 0 otherwise
        '''
        for i in arg1:
            if int(i)==int(arg2):
                return 1
        return 0
    
    def stat_4(self,arg1,arg2,arg3):
        '''
        This function compute the sum of the total activities to which a person participate
        Input:arg1-the person_id, arg2-the persons name, arg3-the list of the activities
        Output:arg1-the person_id, arg2-the persons name, s the sum of the activities
        '''
        s=0
        for i in arg3:
            s=s+self.act_sum(i[1],arg1)
        return arg1,arg2,s
            
            
class ActivityRepository:
    
    def __init__(self):
        self.__data_activity=Data_Structure()
        
    def get_activity(self):
        return self.__data_activity.Get()
    
    def setup(self,res):
        self.__data_activity.Set(res)
    
    def add_activity(self,arg1,arg2,arg3,arg4,arg5):
        '''
        Add an activity to the activity list
        '''   
        arg2=[int(x) for x in arg2]
        adr=arg1,arg2,arg3,arg4,arg5
        self.__data_activity.append(adr)
        
    def update_activity(self,arg1,arg2,arg3,arg4,arg5,arg6):
        '''
        This Controller update the activity list with something else
        arg1 - the activity_id on which we apply the update
        arg(2,3,4,5) - the parameters to update 
        '''
        for i in arg6:
            if int(i[0])==int(arg1):
                arg2=[int(x) for x in arg2]
                i[1]=arg2
                i[2]=arg3
                i[3]=arg4
                i[4]=arg5
        self.setup(arg6)
        
    def find_act(self,arg1):
        '''
        This function find the person_ids which participates at the activity with the id arg1
        intput:arg1-the activity id
        output:The list of person_ids
        '''
        for i in self.get_activity():
            if int(i[0])==int(arg1):
                return i[1]
 
    def remove_activity(self,arg):
        '''
        This function remove an activity together with all it's elements
        arg - The activity_id to remove
        '''
        res=[x for x in self.get_activity() if int(x[0])!=int(arg)]
        self.setup(res)
                
    def search_date(self,arg1):
        '''
        This function search in the list a specific date
        Input:arg1 - the date to search
        Output:res a new list containing the elements with the same date as arg1
        '''
        arg=self.get_activity()
        e=arg1.split("-")
        res=filterF(filter_date,arg,e,2)
        return res
    
    def search_time(self,arg1):
        '''
        This function search in the list a specific time
        Input:arg1 - the time to search
        Output:res a new list containing the elements with the same time as arg1
        '''
        e=arg1.split(":")
        arg=self.get_activity()
        res=filterF(filter_time,arg,e,3)
        return res
    
    def search_description(self,arg1):
        '''
        This function search in the list a specific description
        Input:arg1- the description to search
        Output:res a new list containing the elements with the same description as arg1
        '''
        e=arg1.split(" ")
        arg=self.get_activity()
        res=filterF(filter_name,arg,e,4)
        return res
    
    def stat_1(self,arg1,arg2,arg3,arg4,arg5):
        '''
        Returns the elements which have the same day
        '''   
        return arg1,arg2,arg3,arg4,arg5
    
    def stat_3(self,arg1,arg2):
        '''
        This function checks if a number exist in a list
        Input:arg1-the list ,arg2-the number to check
        Ouptput:returns True if the number exist in the list otherwise False
        '''     
        for i in arg1:
            if int(i)==int(arg2):
                return True
        return False
    
    def stat_2(self,arg1):
        '''
        This function computes the total sum of activities for a day
        Input:arg1- the day to check
        Output:arg1-the day, sum-the sum of the activities of arg1
        '''
        s=0
        for i in self.get_activity():
            d=i[2].split("-")
            if d[2]==arg1:
                s=s+len(i[1])
        return arg1,s
        
    
def filter_name(arg1,arg2):
    '''
    This function verifies if two names or descriptions are the same
    input:arg1,arg2 the elements to checks
    output:True if they are the same, False otherwise
    '''
    arg=arg1.split(" ")
    if len(arg2)==2:
        if arg[0]==arg2[0] or arg[0]==arg2[1] or arg[1]==arg2[0] or arg[1]==arg2[1]:
            return True
        else:
            return False
    else:
        if arg[0]==arg2[0] or arg[1]==arg2[0]:
            return True
        else:
            return False
        
def filter_phone(arg1,arg2):
    '''
    This function verifies if two phones are the same
    input:arg1,arg2 the elements to checks
    output:True if they are the same, False otherwise
    '''    
    if arg1==arg2:
        return True
    else:
        return False
    
def filter_date(arg1,arg2):
    '''
    This function verifies if two dates are the same
    input:arg1,arg2 the elements to checks
    output:True if they are the same, False otherwise
    '''
    arg=arg1.split("-")
    if arg[0]==arg2[0] or arg[1]==arg2[1] or arg[2]==arg2[2]:
        return True
    else:
        return False
    
def filter_time(arg1,arg2):
    '''
    This function verifies if two times are the same
    input:arg1,arg2 the elements to checks
    output:True if they are the same, False otherwise
    '''
    arg=arg1.split(":")
    if arg[0]==arg2[0] or arg[1]==arg2[1]:
        return True
    else:
        return False
    
def filterF(functie,lista,item,c):
    res=[]
    for i in lista:
        if functie(i[c],item)==True:
            res.append(list(i))
    return res
