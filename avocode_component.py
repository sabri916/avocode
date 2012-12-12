class Component:
    """This is the root of all tagClasses"""
    def __init__(self,ID,avocodeTag=''):
        self.ID=ID
        self.avocodeTag=avocodeTag

class Button(Component):
    """button tag class
    Required Arguments: ID, ButtonLabel, Action
    """
    def __init__(self,ID,label,action,class_att='btn'):
        Component.__init__(self,ID,'button')
        self.label=label #label
        self.action=action #destination page
        self.class_att=class_att #html class attribute for 'btn from bootstrap
        self.html = '<a name=\"'+self.ID+'\" class=\"'+self.class_att+'\" href=\"'+self.action+'\">'+self.label+'</a>'
    
    def getHtml(self):
        return self.html


class Text(Component):
    """text tag class
    Required Arguments: ID and exec
    """
    def __init__(self,ID,handler,class_att=''):
        Component.__init__(self,ID,'text')
        self.handler=handler #destination page
        self.class_att=class_att #html class attribute for 'btn from bootstrap
        self.html = '<input name=\"'+self.ID+'\" class=\"'+self.class_att+'\" type=\"text\" placeholder=\"\">'
        
    def getHtml(self):
        return self.html