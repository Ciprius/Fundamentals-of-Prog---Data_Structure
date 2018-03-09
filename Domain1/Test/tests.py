'''
Created on Nov 22, 2016

@author: Cipri
'''
import unittest
from Domain1.Repository.Repository import PersonRepository,ActivityRepository
from Domain1.Controller.Controller import PersonController,ActivityController
from Domain1.Controller.Controller import ControllerException
from Domain1.UI.UI import Validation
from copy import deepcopy

class RepoTest(unittest.TestCase):
    def setUp(self):
        perstest=PersonRepository()
        actstest=ActivityRepository()
        self._valid=Validation()
        perstest.add_person(11,'Maria Pop','0705835438','Aleea Tarnavelor nr.9')
        perstest.add_person(15,'Alexandru Buhai','0647537454','Strada Potaisa nr.60')
        perstest.add_person(1,'Gigi Luigi','0245632656','Aleea Padin nr.12')
        perstest.add_person(2,'Adi Costea','0543627546','Strada Brasov nr.2')
        perstest.add_person(3,'Gigel Frone','0245635422','Bulevardu Eroilor nr.10')
        
        actstest.add_activity(1,[11,15],'2016-6-24','16:56','No description')
        actstest.add_activity(2,[1],'2016-6-24','8:40','No description')
        actstest.add_activity(4,[2],'2016-9-30','12:45','Great View')
        actstest.add_activity(3,[3,1,2],'2016-3-13','14:30','No description')
        actstest.add_activity(6,[15],'2016-2-19','18:10','Awesome places')
        actstest.add_activity(7,[3,11],'2016-8-23','16:56','Great Zoo')
        
        self.perscont=PersonController(perstest)
        self.actscont=ActivityController(actstest)
    
        
    def test_add_person(self):
        self.a=("fbgbd")
        self.assertRaises(ControllerException,self.perscont.test_type,self.a)
        self.a=("11")
        self.assertRaises(ControllerException,self.perscont.test_find,self.a)
        self.perscont.addperson(14,'Niculai Ioan','0770654765','Strada  Dorobantiilor nr.4')
        self.assertEqual(len(self.perscont.printperson()),6)
        
    def test_remove_person_id(self):
        self.a=("ghjyutyughghjg")
        self.assertRaises(ControllerException,self.perscont.test_type,self.a)
        self.a=("40")
        self.assertRaises(ControllerException,self.perscont.test_exist,self.a)
        arg2=deepcopy(self.actscont.printactivity())
        arg3=deepcopy(self.perscont.printperson())
        res=self.perscont.removeperson(15,arg2,arg3)
        self.actscont.set_Up(res)
        self.assertEqual(len(self.perscont.printperson()),4)
        
    def test_update_person(self):
        self.a=("ggjgjgjgjgjgjgjgjg")
        self.assertRaises(ControllerException,self.perscont.test_type,self.a)
        self.a=("2055")
        self.assertRaises(ControllerException,self.perscont.test_exist,self.a)
        
    def test_search_person(self):
        self.a=("motor")
        self.assertRaises(ControllerException,self.perscont.test_exist,self.a)
        self.a=("4gghhh")
        self.assertRaises(ControllerException,self.perscont.test_exist,self.a)
        res=self.perscont.searchname('Alexandru')
        self.assertEqual(len(res),1)
    
    def test_search_phone(self):
        self.a=('6hgjhgjhgj')
        self.assertRaises(ControllerException,self.perscont.test_phone,self.a)
        self.a=('0876')
        self.assertRaises(ControllerException,self.perscont.test_phone,self.a)
        res=self.perscont.searchphone('0705835438')
        self.assertEqual(len(res),1)
    
    def test_serach_date(self):
        self.a=("gggjjhhh")
        self.assertRaises(ControllerException,self.actscont.test_date,self.a)
        self.a=("16:6-55556")
        self.assertRaises(ControllerException,self.actscont.test_date,self.a)
        self.a=("12-4")
        self.assertRaises(ControllerException,self.actscont.test_date,self.a)
        self.a=("2012-12-24")
        self.assertTrue(self.actscont.test_date,self.a)
        res=self.actscont.searchdate('2012-12-24')
        self.assertEqual(len(res),2)
        
    def test_search_time(self):
        self.a=("gjj33hgg")
        self.assertRaises(ControllerException,self.actscont.test_time,self.a)
        self.a=("19:009")
        self.assertRaises(ControllerException,self.actscont.test_time,self.a)
        self.a=("20:56")
        self.assertTrue(self.actscont.test_time,self.a)
        res=self.actscont.searchtime('20:56')
        self.assertEqual(len(res),2)
    
    def test_search_description(self):
        self.a=("fjfjfhh hhgg")
        res=self.actscont.searchdescription(self.a)
        self.assertEqual(len(res),0)
        self.a=("ff 485")
        res=self.actscont.searchdescription(self.a)
        self.assertEqual(len(res),0)
        self.a=("No View")
        res=self.actscont.searchdescription(self.a)
        self.assertEqual(len(res),4)
    
    def test_add_activty(self):
        self.a=("fkggjb")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
        self.a=("1")
        self.assertRaises(ControllerException,self.actscont.test_Find,self.a)
        self.actscont.addactivity(5,[11,2,3],'2016-6-28','16:7','No description')
        self.assertEqual(len(self.actscont.printactivity()),7)
      
    def test_remove_activity(self):
        self.a=("fhghghghg")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)  
        self.a=("5006")
        self.assertRaises(ControllerException,self.actscont.test_Find,self.a)
        self.a=('1')

    def test_update_activity(self):
        self.a=("hdfgjkh")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
        self.a=("5668855")
        self.assertRaises(ControllerException,self.actscont.test_Find,self.a)
        self.a=("h888")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
    
    def test_stats_1(self):
        self.a=("fff")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
        self.a=("778")
        self.assertRaises(ControllerException,self.actscont.test_day,self.a)
        self.a=("24")
        res=self.actscont.stats1(self.a)
        self.assertEqual(len(res),2)
    
    def test_stats_2(self):
        res=self.actscont.stats2()
        self.assertEqual(len(res),5)
        
    def test_stats_3(self):
        self.a=("gfhkh")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
        self.a=("5666")
        self.assertRaises(ControllerException,self.actscont.test_Find,self.a)
        self.a=("5hh")
        self.assertRaises(ControllerException,self.actscont.test_Type,self.a)
        self.a=('1')
        res=self.actscont.stats3(self.a)
        self.assertEqual(len(res),2)
        
    def test_stats_4(self):
        res=self.perscont.stats4(self.actscont.printactivity())
        self.assertEqual(len(res),5)
        for i in res:
            self.assertEqual(i[2],2)
    
    
    