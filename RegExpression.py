import re

examplesString = '''Jessica is 15 years old, and Daniel is 27 years old.  
Edward is 97, and his grandfather, Oscar is 102'''

ages = re.findall(r'\d{1,3}', examplesString)
names = re.findall(r'[A-Z][a-z]*', examplesString)

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)