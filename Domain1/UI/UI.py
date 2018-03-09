'''
Created on Nov 20, 2016

@author: Cipri
'''
import datetime
import time
from copy import deepcopy

    
class Interface:
    
    def __init__(self,perscontroller,actscontroller,undocontroller):
        self._perscontroller=perscontroller
        self._actscontroller=actscontroller
        self._undocontroller=undocontroller
        
    def _printMenu(self):
        menuString = '\nAvailable commands:\n'
        menuString +='\t  1-add  \n'
        menuString +='\t  2-remove \n'
        menuString +='\t  3-update \n'
        menuString +='\t  4-search \n'
        menuString +='\t  5-statistics\n'
        menuString +='\t  6-undo\n'
        menuString +='\t  7-redo\n'
        menuString +='\t  8-list\n'
        menuString +='\t  9-exit\n'
        print(menuString)
    def _interface(self):
        while True:
            self._printMenu()
            com=self._command()
            if com=='1':
                while True:
                    print("0 exit")
                    print("1 add person")
                    print("2 add activity")
                    com1=input("Give the command:")
                    if com1=='1':
                        self.ui_add_person()
                    elif com1=='2':
                        self.ui_add_activity()
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")            
            elif com=='2':
                while True:
                    print("0 exit")
                    print("1 remove person by ID")
                    print("2 remove person by name")
                    print("3 remove activity by ID")
                    com1=input("Give the command:")
                    if com1=='1':
                        self.ui_remove()
                    elif com1=='2':
                        self.ui_remove_name()
                    elif com1=='3':
                        self.ui_remove_activity()
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")
            elif com=='3':
                while True:
                    print("0 exit")
                    print("1 update person list")
                    print("2 update activity list")
                    com1=input("Give the command:")
                    if com1=='1':
                        self.ui_update_person()
                    elif com1=='2':
                        self.ui_update_activity()
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")
            elif com=='4':
                while True:
                    print("0 exit")
                    print("1 search person")
                    print("2 search activity")
                    com1=input("Give the command:")
                    if com1=='1':
                        self.ui_search_person()
                    elif com1=='2':
                        self.ui_search_activity()
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")
            elif com=='5':
                while True:
                    print("0 exit")
                    print("1 statistics for a given day")
                    print("2 statistics for the busiest day")
                    print("3 statistics for a given person")
                    print("4 statistics for the most active person")
                    com1=input("Give the command:")
                    if com1=='1':
                        self.ui_stats_1()
                    elif com1=='2':
                        self.ui_stats_2()
                    elif com1=='3':
                        self.ui_stats_3()
                    elif com1=='4':
                        self.ui_stats_4()
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")
            elif com=='6':
                if self._undocontroller._index > -1:
                    self._undocontroller.undo()
                    self._ui_print_person(None)
                    print()
                    self._ui_print_activity(None)
                else:
                    print("No more undo posible!!")
            elif com=='7':
                if self._undocontroller._index == len(self._undocontroller._operations)-1:
                    print("No more redo avaible!!")
                else:
                    self._undocontroller.redo()
                    self._ui_print_person(None)
                    print()
                    self._ui_print_activity(None)                  
            elif com=='8':
                while True:
                    print("0 exit")
                    print("1 list the persons list")
                    print("2 list the activities list")
                    com1=input("Give the command:")
                    if com1=='1':
                        self._ui_print_person(None)
                    elif com1=='2':
                        self._ui_print_activity(None)
                    elif com1=='0':
                        break
                    else:
                        print("Wrong command!")
            elif com=='9':
                break
            elif com!='1' and com!='2' and  com!='3' and com!='4' and com!='5' and com!='6' and com!='7' and com!='8' and com!='9':
                print("Wrong command")
                
    def _print_1(self,mylist1=None,mylist2=None):
        '''
        This function display the elements from a list
        '''
        if mylist1!=None and mylist2==None:
            for i in mylist1:
                print('Day:',str(i[0]).ljust(4),'Have ',str(i[1]).ljust(2),' activities')
        if mylist1==None and mylist2!=None:
            for i in mylist2:
                print('IDp:',str(i[0]).ljust(4),'Name:',i[1].ljust(20),'Go to ',i[2],' activities')

    def _ui_print_person(self,mylist=None):
        '''
        This function display the elements from person list and activity list
        '''
        if mylist== None:
            for i in self._perscontroller.printperson():
                print('IDp:',str(i[0]).ljust(4),'Name:',i[1].ljust(20),'Phone:',i[2].ljust(13),'Address:',i[3])
        else:
            for i in mylist:
                print('IDp:',str(i[0]).ljust(4),'Name:',i[1].ljust(20),'Phone:',str(i[2]).ljust(13),'Address:',i[3])
    def _ui_print_activity(self,mylist=None):
        '''
        This function display the elements from person list and activity list
        '''
        if mylist==None:     
            for i in self._actscontroller.printactivity():
                print('IDa:',str(i[0]).ljust(4),'Person_IDs:',str(i[1]).ljust(30),'Date:',i[2].ljust(15),'Time:',i[3].ljust(10),'Description:',i[4])
        else:
            for i in mylist:
                print('IDa:',str(i[0]).ljust(4),'Person_IDs:',str(i[1]).ljust(30),'Date:',i[2].ljust(15),'Time:',i[3].ljust(10),'Description:',i[4])
     
    def _command(self):
        '''
        This function allows the user to give commands
        Output:cmd,command-are the commands given by the user
        args-are the arguments given by the user
        '''
        command=input("Give a command:")
        pos=command.find(" ")
        if pos==-1:
            return command
        else:
            return command
        
    def ui_add_person(self):
        '''
        This function adds a new element to the list
        '''
        arg1=input("Give the person_id:")
        arg2=input("Give the name:")
        arg3=input("Give the phone number:")
        arg4=input("Give the address:")
        r=Validation()
        arg=self._perscontroller.printperson()
        while r.valid(arg1)==False or r.valid(arg3)==False or r.valid_per(arg1,arg)==False or len(arg3)!=10:
            print("Make sure that your pers_id,phone number are integers and pers_id doesn't exit in the list!")
            arg1=input("Give the person_id:")
            arg2=input("Give the name:")
            arg3=input("Give the phone number:")
            arg4=input("Give the address:")
        self._perscontroller.addperson(int(arg1),arg2,arg3,arg4)
        
    def ui_add_activity(self):
        '''
        This function adds a new element to the list
        '''
        arg1=input("Give the activity_id:")
        arg2=input("Give the persons_id:")
        arg3=input("Give the date:")
        arg4=input("Give the time:")
        arg5=input("Give the description:")
        r=Validation()
        arg2=[x for x in arg2.split(' ') ]
        arg=self._perscontroller.printperson()
        arg0=self._actscontroller.printactivity()
        
        while r.valid(arg1)==False or r.valid_act(arg1, arg0)==False:
            print("Give an integer number which doesn't exist in the list!")
            arg1=input("Give the activity_id:")
        
        while r.valid_activities(arg2)==False or r.validation(arg2,arg)==False:
            print("Give some person_id which already exist!")
            arg2=input("Give the persons_id:")
            arg2=[x for x in arg2.split(' ') ]
        
        while r.valid_date(arg3)==False or r.valid_time(arg4)==False or r.valid_date_time(arg3, arg4, arg0)==False:
                print("Give a valid date and time format!")
                arg3=input("Give the date:")
                arg4=input("Give the time:")
                       
        arg2=[int(x) for x in arg2]
        self._actscontroller.addactivity(int(arg1),list(arg2),arg3,arg4,arg5)

    def ui_remove(self):
        '''
        This function remove a person from the list by it's id
        '''
        r=Validation()
        arg1=input("Give the person_id:")
        arg=self._perscontroller.printperson()
        while r.valid(arg1)==False:
            print("Make sure that the person_id is a integer which exist in the list!")
            if r.valid_per(arg1,arg)==False:
                arg1=input("Give the person_id:")
        #arg2=self._actscontroller.printactivity()   
        self._perscontroller.removeperson(arg1)

    def ui_remove_activity(self):
        '''
        This function remove an activity from the list by it's id
        '''
        r=Validation()
        arg1=input("Give the acitivity_id:")
        arg=self._actscontroller.printactivity()
        while r.valid(arg1)==False:
            print("Make sure that the activity_id is an integer which doesn't exist in the list!")
            if r.valid_act(arg1,arg)==True:
                arg1=input("Give the acitivity_id:")
        self._actscontroller.removeactivity(arg1)

        
    def ui_remove_name(self):
        '''
        This function remove a person from the list by it's name
        '''
        r=Validation()
        arg1=input("Give the name:")
        arg=self._perscontroller.printperson()
        if r.valid_name(arg1,arg)==False:
            print("Give a name which exist in the list!")
            arg1=input("Give the name:")
        self._perscontroller.removename(arg1)

        
    def ui_update_person(self):
        '''
        This function updates the person list
        '''
        r=Validation()
        arg1=input("Give the person_id:")
        arg2=input("Give the name:")
        arg3=input("Give the phone number:")
        arg4=input("Give the address:")
        arg=self._perscontroller.printperson()
        while r.valid(arg1)==False or r.valid(arg3)==False or len(arg3)!=10 or r.valid_per(arg1,arg)==True or r.valid_phone(arg3, arg)==True:
            print("Make sure that the person_id is an integer which doesn't exist in the list also the phone number must be unique!")
            arg1=input("Give the person_id:")
            arg2=input("Give the name:")
            arg3=input("Give the phone number:")
            arg4=input("Give the address:")
        arg5=deepcopy(self._perscontroller.printperson())
        self._perscontroller.updateperson(arg1,arg2,arg3,arg4,arg5)
        
    def ui_update_activity(self):
        '''
        This function updates the activity list
        '''
        r=Validation()
        arg1=input("Give the activity_id:")
        arg2=input("Give the persons_id:")
        arg3=input("Give the date:")
        arg4=input("Give the time:")
        arg5=input("Give the description:")
        arg2=[x for x in arg2.split(' ') ]
        arg=self._perscontroller.printperson()
        arg0=self._actscontroller.printactivity()
        while r.valid(arg1)==False or r.valid_act(arg1, arg0)==True:
            print("Give an integer number which exist in the list!")
            arg1=input("Give the activity_id:")
        
        while r.valid_activities(arg2)==False or r.validation(arg2,arg)==False:
            print("Give some person_id which already exist!")
            arg2=input("Give the persons_id:")
            arg2=[x for x in arg2.split(' ') ]
        
        while r.valid_date(arg3)==False or r.valid_time(arg4)==False or r.valid_date_time(arg3, arg4, arg0)==False:
                print("Give a valid date and time format!")
                arg3=input("Give the date:")
                arg4=input("Give the time:")
                       
        arg2=[int(x) for x in arg2]
        arg6=deepcopy(self._actscontroller.printactivity())
        self._actscontroller.updateactivity(arg1,list(arg2),arg3,arg4,arg5,arg6)
    
    def ui_search_person(self):
        '''
        This function search in the person list a person by it's name or phone number
        '''
        r=Validation()
        arg1=input("Search for name or phone:")
        if arg1=='name' or arg1=='Name':
            arg2=input("Give the name:")
            res=self._perscontroller.searchname(arg2)
            if len(res)!=0:
                self._ui_print_person(res)
            else:
                print("Couldn't find anything!")
        elif arg1=='phone' or arg1=='Phone':
            arg2=input("Give the phone number:")
            arg=self._perscontroller.printperson()
            while r.valid(arg2)==False or len(arg2)!=10 or r.valid_phone(arg2,arg)==False:
                print("Make sure that the phone number is an integer, it's length is 10 and is in the person list!")
                arg2=input("Give the phone number:")
            res=self._perscontroller.searchphone(arg2)
            self._ui_print_person(res)
        else:
            print("Wrong command!")
    def ui_search_activity(self):
        '''
        This function search in the activity list an activity by it's date or time or description
        '''
        r=Validation()
        arg1=input("Search for date or time or description:")
        if arg1=='date' or arg1=='Date':
            arg2=input("Give the date:")
            while r.valid_date(arg2)==False:
                print("Give a valid date format!")
                arg2=input("Give the date:")
            res=self._actscontroller.searchdate(arg2)
            if len(res)!=0:
                self._ui_print_activity(res)
            else:
                print("Couldn't find anything!")
        elif arg1=='time' or arg1=='Time':
            arg2=input("give the time:")
            while r.valid_time(arg2)==False:
                print("Give a valid time format!")
                arg2=input("give the time:")
            res=self._actscontroller.searchtime(arg2)
            if len(res)!=0:
                self._ui_print_activity(res)
            else:
                print("Couldn't find anything!")
        elif arg1=='description' or arg1=='Description':
            arg2=input("Give the description:")
            res=self._actscontroller.searchdescription(arg2)
            if len(res)!=0:
                self._ui_print_activity(res)
            else:
                print("Wrong description!")
        else:
            print("Wrong argument given!")
        
    def ui_stats_1(self):
        '''
        This function make a statistic of the activities from a given day
        '''
        r=Validation()
        arg1=input("Give the day:")
        arg=self._actscontroller.printactivity()
        while r.valid_day(arg1,arg)==False:
            print("Make sure that the day exist in the list!")
            arg1=input("Give the day:")
        res=self._actscontroller.stats1(arg1)
        #res.sort(key=lambda res:datetime.datetime.strptime(res[3], '%H:%M'))
        res=gnome_sort(sort_time,res,3)
        self._ui_print_activity(res) 
    
    def ui_stats_2(self):
        '''
        This function make a statistic of the busiest days in which the persons participates
        '''
        res=self._actscontroller.stats2()
        res=gnome_sort(sort_numbers,res,1)
        res.reverse()
        print("The most busiest days are:")
        self._print_1(res,None)
        
    def ui_stats_3(self):
        '''
        This function make a statistic for a given person_id
        '''
        r=Validation()
        arg1=input("Give the person_id:")
        arg=self._perscontroller.printperson()
        while r.valid(arg1)==False:
            print("Make sure that the person_id is an integer an exist in the person list!")
            if r.valid_per(arg1,arg)==False:
                arg1=input("Give the person_id:")
        res=self._actscontroller.stats3(arg1)
        self._ui_print_activity(res)

    def ui_stats_4(self):
        '''
        This function make a statistic of the most active persons
        '''
        arg=self._actscontroller.printactivity()
        res=self._perscontroller.stats4(arg)
        res=gnome_sort(sort_numbers,res,2)
        res.reverse()
        print("The most active persons are:")
        self._print_1(None,res)
                  
