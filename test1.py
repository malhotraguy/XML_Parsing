import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()
    #print(root)

    # create empty list for news items
    ComponentItems = {}

    # iterate news items
    for item in root.findall('./Bug'):
        #print(item)

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:

            # special checking for namespace object content:media
            #print(child.tag)
            if child.tag == 'BugId':
                BugId = child.attrib['amount']
            if child.tag == 'component':

                #news['component'] = child.attrib['amount']
                if child.attrib['amount'] not in ComponentItems:
                    ComponentItems[child.attrib['amount']] =[BugId]
                else:
                    ComponentItems[child.attrib['amount']].append(BugId)



            else:
                pass

            

    # return news items list
    return ComponentItems
print(parseXML("//home//rahul//Downloads//EEE//bugs1-100.xml"))