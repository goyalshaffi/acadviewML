
import datetime

#print(datetime.date)



import datetime,time,math
'''
print(time.gmtime())
print(time.localtime())
print(time.asctime(time.localtime()))
'''

t1=time.localtime()
print(time.asctime(t1))

print(datetime.date.today())

'''

from datetime import date
print(date.today())



import os
print(os.getcwd())
print(os.name)
print(os.environ)
'''



struct_time=time.strptime("30 nov 00","%d %b %y")
print"returned tuple:%s"% struct_time.tm_mday
