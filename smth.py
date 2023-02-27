
from models import *
from service import *
card0=addCard(number='123', valid_thru='29/09', holder_name='Store', cvc=100)

acc = addUser(card0, login='login', password='password', FIO='myName')
