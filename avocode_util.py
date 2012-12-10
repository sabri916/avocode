import avocode_component as comp

def componentFactory(node):
    """
    Require parameters:
    *xml node
    """
    if node.tag=='button':
        b=comp.Button(node.attrib['id'],node.text,'yellow')
        return b
    
    if node.tag=='text':
        t=comp.Text(node.attrib['id'],node.attrib['handler'])
        return t


def createDocument(root,filename='output.html'):
    f=open(filename,'w')
    f.write('<html>\n<head>\n<script src="bootstrap/js/bootstrap.js"></script>\n<link href="bootstrap/css/bootstrap.css" rel="stylesheet type="text/css" />\n</head>\n<body>\n')
    
    for i in root:
        component=componentFactory(i)
        html=component.getHtml()
        f.write(html+'\n')
    
    f.write('</body>\n<html>')

