'''
Created on Nov 20, 2016

@author: Cipri
'''
from Domain1.Repository.RepositoryPickleActivity import PickleActivityRepository
from Domain1.Repository.RepositoryPicklePerson import PicklePersonRepository
from Domain1.Repository.RepositoryFileActivity import FileActivityRepository
from Domain1.Repository.RepositoryFilePerson import FilePersonRepository
from Domain1.Controller.ControllerWithUndo import PersControllerUndo,ActControllerUndo
from Domain1.Controller.undoController1 import UndoController
from Domain1.Controller.Controller import PersonController,ActivityController
from Domain1.UI.UI import Interface
'''
 1.  Initialize the repository
        - Repository holds the business entities
        - Acts like the program's database
        - Does not know about any other components
'''

while True:

    print("From where do you want to read:")
    print("1- text file")
    print("2- binary file")
    com=input("Give the command:")
    
    if com=='1':   
        pers=FilePersonRepository("D:\Faculta\python projects\lab5-7\init_person.txt")
        acts=FileActivityRepository("D:\Faculta\python projects\lab5-7\init_activity.txt",pers)
        break
    elif com=='2':
        pers=PicklePersonRepository("D:\Faculta\python projects\lab5-7\init_person_pi.pickle")
        acts=PickleActivityRepository("D:\Faculta\python projects\lab5-7\init_activity_pi.pickle",pers)
        break
    else:
        print("Wrong command!")

undocontroller=UndoController()

pers_undo=[[11,'Maria Pop','0705835438','Aleea Tarnavelor nr.9'],[15,'Alexandru Buhai','0647537454','Strada Potaisa nr.60'],[1,'Gigi Luigi','0245632656','Aleea Padin nr.12'],[2,'Adi Costea','0543627546','Strada Brasov nr.2'],[3,'Gigel Frone','0245635422','Bulevardu Eroilor nr.10'],[4,'Adrian Marian','0547727546','Strada Emil-Isaac nr.2'],[8,'Alexandru Tothazan','0245632656','Aleea Padin nr.6'],[10,'Felix Dulca','0770123554','Strada Gh. Alexandrescu nr.67'],[9,'Lucian Cui','0242012489','Bulevardu 1 Decembrie nr.1'],[7,'Paul Marian','0547754298','Strada Emil-Isaac nr.56'],[5,'Duma Florin','0549753546','Strada Emil Racovita nr.29'],[12,'Pinte Laurentiu','0865435765','Aleea Baita nr.15'],[13,'Bordeiu Andrei','0770125889','Buleverdu Muncii nr.6'],[19,'Lucian Cotrau','0771334600','Bulevardu 30 Decembrie nr.10'],[17,'Pop George','0772456343','Strada Ion Budai Deleanu nr.21'],[18,'Andrei Pop','0743256765','Aleea Raabe-Duhamel nr.19'],[14,'Petrica Marcel','0624111225','Strada Bucuresti nr.6'],[6,'Petrus Marius','0246588765','Aleea Padin nr.22'],[20,'Alexandru Costea','0544437658','Strada Cojocna nr.12'],[21,'Gigel Marciuc','0246789142','Bulevardu Victoria nr.19'],[22,'Adrian Minune','0556788964','Strada Stalin nr.2'],[28,'Andrei Tothazan','0725475731','Aleea Dafinului nr.16'],[30,'Felix Muresan','0770325898','Strada Lemnului nr.7'],[29,'Lucian Cuibusor','0807654574','Bulevardu 1 Decembrie nr.11'],[27,'Paul Pop','0549877651','Strada Emil-Isaac nr.76'],[25,'Duma Sebastian','0549611142','Strada Emil Racovita nr.19'],[32,'Pinte Lucian','0865208064','Alee Baba-Novac nr.15'],[33,'Bordeiu Andreea','0770453654','Buleverdu Muncii nr.60'],[39,'Andreea Cotrau','0771176594','Bulevardu 30 Decembrie nr.11'],[37,'Pop Laurentiu','0772200194','Strada Ion Creanga nr.21'],[50,'Tarmure Florina','0556836485','Strada Dorobantilor nr.29'],[52,'Rupeanu Carmen','0858764367','Aleea Baisoara nr.25'],[53,'Huluban Alexandrina','0770566111','Buleverdu Victoriei nr.60'],[59,'Petrica Anca','0771876497','Bulevardu 21 Decembrie nr.20'],[57,'Berar Liliana','0264112112','Strada Ion ALexandrescu nr.2'],[58,'Stef Florina','0981116576','Aleea Islazului nr.10'],[54,'Petrica Florentin','0676654322','Strada Cauchy nr.16'],[56,'Hontau Codruta','0246112789','Aleea Colina nr.70'],[60,'Marian Ringhilesu','0544118900','Strada Bucuresti nr.52'],[61,'Tusa Emil','0455121340','Strada Cauchy-Hadamard nr.1'],[62,'Susman Andrei','0556788100','Strada Stolnii nr.12'],[68,'Popa Octavian','0729908751','Aleea Cartii nr.80'],[64,'Codrea Nicolae','0779221706','Strada Primaverii nr.78'],[49,'Iuga Mihai','0467176200','Strada Sanatorului nr.110'],[47,'Borgovan Aurel','0889011678','Strada lacramioarelor nr.3'],[45,'Duman Florin','0770112497','Strada Emil Boc nr.10'],[42,'Pop Crenguta','0446012256','Strda Primaverii nr.150'],[43,'Muresan Ioan','0721456789','Strada Clabucet nr.6'],[79,'Rus Andrei','0720125765','Strada Dunarii nr.40'],[87,'Candela Ioan','0757123657','Strada Baba Novac nr.69']]

