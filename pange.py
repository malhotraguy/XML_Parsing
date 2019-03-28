import xml.etree.ElementTree as ET
import numpy as np

def parseXML(xmlfile,ComponentItems):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # iterate Bug tags
    for item in root.findall('./Bug'):

        # iterate child elements of Bug
        for child in item:

            # checking each tag under the Bug Tag
            if child.tag == 'BugId':
                BugId = child.attrib['amount']
            if child.tag == 'component':
                if child.attrib['amount']:

                    if child.attrib['amount'] not in ComponentItems:
                        ComponentItems[child.attrib['amount']] = np.array([BugId])
                    else:

                        ComponentItems[child.attrib['amount']]=np.append(ComponentItems[child.attrib['amount']],BugId)

            else:
                pass
    return ComponentItems

ComponentItems = {}
for n in range(1,136901,100):
    parseXML("EEE//bugs{0}-{1}.xml".format(n,n+99),ComponentItems )
with open('output2.txt',"w") as output:
    print(ComponentItems,file=output)
    print(ComponentItems)
from PANGE2 import *
Paring(ComponentItems,2)

