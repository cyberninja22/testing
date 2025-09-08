import logging 
#creating a new logger
logger = logging.getLogger(__name__)

#setting the logging levels
logger.setLevel(logging.INFO)
#setting up the formatter
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')


#setting up the employee log file
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee: 
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        logger.info('Created Employees: {} {}'.format(self.fullname, self.email))
    
    @property
    def email(self):
        return ('{}.{}@gmail.com'.format(self.first_name,self.last_name))
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
e1 = Employee('Nandan','Kela')
e2= Employee('Rohan','Varma')
e3=Employee('Mohsin','Moku')       