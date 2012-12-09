import xml.etree.ElementTree as ET
import sys
from avocode_util import *

for i in sys.argv:
    print i

if len(sys.argv)>3:
    print 'Too many arguments'
    print 'EXAMPLE: avocode_gen XMLfile outputFile'
    exit()
    
if len(sys.argv)<=1:
    print 'Specify XML file'
    exit()

tree = ET.parse(sys.argv[1])
root = tree.getroot()
createDocument(root,sys.argv[2])