# Regular Expression
import re
text = "Albania,Andorra,Armenia,Austria,Azerbaijan,Belarus,Belgium,Bosnia & Herzegovina,Bulgaria,Croatia,Cyprus,Czechia,Denmark,Estonia,Finland,France,Georgia,Germany,Greece,Hungary,Iceland,Ireland,Italy,Kazakhstan,Kosovo,Latvia,Liechtenstein,Lithuania,Luxembourg,Malta,Moldova,Monaco,Montenegro,Netherlands,North Macedonia,Norway,Poland,Portugal,Romania,Russia,San Marino,Serbia,Slovakia,Slovenia,Spain,Sweden,Switzerland,Turkey,Ukraine,United Kingdom,Vatican City"

find_land = re.findall(r'\w+lands*',text)
print("List of countries whose name ends with 'land' \n" + str(find_land))

match = re.search('Bangla','Bangladesh')
# print(match)
# print(match.group())

info = "Name: Akash Mallik; Id: 163015044; Mobile: 01777334628 019 16659114 000 00000000; Address: Dhaka, Bangladesh"
#find = re.search('.',info)
#find = re.search('A..',info)
#find = re.search('A.*',info)
#find = re.search('A.*M',info)
#find = re.search('A.*?M',info)
#find = re.search('M\w\w\w\w\w',info)
#find = re.search('M\w*',info)

#print(find.group())

#find = re.findall('M\w*',info)
#print(find)

#mobile = re.findall('\d+', info)
#mobile = re.findall('\d{11}', info)
#mobile = re.findall(r'\d{3}\s?\d{8}', info)
mobile = re.findall(r'01[56789]\s?\d{8}', info)
print('\nFind mobile form info' + str(mobile))
