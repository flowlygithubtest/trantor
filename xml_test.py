#  python code to replace DEPART and RETURN with current date
import xml.etree.ElementTree as ET
from datetime import date
def xml_method(ele1, ele2):
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    ct = str(date.today()).replace("-","")
    root.find('REQUEST').find('TP').find(ele1).text = ct
    root.find('REQUEST').find('TP').find(ele2).text = ct
    tree.write( 'test_payload1_update.xml' )
xml_method("DEPART","RETURN")