import os
from xml.etree import ElementTree

filename = 'D:\\Downloads\\Current_SystemConfig.xml'

dom = ElementTree.parse(filename)

progname = dom.findall('Program')
for item in progname:
    program = item.text

tphase = dom.findall('TestPhase')
for item in tphase:
    phase = item.text

items = dom.findall(program + "_" + phase + "_CONFIG")

for item in items:
    sts_common = item.find('STS_CONFIG/STS_PRODUCT_LINE_DESCRIPTION').text
    prog_specific = item.find(program + '_CONFIG/STS_PROGRAM_SPECIFIC_DESCRIPTION').text
    sc_specific = item.find(program + '_CONFIG/STS_SC_SPECIFIC_DESCRIPTION').text

print("STS Common Software: ", sts_common)
print("Program Common Software: ", prog_specific)
print("S/C Specific Software", sc_specific)

