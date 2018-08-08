'''
import re

nameage="
Abc is 18 years old
 Xyz is 20 years old
 Mno is 22 years old"

names=re.findall('[A-Z][A-z]*',nameage)
print(names)
ages=re.findall('\d{1,3}',nameage)
print(ages)

'''
import re
email='''isha31198@gmail.com
gatj7879gmail.com
yhsuj63@.com
'''
match=re.findall('[\w_$+-=]{1,20}[@][\w]{1,20}[.][\w]{1,3}',email)
print(match)


'''
import re
strr='sat cat mat rat'
regex=re.compile("[c]at")
regex=re.compile("[c,m]at")
strr=regex.sub("strr",strr)
print(strr)

'''