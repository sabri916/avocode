import xml.etree.ElementTree as ET
from avocode_util import *


tree = ET.parse('avocode_ui.xml')
root = tree.getroot()
createDocument(root)
   