class Validation:
            
    def valid(self,arg):
        '''
        This function checks if the can be converted into integer
        arg - The parameter to check
        ValueError if the number can't be converted
        '''
        try:
            int(arg)
            return True
        except ValueError:
            return False
        
    def valid_per(self,arg1,arg):
        '''
        This function checks if the parameter already exists
        arg - The parameter to check
        Output:Return True if it's not in person list or False otherwise
        '''
        for i in arg:
            if int(i[0])==int(arg1):
                return False
        return True
    
    def valid_date(self,arg):
        '''
        This function checks if the date it's correct
        arg - The parameter to check
        ValueError if the parameter is not the type date
        '''
        try:
            datetime.datetime.strptime(arg, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def valid_time(self,arg):
        '''
        This function checks if the time it's correct
        arg - The parameter to check
        ValueError if the parameter is not the type time
        '''
        try:
            time.strptime(arg, '%H:%M')
            return True
        except ValueError:
            return False
        
    def valid_act(self,arg1,arg):
        '''
        This function checks if the parameter already exists
        arg - The parameter to check
        Output:Return True if it's not in activity list or False otherwise
        '''
        for i in arg:
            if int(i[0])==int(arg1):
                return False
        return True
        
    def validation(self,arg2,arg):
        '''
        This function checks if all the person_ids already exist
        Input:arg2-the list to check
        Output":True if exist False otherwise
        '''
        c=0
        for i in list(arg2):
            if self.valid_per(i,arg)==False:
                c=c+1
        if c==len(arg2):
            return True
        else:
            return False
    
    def valid_name(self,arg1,arg):
        '''
        This function checks if the name already exist in the list
        Input:arg1-the name to check
        Output:True if it's in the list False otherwise
        '''
        for i in arg:
            if i[1]==arg1:
                return True
        return False
    
    def valid_activities(self,arg2):
        '''
        This function checks if all the person_ids are integer
        Input:arg2-the list to check
        Output:True if all the elements can be converted False otherwise
        '''
        try:
            for i in arg2:
                int(i)
            return True
        except ValueError:
            return False
        
    def valid_date_time(self,arg1,arg2,arg):
        '''
        This function checks if the date and the time already exist in the list
        Input:arg1-the date to check,arg2-the time to check
        Output:False if it's in the list True otherwise        
        '''
        for i in arg:
            if i[2]==arg1 and i[3]==arg2:
                return False
        return True
    
    def valid_phone(self,arg1,arg):
        '''
        This function checks if the phone number already exist in the list
        Input:arg1-the phone number to check
        Output:True if it's in the list False otherwise        
        '''
        for i in arg:
            if i[2]==arg1:
                return True
        return False
    
    def valid_day(self,arg1,arg):
        '''
        This function checks if the day already exist in the list
        Input:arg1-the day to check
        Output:True if it's in the list False otherwise
        '''
        for i in arg:
            d=i[2].split("-")
            if int(d[2])==int(arg1):
                return True
        return False
    
def sort_time(arg1,arg2):
    '''
    This function compare two date times
    input: arg1,arg2 two dates which must be compared
    output:returns True if arg1<=arg2,False otherwise
    '''
    timeA = datetime.datetime.strptime(arg1, "%H:%M")
    timeB = datetime.datetime.strptime(arg2, "%H:%M")
    return timeA<=timeB
    
def sort_numbers(arg1,arg2):
    '''
    This function compare two numbers
    input:arg1,arg2 two numbers which must be compared
    output:returns True if arg1<=arg2,False otherwise
    '''
    return arg1<=arg2
    

def gnome_sort(functie,lista,c):
    '''
    This function sort the elements from a list
    output:returns the list sorted
    '''
    i,j,size = 1,2,len(lista)
    while i < size:
        if functie(lista[i-1][c],lista[i][c]) ==True:
            i,j = j, j+1
        else:
            lista[i-1],lista[i] = lista[i],lista[i-1]
            i -= 1
            if i == 0:
                i,j = j, j+1
    return lista
    
                
