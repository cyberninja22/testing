import logging
import employee

"""
DEBUG	10	Detailed information for diagnosing problems
INFO	20	Confirmation that things are working as expected
WARNING	30	Indicates something unexpected or potential issues
ERROR	40	A serious problem preventing a function from executing
CRITICAL	50
"""

logger = logging.getLogger(__name__)
format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(format)

logger.addHandler(file_handler)


#adding a streamHAndler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)

#changing the basic logging config
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s' )

def add (x,y):
    """Add Function"""
    return x+y 

def subtract(x,y):
    """Subtract function"""
    return x-y 
def multiply(x,y):
    """multiply function"""
    return x*y 

def divide (x,y):
    """divide function"""
    try:
        result=  x/y 
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 20 
num_2 = 0 

add_result = add(num_1,num_2)
logger.info('Add: {} + {} = {}'.format(num_1,num_2,add_result))

subtract_result = subtract(num_1,num_2)
logger.info('subtract: {} + {} = {}'.format(num_1,num_2,subtract_result))

multiply_result = multiply(num_1,num_2)
logger.info('multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))

divide_result = divide(num_1,num_2)
logger.info('divide: {} + {} = {}'.format(num_1,num_2,divide_result))

logger.error("Lavde lag gaye bhai")

print(logging.WARNING)