acts_undo=[[1,[11,15,18],'2016-6-24','16:56','No description'],[2,[1,5,19,17],'2016-6-24','8:40','No description'],[4,[2,12,5],'2016-9-30','12:45','Great View'],[3,[3,1,2],'2016-3-13','14:30','No description'],[6,[4,5,15],'2016-2-19','18:10','Awesome places'],[7,[8,11,30],'2016-8-23','16:56','Great Zoo'],[5,[10,9,6],'2016-12-24','17:08','Nice landscapes'],[10,[9,19,10],'2016-6-24','6:29','No description'],[12,[7,11,13,17],'2016-1-30','11:40','Great mountains'],[13,[1,11,17,5],'2016-5-14','6:56','No description'],[15,[17,1,19,5],'2016-8-22','16:56','Great View'],[16,[11,19,10,13],'2016-11-24','17:57','Nice landscapes'],[11,[9,10,12,17],'2016-1-14','16:29','No description'],[17,[7,19,17,1],'2016-11-30','10:40','Great mountains'],[18,[1,11,17,10,19],'2016-5-27','16:56','No description'],[14,[11,15,5,37,1],'2017-1-14','13:26','No description'],[22,[1,5,33,37,25],'2017-7-10','18:40','Sociable people'],[24,[2,12,5,29],'2017-9-20','22:45','Great View'],[23,[27,29,37,6],'2017-12-1','19:30','No description'],[26,[4,6,33,20],'2017-12-19','21:10','Awesome places'],[27,[8,11,20,21],'2017-3-4','19:56','Great Parks and Landmarks'],[25,[10,6,21,14],'2017-12-3','3:08','Nice landscapes'],[30,[9,14],'2015-9-26','6:29','No description'],[32,[7,11,30,27],'2015-11-30','19:40','Great mountains'],[33,[6,21,27],'2015-5-6','4:56','No description'],[45,[17,29],'2017-8-22','23:56','Awesome beaches and places'],[36,[11,19,10,13,29,6],'2016-1-2','17:57','Nice landscapes'],[21,[9,10,30,25],'2017-1-1','23:29','Nice people and places'],[37,[37,33,39,1],'2017-1-30','10:40','Great mountains'],[28,[39,6],'2016-7-29','13:16','No description'],[75,[50,79,19,5,1],'2016-8-20','14:56','Great View and Landscapes'],[76,[47,79,42,1,11,45],'2016-1-14','1:57','Nice weather'],[71,[9,50,1,60,87],'2018-11-14','16:19','No description'],[77,[60,50,61,62],'2018-11-30','10:40','High mountains'],[78,[1,11,87,43,49],'2017-7-24','18:56','No description'],[74,[11,1,87,79,53],'2017-10-14','13:40','No description'],[72,[1,5,33,37,25,87],'2017-3-30','18:41','Sociable people'],[79,[61,62,59],'2019-9-20','22:45','Great Landscapes'],[73,[61,37,6],'2017-12-11','19:35','No description'],[66,[87,79,54,56],'2018-10-11','21:10','Awesome places'],[67,[49,47],'2019-3-4','19:56','Great Parks and Landmarks'],[65,[42,43,45],'2019-12-3','3:08','Nice landscapes'],[60,[50,52,53],'2018-4-26','16:59','No description'],[62,[7,11,60,50],'2015-3-30','18:40','Great mountains'],[63,[87,50,68],'2019-1-16','14:56','No description'],[55,[17,29,57,54],'2017-8-1','2:56','Awesome beaches'],[56,[29,6,87],'2019-4-2','15:57','Nice landscapes'],[51,[37,60,50,37,87],'2017-11-11','23:1','Nice places'],[57,[37,22,21,68,9,7,1],'2018-11-30','11:48','Great mountains'],[58,[39,6,60,18,28,32],'2019-9-19','12:16','No description']]
'''
    2. Initialize the controller
        - The controller implements the program's 'operation'
        - Knows only about the repository layer
        - 'Talks' to the repository and UI using parameter passing and exceptions
'''

perscontroller=PersControllerUndo(pers,undocontroller,acts)
actscontroller=ActControllerUndo(acts,undocontroller,pers)


'''
    3. Initialize the user interface
        - The UI implements all user interactions
        - Only knows about the controller layer
        - Calls functions from the controller to implement program features
        - Might include some data validation, as a fast-fail mechanism
'''

ui=Interface(perscontroller,actscontroller,undocontroller)


'''
    4. Start the application's user interface
'''

ui._interface()
